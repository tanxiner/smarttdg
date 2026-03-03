from flask import Flask, request, jsonify, send_from_directory
import os
from time import sleep
import tempfile
import zipfile
import shutil
import time
from pathlib import Path
import threading
import uuid
from typing import Dict, Any
import platform
import ctypes
import subprocess
import sys

# Import the analyzer runner module (we need to call cancel_analyzer)
import services.analyzer.analyzer_runner as analyzer_runner
# keep a local alias for convenience
run_analyzer = analyzer_runner.analyze_code

# Add this import at the top with other imports
from services.diagram_routes import register_diagram_routes

BASE_DIR = os.path.dirname(__file__)
app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, '..', 'frontend', 'build'),
    static_url_path='/'
)

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

JOB_STATUS: Dict[str, Dict[str, Any]] = {}

def _update_job(job_id: str, **kwargs):
    st = JOB_STATUS.setdefault(job_id, {})
    st.update(kwargs)

def analyze_zip(zip_path: str, job_id: str | None = None) -> dict:
    _update_job(job_id, progress=5, step="queued") if job_id else None

    # --- Explicitly clear output folders and OLD MANIFESTS at start ---
    prompts_base = os.path.join(BASE_DIR, "prompts_output")
    analysis_base = os.path.join(BASE_DIR, "analysis_output")
    
    # 1. Clear prompt/analysis subfolders
    dirs_to_clean = [
        os.path.join(prompts_base, "Page_Documentation_Prompts"),
        os.path.join(prompts_base, "Utility_Documentation_Prompts"),
        os.path.join(prompts_base, "SQL_Documentation_Prompts"),
        os.path.join(analysis_base, "Final_Documentation_Chapters"),
        os.path.join(analysis_base, "Final_Utility_Chapters"),
        os.path.join(analysis_base, "Final_SQL_Docs")
    ]

    for d in dirs_to_clean:
        if os.path.exists(d):
            try:
                shutil.rmtree(d)
                os.makedirs(d, exist_ok=True)
            except Exception:
                pass
    
    # 2. Clear old manifest files in the prompts root
    if os.path.exists(prompts_base):
        try:
            for f in os.listdir(prompts_base):
                if f.startswith("manifest_") and f.endswith(".json"):
                    try:
                        os.remove(os.path.join(prompts_base, f))
                    except Exception:
                        pass
        except Exception:
            pass
    # ------------------------------------------------

    # create a short temp base on the same drive as the system temp to avoid very long paths
    sys_tmp = Path(tempfile.gettempdir())
    short_base = os.path.join(sys_tmp.drive + os.sep, "sdtg_tmp")
    os.makedirs(short_base, exist_ok=True)

    temp_dir = tempfile.mkdtemp(prefix="smarttdg_", dir=short_base)
    try:
        _update_job(job_id, progress=10, step="extracting") if job_id else None

        with zipfile.ZipFile(zip_path, 'r') as z:
            print("Files in ZIP:", [f.filename for f in z.infolist()])
            z.extractall(temp_dir)
            print("Extracted files:", list(Path(temp_dir).rglob("*")))

        # --- Pass SQL input info to downstream analyzer scripts ---
        # UPDATED: Collect ALL .sql files, not just the first one.
        # Check specific scripts (sql_splitter.py) to ensure they handle multiple files or catch all.
        # We will pass a semicolon-delimited string of paths.
        try:
            os.environ["ANALYZER_TEMP_DIR"] = temp_dir
            
            sql_files = []
            for p in Path(temp_dir).rglob("*.sql"):
                sql_files.append(str(p))
            
            if sql_files:
                # Join with ; or another delimiter. Ensure your sql_splitter can handle this.
                # If sql_splitter only takes one file, this change implies you need to update sql_splitter 
                # to split strings or iterate the list on the receiving end.
                # For safety, let's assume the splitter can be updated or we pick the largest one?
                # Actually, standard env var "ANALYZER_SQL_FILE" usually implies one file.
                # Let's combine paths with a delimiter that valid windows paths won't contain: ';'
                combined_sql_paths = ";".join(sql_files)
                os.environ["ANALYZER_SQL_FILE"] = combined_sql_paths
                
                _update_job(job_id, analyzer_sql_file=combined_sql_paths) if job_id else None
                print(f"[Debug] ANALYZER_SQL_FILE set to: {combined_sql_paths} ({len(sql_files)} files)")
            else:
                os.environ.pop("ANALYZER_SQL_FILE", None)
        except Exception as _:
            pass

        # Recursively collect files we want to analyze (code-behind and markup)
        all_paths = list(Path(temp_dir).rglob("*"))
        dirs = [p for p in all_paths if p.is_dir()]

        desired_suffixes = {
            ".cs", ".vb",          # code-behind / source files
            ".aspx", ".ascx", ".master",  # WebForms markup
            ".js", ".jsx",    # JavaScript / TypeScript / JSX / TSX
            ".html"                  # static HTML
        }

        irrelevant_tokens = {
            "obj", "bin", "node_modules", "packages", ".git", "properties", "plugins",
            ".vs", "debug", "release", "publish", "_published"
        }

        def _is_in_irrelevant_dir(path: Path) -> bool:
            try:
                rel = path.relative_to(temp_dir)
            except Exception:
                return False
            for part in rel.parts:
                pl = part.lower()
                if pl in irrelevant_tokens:
                    return True
                for tok in irrelevant_tokens:
                    if tok and tok in pl:
                        return True
            return False

        def _is_designer_file(path: Path) -> bool:
            try:
                name = path.name.lower()
            except Exception:
                return False
            return ".designer." in name or name.endswith(".designer.cs") or name.endswith(".designer.vb")

        def _is_thirdparty_js(path: Path) -> bool:
            try:
                rel = path.relative_to(temp_dir)
            except Exception:
                rel = path
            s = str(rel).replace("\\", "/").lower()
            name = path.name.lower()
            if "bootstrap" in name or "bootstrap" in s:
                return True
            vendor_tokens = {
                "microsoftajax", "jquery", "react", "react-dom", "reactdom", "angular",
                "vue", "lodash", "underscore", "moment", "backbone", "require", "systemjs", "rxjs",
                "knockout", "signalr", "d3", "chart", "chartjs", "select2", "datatables",
                "fullcalendar", "handsontable", "toastr", "popper", "modernizr", "polyfill",
                "core-js", "babel-polyfill", "vue.runtime", "migrate", "zepto"
            }
            vendor_folders = ("/lib/", "/vendor/", "/scripts/vendor/", "/scripts/lib/", "/bower_components/", "/dist/", "/cdn/")
            if name.endswith(".min.js") or name.endswith(".min.css") or name.endswith(".map"):
                return True
            simple_names = {
                "microsoftajax.js", "microsoftajax.debug.js", "microsoftajax.min.js", "microsoft-ajax.js",
                "sys.js"
            }
            if name in simple_names:
                return True
            for tok in vendor_tokens:
                if tok in name:
                    return True
            for vf in vendor_folders:
                if vf in s:
                    return True
            return False

        files_to_analyze = [
            p for p in all_paths
            if p.is_file()
               and p.suffix.lower() in desired_suffixes
               and not _is_in_irrelevant_dir(p)
               and not _is_designer_file(p)
               and not _is_thirdparty_js(p)
        ]
        files_to_analyze.sort(key=lambda p: str(p.relative_to(temp_dir)).lower())

        _update_job(job_id, progress=30, step="collecting_files", filesDiscovered=len(files_to_analyze)) if job_id else None

        if not files_to_analyze:
            result = {
                "status": "ok",
                "message": "No supported source or markup files found in archive.",
                "filesDiscovered": 0,
                "filesAnalyzed": 0,
                "foldersVisited": len(dirs),
                "results": []
            }
            _update_job(job_id, progress=100, step="done", result=result) if job_id else None
            return result

        rel_paths = [str(p.relative_to(temp_dir)) for p in files_to_analyze]

        seen = set()
        unique_rel_paths = []
        duplicates = []
        for rp in rel_paths:
            norm = rp.replace("\\", "/").lower()
            if norm in seen:
                duplicates.append(rp)
            else:
                seen.add(norm)
                unique_rel_paths.append(rp)

        if duplicates:
            print(f"[Debug] Detected duplicate relative paths (ignored): {duplicates}")

        _update_job(job_id, progress=40, step="running_analyzer", files=len(rel_paths)) if job_id else None

        # --- Monitor Process (Updated to NOT guess Expected until explicitly told) ---
        monitor_thread = None
        stop_monitor = None
        if job_id:
            stop_monitor = threading.Event()
            def _monitor():
                analysis_base = os.path.join(BASE_DIR, "analysis_output")
                analysis_folders = ("Final_Documentation_Chapters", "Final_Utility_Chapters", "Final_SQL_Docs")

                while not stop_monitor.is_set():
                    try:
                        # Only count generated chapters here (MD files)
                        def _count_md_any(folder_root, af):
                            try:
                                a = os.path.join(folder_root, af)
                                if os.path.isdir(a):
                                    cnt = 0
                                    for fname in os.listdir(a):
                                        if fname.endswith(".md"):
                                            cnt += 1
                                    return cnt
                            except Exception:
                                pass
                            return 0

                        observed_generated = 0
                        for af in analysis_folders:
                            observed_generated += _count_md_any(analysis_base, af)

                        # We do NOT set expected_chapters here anymore. 
                        # We only update chapters_generated.
                        # The main thread will set expected_chapters once splitters finish.
                        
                        _update_job(job_id, chapters_generated=observed_generated)

                        # Update progress % based on the main thread's authoritative expected count
                        current_status = JOB_STATUS.get(job_id, {})
                        auth_expected = current_status.get("expected_chapters", 0)
                        
                        if auth_expected > 0:
                            prog = int((observed_generated / auth_expected) * 100)
                            # Cap at 99 until truly done
                            prog = min(99, max(55, prog)) 
                            _update_job(job_id, progress=prog)
                            
                    except Exception:
                        pass
                    stop_monitor.wait(1.0)

            monitor_thread = threading.Thread(target=_monitor, daemon=True)
            monitor_thread.start()

        analysis_result = None
        cwd_before = os.getcwd()
        try:
            os.chdir(temp_dir)

            env_base = os.environ.copy()
            env_base["ANALYZER_TEMP_DIR"] = temp_dir
            if job_id:
                env_base["ANALYZER_JOB_ID"] = job_id

            # STEP 1: Static Analysis
            _update_job(job_id, progress=42, step="running_static_analyzer") if job_id else None
            print("[Pipeline] STEP 1: Running static analyzer (Roslyn)")
            try:
                analysis_result = run_analyzer(*unique_rel_paths, job_id=job_id)
                print("[Pipeline] STEP 1 COMPLETE: Static analysis finished")
            except Exception as e:
                msg = f"Static analyzer failed: {str(e)}"
                print(f"[PipelineError] {msg}")
                if job_id:
                    _update_job(job_id, progress=100, step="error", error=msg)
                raise

            if isinstance(analysis_result, dict):
                runner_stdout = analysis_result.get("runner_stdout")
                runner_stderr = analysis_result.get("runner_stderr")
                if runner_stdout and job_id:
                    _update_job(job_id, analyzer_stdout=runner_stdout[:8000])
                if runner_stderr and job_id:
                    _update_job(job_id, analyzer_stderr=runner_stderr[:8000])

            # STEP 1.5: Diagrams
            print("[Pipeline] STEP 1.5: Generating diagrams from static analysis")
            try:
                if job_id:
                    _update_job(job_id, progress=45, step="generating_diagrams")
    
                diagrams_script = os.path.join(BASE_DIR, "services", "analyzer", "diagram_generator.py")
                if os.path.isfile(diagrams_script):
                    proc = subprocess.run(
                        [sys.executable, diagrams_script],
                        cwd=temp_dir,
                        env=env_base,
                        capture_output=True,
                        text=True,
                        timeout=60,
                        encoding='utf-8', errors='replace' # Force UTF-8
                    )
                    if job_id:
                        dout = (proc.stdout or "").strip()
                        derr = (proc.stderr or "").strip()
                        _update_job(job_id, diagram_stdout=dout[:2000], diagram_stderr=derr[:2000])
            except Exception as e:
                print(f"[Pipeline] Diagram generation error: {e}, but continuing")

            # STEP 2: Run splitters
            print("[Pipeline] STEP 2: Running splitters")
            splitters = [
                ("ai_splitter", os.path.join(BASE_DIR, "services", "analyzer", "ai_analysis", "ai_splitter.py")),
                ("sql_splitter", os.path.join(BASE_DIR, "services", "analyzer", "sql_analysis", "sql_splitter.py")),
            ]
            step_progress = 50
            for name, script in splitters:
                if not os.path.isfile(script):
                    continue
                try:
                    if job_id:
                        _update_job(job_id, progress=step_progress, step=f"running_{name}")
                    print(f"[Pipeline] Running {name}")
                    proc = subprocess.run(
                        [sys.executable, script],
                        cwd=temp_dir,
                        env=env_base,
                        capture_output=True,
                        text=True,
                        #timeout=300,
                        encoding='utf-8', errors='replace' # Force UTF-8
                    )
                    if job_id:
                        out = (proc.stdout or "").strip()
                        err = (proc.stderr or "").strip()
                        _update_job(job_id, **{f"{name}_stdout": out[:4000], f"{name}_stderr": err[:4000]})
                except Exception as e:
                    print(f"[Pipeline] {name} error: {e}, but continuing")
                step_progress += 6
            print("[Pipeline] STEP 2 COMPLETE: Splitters finished")

            # --- NEW: CALCULATE EXPECTED CHAPTERS HERE (POST-SPLITTER) ---
            # We now know exactly how many prompt files exist.
            if job_id:
                try:
                    _pb = os.path.join(BASE_DIR, "prompts_output")
                    _pf = ("Page_Documentation_Prompts", "Utility_Documentation_Prompts", "SQL_Documentation_Prompts")
                    total_prompts = 0
                    for fldr in _pf:
                        fp = os.path.join(_pb, fldr)
                        if os.path.exists(fp):
                            # Count strictly valid prompt text files
                            total_prompts += len([n for n in os.listdir(fp) if n.lower().endswith('.txt')])
                    
                    print(f"[Pipeline] Splitters done. Authoritative Expected Chapters = {total_prompts}")
                    # Update status so frontend and monitor see the final count
                    _update_job(job_id, expected_chapters=total_prompts)
                except Exception as e:
                    print(f"[Pipeline] Error counting prompts: {e}")
            # -------------------------------------------------------------

            # STEP 3: Run analysis scripts
            print("[Pipeline] STEP 3: Running analysis scripts")
            analyses = [
                ("ai_analysis", os.path.join(BASE_DIR, "services", "analyzer", "ai_analysis", "ai_analysis.py")),
                ("sql_analysis", os.path.join(BASE_DIR, "services", "analyzer", "sql_analysis", "sql_analysis.py")),
            ]
            for name, script in analyses:
                if not os.path.isfile(script):
                    continue
                try:
                    if job_id:
                        _update_job(job_id, progress=step_progress, step=f"running_{name}")
                    print(f"[Pipeline] Running {name}")
                    proc = subprocess.run(
                        [sys.executable, script],
                        cwd=temp_dir,
                        env=env_base,
                        capture_output=True,
                        text=True,
                        #timeout=300,
                        encoding='utf-8', errors='replace' # Force UTF-8!
                    )
                    if job_id:
                        out = (proc.stdout or "").strip()
                        err = (proc.stderr or "").strip()
                        _update_job(job_id, **{f"{name}_stdout": out[:4000], f"{name}_stderr": err[:4000]})
                except Exception as e:
                    print(f"[Pipeline] {name} error: {e}, but continuing")
                step_progress += 6
            print("[Pipeline] STEP 3 COMPLETE: Analysis scripts finished")

            # STEP 4: Run compiler
            print("[Pipeline] STEP 4: Running compiler")
            compile_py = os.path.join(BASE_DIR, "compile.py")
            if os.path.isfile(compile_py):
                try:
                    if job_id:
                        _update_job(job_id, progress=step_progress, step="running_compiler")
                    print(f"[Pipeline] Running compiler")
                    proc = subprocess.run(
                        [sys.executable, compile_py],
                        cwd=BASE_DIR,
                        env=env_base,
                        capture_output=True,
                        text=True,
                        timeout=120,
                        encoding='utf-8', errors='replace' # Force UTF-8!
                    )
                    if job_id:
                        cout = (proc.stdout or "").strip()
                        cerr = (proc.stderr or "").strip()
                        _update_job(job_id, compiler_stdout=cout[:4000], compiler_stderr=cerr[:4000])
                except Exception as e:
                    print(f"[Pipeline] Compiler error: {e}, but continuing")

            print("[Pipeline] ALL STEPS COMPLETE")

        finally:
            try:
                os.chdir(cwd_before)
            except Exception:
                pass
            if stop_monitor:
                try:
                    stop_monitor.set()
                except Exception:
                    pass
            if monitor_thread:
                try:
                    monitor_thread.join(timeout=2.0)
                except Exception:
                    pass

        # --- Count final documentation chapters and totals ---
        try:
            analysis_folders = ("Final_Documentation_Chapters", "Final_Utility_Chapters", "Final_SQL_Docs")
            analysis_base = os.path.join(BASE_DIR, "analysis_output")
            
            # Simple final count
            def _cnt(fld): 
                p = os.path.join(analysis_base, fld)
                return len([f for f in os.listdir(p) if f.endswith(".md")]) if os.path.exists(p) else 0

            web_count = _cnt("Final_Documentation_Chapters")
            util_count = _cnt("Final_Utility_Chapters")
            sql_count = _cnt("Final_SQL_Docs")
            
            totals_payload = {"classes": web_count, "methods": sql_count, "others": util_count}
            if isinstance(analysis_result, dict):
                analysis_result.setdefault("totals", {}).update(totals_payload)
            elif isinstance(analysis_result, list):
                analysis_result = {"analysis_list": analysis_result, "totals": totals_payload}

            computed_totals = {"webChapters": web_count, "sqlChapters": sql_count, "utilityChapters": util_count}
            total_chapters = web_count + util_count + sql_count

            if job_id:
                # Force final sync
                expected_now = JOB_STATUS.get(job_id, {}).get("expected_chapters", total_chapters)
                _update_job(
                    job_id,
                    webChapters=web_count,
                    sqlChapters=sql_count,
                    utilityChapters=util_count,
                    expected_chapters=max(expected_now, total_chapters),
                    chapters_generated=total_chapters
                )
        except Exception:
            computed_totals = {"webChapters": 0, "sqlChapters": 0, "utilityChapters": 0}

        _update_job(job_id, progress=75, step="analyzer_finished", analysis=analysis_result) if job_id else None

        results = []
        for p in files_to_analyze:
            rel = str(p.relative_to(temp_dir))
            results.append({
                "file": rel,
                "result": "analyzed"
            })

        discovered_sample = [str(p.relative_to(temp_dir)) for p in files_to_analyze[:10]]
        folders_with_cs = sorted({str(p.parent.relative_to(temp_dir)) for p in files_to_analyze})[:10]

        final = {
            "status": "ok",
            "message": "Analysis complete",
            "filesDiscovered": len(rel_paths),
            "filesAnalyzed": len(results),
            "foldersVisited": len(dirs),
            "foldersWithCsSample": folders_with_cs,
            "discoveredSample": discovered_sample,
            "results": results,
            "analysisOutput": analysis_result,
            "computedTotals": computed_totals
        }

        _update_job(job_id, progress=95, step="postprocessing", result=final) if job_id else None

        return final
    except Exception as ex:
        if job_id and JOB_STATUS.get(job_id, {}).get("canceled"):
            _update_job(job_id, progress=100, step="canceled", error=str(ex))
            return {"status": "canceled", "message": "Analysis canceled", "results": []}
        _update_job(job_id, progress=100, step="error", error=str(ex)) if job_id else None
        return {"status": "error", "message": f"Analysis failed: {str(ex)}", "results": []}
    finally:
        try:
            os.remove(zip_path)
        except OSError:
            pass
        shutil.rmtree(temp_dir, ignore_errors=True)
        if job_id:
            final_step = JOB_STATUS.get(job_id, {}).get("step", "")
            if final_step not in ("canceled", "error", "done"):
                _update_job(job_id, progress=100, step="done")


