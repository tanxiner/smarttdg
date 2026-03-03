from flask import Flask, jsonify, send_from_directory, request
import os
import json
import tempfile
import zipfile
import shutil
import time
import uuid
import threading
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
                        result_meta = analyzer_runner.analyze_code(*unique_rel_paths, job_id=job_id)
                        
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

                        _update_diagram_job(job_id, progress=60, step="generating_diagrams")
                        
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

    print(f"[DiagramRoutes] Registered diagram routes with BASE_DIR: {BASE_DIR}")