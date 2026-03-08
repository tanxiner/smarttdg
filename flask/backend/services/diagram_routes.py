from flask import Flask, jsonify, send_from_directory, request, send_file, after_this_request
import re
import os
import json
import tempfile
import zipfile
import shutil
import time
import uuid
import threading
import subprocess
from pathlib import Path
from typing import Dict, Any

def register_diagram_routes(app: Flask):
    """Register diagram-related routes with the Flask app."""
    
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    # Use the standard static output directory
    STATIC_OUTPUT_DIR = os.path.join(BASE_DIR, "static_analysis_output")
    
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(STATIC_OUTPUT_DIR, exist_ok=True)
    
    DIAGRAM_JOBS: Dict[str, Dict[str, Any]] = {}

    def _update_diagram_job(job_id: str, **kwargs):
        st = DIAGRAM_JOBS.setdefault(job_id, {})
        st.update(kwargs)

    def _is_diagram_job_canceled(job_id: str) -> bool:
        st = DIAGRAM_JOBS.get(job_id) or {}
        return bool(st.get("canceled")) or st.get("step") in ("cancel_requested", "canceled")

    @app.route("/diagram_cancel/<job_id>", methods=["POST"])
    def cancel_diagram_job(job_id: str):
        st = DIAGRAM_JOBS.get(job_id)
        if not st:
            return jsonify({"error": "job not found"}), 404

        st["step"] = "cancel_requested"
        st["canceled"] = True
        st.setdefault("progress", 0)

        # Note: current implementation can't stop the running analyzer thread.
        # This just makes the UI stop and the status reflect cancellation.
        st["step"] = "canceled"
        st["progress"] = 0
        return jsonify({"status": "ok", "message": "cancel requested"}), 200

    @app.route("/upload_for_diagrams", methods=["POST"])
    def upload_for_diagrams():
        """Upload ZIP file specifically for diagram generation only."""
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']
        if not file.filename.lower().endswith(".zip"):
            return jsonify({"error": "Only .zip files are supported"}), 400

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        job_id = str(uuid.uuid4())
        DIAGRAM_JOBS[job_id] = {
            "progress": 0, 
            "step": "queued", 
            "created": time.time(),
            "filename": file.filename
        }
        
        def _run_diagram_analysis():
            try:
                _update_diagram_job(job_id, progress=10, step="extracting")
                
                # Clear previous diagrams
                diagrams_dir = os.path.join(BASE_DIR, "analysis_output", "Diagrams")
                if os.path.exists(diagrams_dir):
                    try:
                        for f in os.listdir(diagrams_dir):
                            os.remove(os.path.join(diagrams_dir, f))
                    except: pass

                # Ensure output directory is clean/ready
                os.makedirs(STATIC_OUTPUT_DIR, exist_ok=True)
                analysis_results_file = os.path.join(STATIC_OUTPUT_DIR, "all_analysis_results.json")
                # Remove old results file to avoid confusion
                if os.path.exists(analysis_results_file):
                    try:
                        os.remove(analysis_results_file)
                    except: pass

                # Create temp directory
                sys_tmp = Path(tempfile.gettempdir())
                short_base = os.path.join(sys_tmp.drive + os.sep, "sdtg_tmp_diag")
                os.makedirs(short_base, exist_ok=True)
                temp_dir = tempfile.mkdtemp(prefix="diag_", dir=short_base)
                
                try:
                    # Extract ZIP
                    with zipfile.ZipFile(filepath, 'r') as z:
                        z.extractall(temp_dir)
                    
                    _update_diagram_job(job_id, progress=30, step="running_static_analysis")
                    
                    # File collection logic
                    all_paths = list(Path(temp_dir).rglob("*"))
                    desired_suffixes = {".cs", ".vb", ".aspx", ".ascx", ".master", ".js", ".jsx", ".html"}
                    irrelevant_tokens = { "obj", "bin", "node_modules", "packages", ".git", ".vs", "debug", "release" }
                    
                    files_to_analyze = []
                    for p in all_paths:
                        if p.is_file() and p.suffix.lower() in desired_suffixes:
                            is_junk = False
                            try:
                                rel = p.relative_to(temp_dir)
                                for part in rel.parts:
                                    if part.lower() in irrelevant_tokens:
                                        is_junk = True
                                        break
                            except: pass
                            
                            if not is_junk:
                                files_to_analyze.append(p)
                    
                    if not files_to_analyze:
                        _update_diagram_job(job_id, progress=100, step="error", error="No supported source files found")
                        return

                    cwd_before = os.getcwd()
                    os.chdir(temp_dir)
                    rel_paths = [str(p.relative_to(temp_dir)) for p in files_to_analyze]
                    unique_rel_paths = list(set([p.replace("\\", "/") for p in rel_paths]))

                    try:
                        # --- RUN ANALYZER ---
                        import services.analyzer.analyzer_runner as analyzer_runner
                        
                        # Set env vars to force analyzer to write to our known location
                        os.environ["ANALYZER_JOB_ID"] = job_id
                        os.environ["ANALYZER_TEMP_DIR"] = temp_dir
                        os.environ["ANALYZER_OUTPUT_DIR"] = STATIC_OUTPUT_DIR # Explicitly set output dir
                        
                        flask_root = os.path.dirname(BASE_DIR)
                        if os.path.isdir(flask_root):
                            os.environ["FLASK_ROOT"] = flask_root
                            
                        print(f"[DiagramJob] Running analyzer on {len(unique_rel_paths)} files -> {STATIC_OUTPUT_DIR}")
                        
                        # Run analyzer
                        # We don't care about the return value's data content anymore, just success/fail.
                        # The real data goes to the file.
                        
                        def _on_static_progress(curr, tot):
                            if tot > 0:
                                # Map 0..1 to 30..90 range for diagrams phase
                                # Static analysis is the main lengthy part, diagram generation is fast
                                ratio = min(curr, tot) / tot
                                p = 30 + int(ratio * 60)
                                _update_diagram_job(job_id, progress=p, 
                                                  step=f"analyzing_file_{curr}_of_{tot}")

                        result_meta = analyzer_runner.analyze_code(*unique_rel_paths, job_id=job_id, progress_callback=_on_static_progress)
                        
                        # Check if file exists now
                        if not os.path.exists(analysis_results_file):                            
                            _update_diagram_job(job_id, progress=100, step="error", 
                                              error="Analyzer finished but no output file was created.")
                            return

                        # --- NEW STRATEGY: Read from file ---
                        print(f"[DiagramJob] Reading analysis results from: {analysis_results_file}")
                        try:
                            with open(analysis_results_file, 'r', encoding='utf-8') as f:
                                analysis_data = json.load(f)
                        except Exception as e:
                            _update_diagram_job(job_id, progress=100, step="error", 
                                              error=f"Failed to read analysis output file: {str(e)}")
                            return

                        _update_diagram_job(job_id, progress=90, step="generating_diagrams")
                        
                        # Validate data
                        if not analysis_data or not isinstance(analysis_data, list):
                             # Sometimes it might wrap it? But typically Program.cs writes List<object>
                             if isinstance(analysis_data, dict) and "analysis" in analysis_data: # Just in case
                                 analysis_data = analysis_data["analysis"]
                             
                             if not isinstance(analysis_data, list):
                                 analysis_data = [analysis_data] if analysis_data else []

                        if not analysis_data:
                             _update_diagram_job(job_id, progress=100, step="error", error="Analysis resulted in empty data")
                             return

                        # Generate diagrams
                        from services.analyzer.diagram_generator import DiagramGenerator
                        generator = DiagramGenerator(analysis_data)
                        diagrams = generator.generate_all_diagrams()
                        
                        _update_diagram_job(job_id, progress=100, step="done", 
                                          diagrams_generated=len(diagrams),
                                          result={"diagrams": diagrams})

                    finally:
                        try:
                            os.chdir(cwd_before)
                        except: pass

                finally:
                    shutil.rmtree(temp_dir, ignore_errors=True)
                    try:
                        os.remove(filepath)
                    except: pass
                        
            except Exception as e:
                import traceback
                traceback.print_exc()
                _update_diagram_job(job_id, progress=100, step="error", error=str(e))
        
        thread = threading.Thread(target=_run_diagram_analysis, daemon=True)
        thread.start()
        
        return jsonify({"jobId": job_id}), 202
    
    @app.route("/diagram_status/<job_id>", methods=["GET"])
    def diagram_job_status(job_id):
        st = DIAGRAM_JOBS.get(job_id)
        if not st: return jsonify({"error": "job not found"}), 404
        return jsonify(st)
    
    @app.route("/generate_diagrams", methods=["POST"])
    def generate_diagrams():
        try:
            analysis_file = os.path.join(BASE_DIR, "static_analysis_output", "all_analysis_results.json")
            if not os.path.exists(analysis_file):
                return jsonify({"error": "Static analysis file not found."}), 404
            
            with open(analysis_file, 'r', encoding='utf-8') as f:
                analysis_data = json.load(f)
            
            from services.analyzer.diagram_generator import DiagramGenerator
            generator = DiagramGenerator(analysis_data)
            diagrams = generator.generate_all_diagrams()
            
            diagram_info = []
            for dtype, path in diagrams.items():
                rel_path = os.path.relpath(path, BASE_DIR).replace("\\", "/")
                diagram_info.append({
                    "type": dtype,
                    "filename": os.path.basename(path),
                    "path": rel_path,
                    "size": os.path.getsize(path) if os.path.exists(path) else 0
                })
            
            return jsonify({"status": "success", "diagrams": diagram_info})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route("/diagrams/<path:filename>", methods=["GET"])
    def serve_diagram(filename):
        diagrams_dir = os.path.join(BASE_DIR, "analysis_output", "Diagrams")
        return send_from_directory(diagrams_dir, filename, as_attachment=False, mimetype="text/markdown")
    
    @app.route("/diagrams", methods=["GET"])
    def list_diagrams():
        diagrams_dir = os.path.join(BASE_DIR, "analysis_output", "Diagrams")
        if not os.path.exists(diagrams_dir): return jsonify({"diagrams": []})
        
        diagram_files = []
        for filename in os.listdir(diagrams_dir):
            if filename.endswith('.md'):
                dtype = filename.replace('.md', '')
                diagram_files.append({
                    "type": dtype,
                    "filename": filename,
                    "path": f"diagrams/{filename}",
                    "size": os.path.getsize(os.path.join(diagrams_dir, filename))
                })
        return jsonify({"diagrams": diagram_files})

    @app.route("/diagrams", methods=["DELETE"])
    def clear_diagrams():
        try:
            diagrams_dir = os.path.join(BASE_DIR, "analysis_output", "Diagrams")
            count = 0
            if os.path.exists(diagrams_dir):
                for filename in os.listdir(diagrams_dir):
                    try:
                        os.remove(os.path.join(diagrams_dir, filename))
                        count += 1
                    except: pass
            return jsonify({"message": f"Cleared {count} diagrams", "count": count})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/diagrams/<diagram_type>/svg", methods=["GET"])
    def download_diagram_svg(diagram_type):
        """
        Export diagram(s) to SVG using Node+Playwright exporter.

        Special handling:
        - If class_diagram.md is NOT a mermaid diagram (e.g., an index),
          auto-pick the first split part instead.
        """
        diagrams_dir = os.path.join(BASE_DIR, "analysis_output", "Diagrams")

        def has_mermaid_block(path: str) -> bool:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    md = f.read()
                return re.search(r"```mermaid\s*([\s\S]*?)```", md, re.IGNORECASE) is not None
            except:
                return False

        def pick_md_file() -> str:
            # default behavior
            primary = os.path.join(diagrams_dir, f"{diagram_type}.md")
            if os.path.exists(primary) and has_mermaid_block(primary):
                return primary

            # special: class_diagram may be split
            if diagram_type == "class_diagram":
                # Prefer paged files first (p1)
                candidates = []
                for fn in os.listdir(diagrams_dir):
                    if not fn.endswith(".md"):
                        continue
                    # class_diagram__TAMS__p1.md etc
                    if fn.startswith("class_diagram__") and ("__p1.md" in fn or fn.count("__") == 1):
                        candidates.append(fn)

                # stable ordering: p1 first then alpha
                def sort_key(fn: str):
                    # p1 first, then p2...
                    m = re.search(r"__p(\d+)\.md$", fn)
                    if m:
                        return (0, int(m.group(1)), fn.lower())
                    return (1, 999999, fn.lower())

                candidates.sort(key=sort_key)

                for fn in candidates:
                    path = os.path.join(diagrams_dir, fn)
                    if has_mermaid_block(path):
                        return path

            # fallback: if file exists but no mermaid, still return primary for proper error msg
            return primary

        md_file = pick_md_file()

        if not os.path.exists(md_file):
            return jsonify({"error": f"Diagram not found: {os.path.basename(md_file)}"}), 404

        node_script = os.path.join(BASE_DIR, "render_mermaid_svg.mjs")
        if not os.path.exists(node_script):
            return jsonify({"error": f"Exporter script not found: {node_script}"}), 500

        tmp_dir = None

        try:
            # 1) Read MD
            with open(md_file, "r", encoding="utf-8") as f:
                md = f.read()

            # 2) Extract mermaid block
            m = re.search(r"```mermaid\s*([\s\S]*?)```", md, re.IGNORECASE)
            if not m:
                return jsonify({
                    "error": "No ```mermaid``` block found",
                    "file": os.path.basename(md_file)
                }), 400

            mermaid_src = m.group(1).strip()
            if not mermaid_src:
                return jsonify({"error": "Mermaid block is empty"}), 400

            print("[SVG EXPORT] diagram_type =", diagram_type)
            print("[SVG EXPORT] md_file =", md_file)
            print("[SVG EXPORT] mermaid_src length =", len(mermaid_src))
            print("[SVG EXPORT] node_script =", node_script)

            # 3) Create a temp working dir
            tmp_dir = tempfile.mkdtemp(prefix=f"svgexp_{diagram_type}_")

            def run_export(mmd_text: str, out_svg_path: str):
                mmd_path = os.path.join(tmp_dir, f"input_{uuid.uuid4().hex}.mmd")
                with open(mmd_path, "w", encoding="utf-8") as mf:
                    mf.write(mmd_text)

                res = subprocess.run(
                    ["node", node_script, mmd_path, out_svg_path],
                    cwd=BASE_DIR,
                    capture_output=True,
                    text=True,
                    timeout=180
                )

                print("[SVG EXPORT] node returncode =", res.returncode)
                if res.stdout:
                    print("[SVG EXPORT] node stdout (first 2k) =", res.stdout[:2000])
                if res.stderr:
                    print("[SVG EXPORT] node stderr (first 2k) =", res.stderr[:2000])

                if res.returncode != 0:
                    raise RuntimeError(res.stderr or res.stdout or "Node exporter failed")

            # 4) Heuristic split: if too many lines/edges, split into multiple parts
            lines = mermaid_src.splitlines()

            # Keep the first "graph ..." / "flowchart ..." / "classDiagram" line as header
            header = None
            body = []

            for ln in lines:
                stripped = ln.strip()
                if header is None and stripped.startswith(("graph", "flowchart", "classDiagram")):
                    header = stripped
                    # only rewrite direction for graph/flowchart (NOT classDiagram)
                    if header.startswith(("graph", "flowchart")):
                        header = re.sub(r"\b(LR|RL)\b", "TD", header)
                else:
                    body.append(ln)

            if header is None:
                # fall back — better than failing
                header = "flowchart TD"

            MAX_BODY_LINES_SINGLE = 2500
            CHUNK_BODY_LINES = 2000

            # ✅ classDiagram should not be split by line-chunking (it breaks braces)
            # If it's too large, you should already have split files. So just export single.
            if header.strip() == "classDiagram":
                out_svg = os.path.join(tmp_dir, f"{diagram_type}.svg")
                run_export("\n".join([header] + body), out_svg)

                @after_this_request
                def cleanup(response):
                    try:
                        shutil.rmtree(tmp_dir, ignore_errors=True)
                    except:
                        pass
                    return response

                return send_file(
                    out_svg,
                    as_attachment=True,
                    download_name=f"{diagram_type}.svg",
                    mimetype="image/svg+xml"
                )

            if len(body) <= MAX_BODY_LINES_SINGLE:
                out_svg = os.path.join(tmp_dir, f"{diagram_type}.svg")
                run_export("\n".join([header] + body), out_svg)

                @after_this_request
                def cleanup(response):
                    try:
                        shutil.rmtree(tmp_dir, ignore_errors=True)
                    except:
                        pass
                    return response

                return send_file(
                    out_svg,
                    as_attachment=True,
                    download_name=f"{diagram_type}.svg",
                    mimetype="image/svg+xml"
                )

            # Multi-part export -> ZIP (for flowcharts only)
            svg_paths = []
            part = 1
            for i in range(0, len(body), CHUNK_BODY_LINES):
                chunk = body[i:i + CHUNK_BODY_LINES]
                out_svg = os.path.join(tmp_dir, f"{diagram_type}_part{part}.svg")
                run_export("\n".join([header] + chunk), out_svg)
                svg_paths.append(out_svg)
                part += 1

            zip_path = os.path.join(tmp_dir, f"{diagram_type}_svgs.zip")
            with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
                for p in svg_paths:
                    z.write(p, arcname=os.path.basename(p))

            @after_this_request
            def cleanup(response):
                try:
                    shutil.rmtree(tmp_dir, ignore_errors=True)
                except:
                    pass
                return response

            return send_file(
                zip_path,
                as_attachment=True,
                download_name=f"{diagram_type}_svgs.zip",
                mimetype="application/zip"
            )

        except subprocess.TimeoutExpired:
            if tmp_dir:
                shutil.rmtree(tmp_dir, ignore_errors=True)
            return jsonify({"error": "SVG export timed out"}), 500

        except Exception as e:
            if tmp_dir:
                shutil.rmtree(tmp_dir, ignore_errors=True)
            return jsonify({"error": str(e)}), 500

    print(f"[DiagramRoutes] Registered diagram routes with BASE_DIR: {BASE_DIR}")