@app.route("/analyze", methods=["POST"])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if not file.filename.lower().endswith(".zip"):
        return jsonify({"error": "Only .zip files are supported"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    model_choice = request.form.get("model") or request.args.get("model")
    if model_choice:
        os.environ["ANALYSIS_MODEL"] = model_choice
        print(f"[Debug] ANALYSIS_MODEL set to: {model_choice}")

    try:
        size_mb = round(os.path.getsize(filepath) / 1024 / 1024, 2)
    except OSError:
        size_mb = None

    start = time.perf_counter()
    try:
        result = analyze_zip(filepath)
        # Propagate model choice into the response so frontend can display it.
        if model_choice:
            # top-level key for simple access
            result["analysisModel"] = model_choice
            # legacy/backward-compatible keys the frontend might look for
            result["model"] = result.get("model", model_choice)
            analysis_dict = result.setdefault("analysis", {})
            analysis_dict.setdefault("model", model_choice)

        # attach documentation size (if complete documentation was generated)
        try:
            final_md = os.path.join(BASE_DIR, "final_output", "Complete_Documentation.md")
            if os.path.exists(final_md):
                sz = os.path.getsize(final_md)
                # expose both raw bytes and MB for convenience
                result["documentationSizeBytes"] = int(sz)
                result["documentationSizeMB"] = round(sz / 1024 / 1024, 2)
                # also put the values inside `analysis` so the frontend finds them
                try:
                    analysis_dict = result.setdefault("analysis", {})
                    analysis_dict.setdefault("documentationSizeBytes", int(sz))
                    analysis_dict.setdefault("documentationSizeMB", round(sz / 1024 / 1024, 2))
                except Exception:
                    pass
        except Exception:
            pass

        # --- SHIM: make analyzer output available under predictable keys for frontend ---
        # Many frontend components expect the analyzer JSON at `analysis` or `results`.
        # If analyze_zip returned `analysisOutput`, expose it under both `analysis` and `results`.
        if result is not None and "analysisOutput" in result and result["analysisOutput"] is not None:
            result["analysis"] = result.get("analysisOutput")
            # If analyzer produced a list of per-file objects, also expose as `results`
            if isinstance(result["analysisOutput"], list):
                result["results"] = result["analysisOutput"]

        # also expose the computed totals at top-level for easy consumption
        if result is not None and "computedTotals" in result:
            # backward-compatible mapping for existing frontend expectations:
            # attach as analysis.totals.classes/methods/others and also top-level clearer keys
            ct = result["computedTotals"]
            # ensure analysis dict exists
            analysis_dict = result.setdefault("analysis", {})
            totals = analysis_dict.setdefault("totals", {})
            totals.setdefault("classes", ct.get("webChapters", 0))
            totals.setdefault("methods", ct.get("sqlChapters", 0))
            totals.setdefault("others", ct.get("utilityChapters", 0))

            # expose clearer keys too
            result.setdefault("totals", {}).update(ct)

            # --- Ensure legacy frontend shape: put totals inside analysis.results[] so accumulateTotals finds it ---
            try:
                totals_payload = {
                    "classes": ct.get("webChapters", 0),
                    "methods": ct.get("sqlChapters", 0),
                    "others": ct.get("utilityChapters", 0)
                }

                totals_entry = {"result": {"totals": totals_payload}}
                existing_results = analysis_dict.get("results")
                if not isinstance(existing_results, list) or len(existing_results) == 0:
                    analysis_dict["results"] = [totals_entry]
                else:
                    first = existing_results[0]
                    if isinstance(first, dict):
                        first.setdefault("result", {}).setdefault("totals", totals_payload)
                    else:
                        analysis_dict["results"][0] = totals_entry
            except Exception:
                # non-fatal — we still have analysis_result["totals"] and computedTotals for other consumers
                pass

        duration_ms = int((time.perf_counter() - start) * 1000)
        result.update({
            "zipFilename": file.filename,
            "sizeMB": size_mb,
            "processingMs": duration_ms
        })
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/download/complete_documentation", methods=["GET"])
def download_complete_documentation():
    final_dir = os.path.join(BASE_DIR, "final_output")
    filename = "Complete_Documentation.md"
    file_full = os.path.join(final_dir, filename)
    if os.path.exists(file_full):
        return send_from_directory(final_dir, filename, as_attachment=True, mimetype="text/markdown")
    return jsonify({"error": "Complete_Documentation.md not found"}), 404

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_spa(path):
    file_path = os.path.join(app.static_folder, path)
    if path and os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/analyze_async", methods=["POST"])
def analyze_async():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if not file.filename.lower().endswith(".zip"):
        return jsonify({"error": "Only .zip files are supported"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    model_choice = request.form.get("model") or request.args.get("model")
    if model_choice:
        os.environ["ANALYSIS_MODEL"] = model_choice
        print(f"[Debug] ANALYSIS_MODEL set to: {model_choice}")

    job_id = str(uuid.uuid4())
    # Ensure numeric keys exist immediately so frontend reads stable values
    JOB_STATUS[job_id] = {"progress": 0, "step": "queued", "created": time.time(), "expected_chapters": 0, "chapters_generated": 0}

    def _run():
        try:
            # Export job id so splitter/analysis scripts can write a per-job manifest
            os.environ["ANALYZER_JOB_ID"] = job_id
            _update_job(job_id, progress=2, step="saved")

            # Capture filename and size BEFORE analyze_zip removes the uploaded file
            try:
                size_mb = round(os.path.getsize(filepath) / 1024 / 1024, 2)
            except OSError:
                size_mb = None
            filename = os.path.basename(filepath)

            start = time.perf_counter()
            res = analyze_zip(filepath, job_id=job_id)
            duration_ms = int((time.perf_counter() - start) * 1000)

            # Ensure result is a dict and expose the same metadata as the synchronous endpoint
            if res is None:
                res = {}
            if isinstance(res, dict):
                # expose analyzer output under predictable keys (same shim as sync analyze)
                if "analysisOutput" in res and res["analysisOutput"] is not None:
                    res["analysis"] = res.get("analysisOutput")
                    if isinstance(res["analysisOutput"], list):
                        res["results"] = res["analysisOutput"]
                # Propagate model choice into async result payload as well
                if model_choice:
                    res["analysisModel"] = model_choice
                    res["model"] = res.get("model", model_choice)
                    res.setdefault("analysis", {}).setdefault("model", model_choice)
                # attach documentation size for async results too
                try:
                    final_md_async = os.path.join(BASE_DIR, "final_output", "Complete_Documentation.md")
                    if os.path.exists(final_md_async):
                        sza = os.path.getsize(final_md_async)
                        res["documentationSizeBytes"] = int(sza)
                        res["documentationSizeMB"] = round(sza / 1024 / 1024, 2)
                        # also include inside nested `analysis` for frontend compatibility
                        try:
                            res.setdefault("analysis", {}).setdefault("documentationSizeBytes", int(sza))
                            res.setdefault("analysis", {}).setdefault("documentationSizeMB", round(sza / 1024 / 1024, 2))
                        except Exception:
                            pass
                except Exception:
                    pass
                res.update({
                    "zipFilename": filename,
                    "sizeMB": size_mb,
                    "processingMs": duration_ms
                })

            _update_job(job_id, progress=100, step="done", result=res)
        except Exception as e:
            _update_job(job_id, progress=100, step="error", error=str(e))

    thread = threading.Thread(target=_run, daemon=True)
    thread.start()

    return jsonify({"jobId": job_id}), 202

@app.route("/status/<job_id>", methods=["GET"])
def job_status(job_id):
    st = JOB_STATUS.get(job_id)
    if not st:
        return jsonify({"error": "job not found"}), 404
    # Ensure the response always includes numeric chapter counters
    st.setdefault("expected_chapters", 0)
    st.setdefault("chapters_generated", 0)
    st.setdefault("progress", st.get("progress", 0))
    return jsonify(st)

@app.route("/cancel/<job_id>", methods=["POST"])
def cancel_job(job_id):
    st = JOB_STATUS.get(job_id)
    if not st:
        return jsonify({"error": "job not found"}), 404
    # Mark as cancellation requested so polling clients see it immediately
    st["step"] = "cancel_requested"
    st["canceled"] = True
    st.setdefault("progress", 0)
    try:
        canceled = analyzer_runner.cancel_analyzer(job_id)
        if canceled:
            st["step"] = "canceled"
            st["progress"] = 0
            return jsonify({"status": "ok", "message": "cancel requested"}), 200
        else:
            # No running process found, but job marked canceled
            return jsonify({"status": "ok", "message": "cancel requested (no running process found)"}), 200
    except Exception as e:
        return jsonify({"error": "cancel failed", "details": str(e)}), 500

# --- Prevent system sleep (Windows only) ---
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_AWAYMODE_REQUIRED = 0x00000040  # Vista+

def _prevent_sleep() -> None:
    """Request the OS keep the system awake (Windows). No-op on other OSes."""
    try:
        if platform.system() == "Windows":
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_AWAYMODE_REQUIRED)
            print("[KeepAwake] SetThreadExecutionState: preventing sleep")
    except Exception as e:
        print(f"[KeepAwake] unable to prevent sleep: {e}")

def _allow_sleep() -> None:
    """Clear previous keep-awake request (Windows). No-op on other OSes."""
    try:
        if platform.system() == "Windows":
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
            print("[KeepAwake] SetThreadExecutionState: allowing sleep")
    except Exception as e:
        print(f"[KeepAwake] unable to restore sleep policy: {e}")

# Add this line before the if __name__ == "__main__": block
register_diagram_routes(app)

if __name__ == "__main__":
    # enable threaded so status polling works reliably during background jobs
    app.run(debug=True, threaded=True)
