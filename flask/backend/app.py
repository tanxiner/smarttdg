from flask import Flask, request, jsonify, send_from_directory, send_file
import json
import os
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
import re

import services.analyzer.analyzer_runner as analyzer_runner
run_analyzer = analyzer_runner.analyze_code

import services.analyzer.comment_stripper as comment_stripper

from services.diagram_routes import register_diagram_routes
import convert_doc
markdown_to_word = convert_doc.markdown_to_word
word_to_pdf = convert_doc.word_to_pdf

BASE_DIR = os.path.dirname(__file__)
app = Flask(
    __name__,
    static_folder=os.path.abspath(os.path.join(BASE_DIR, "..", "frontend", "build")),
    static_url_path="/"
)
print("BASE_DIR =", BASE_DIR)
print("STATIC_FOLDER =", app.static_folder)
print("INDEX_EXISTS =", os.path.exists(os.path.join(app.static_folder, "index.html")))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

JOB_STATUS: Dict[str, Dict[str, Any]] = {}
JOB_THREADS: Dict[str, threading.Thread] = {}
JOB_LOCK = threading.Lock()

TERMINAL_STEPS = {"done", "error", "canceled"}


def _update_job(job_id: str | None, **kwargs):
    if not job_id:
        return
    with JOB_LOCK:
        st = JOB_STATUS.setdefault(job_id, {})
        st.update(kwargs)


def _get_job(job_id: str | None) -> Dict[str, Any]:
    if not job_id:
        return {}
    with JOB_LOCK:
        return dict(JOB_STATUS.get(job_id, {}))


def _is_job_canceled(job_id: str | None) -> bool:
    if not job_id:
        return False
    st = _get_job(job_id)
    return bool(st.get("canceled")) or st.get("step") in ("cancel_requested", "canceled")


def _ensure_not_canceled(job_id: str | None) -> None:
    if _is_job_canceled(job_id):
        raise RuntimeError("canceled")


def _find_active_job_id() -> str | None:
    with JOB_LOCK:
        for jid, thread in list(JOB_THREADS.items()):
            if thread and thread.is_alive():
                return jid
    return None


def _has_active_job() -> bool:
    return _find_active_job_id() is not None


def _load_pipeline_steps() -> list:
    pipeline_json = os.path.join(BASE_DIR, "pipeline.json")
    try:
        with open(pipeline_json, "r", encoding="utf-8") as f:
            return json.load(f).get("steps", [])
    except FileNotFoundError:
        print(f"[Pipeline] WARNING: pipeline.json not found at {pipeline_json}. No downstream scripts will run.")
        return []
    except json.JSONDecodeError as e:
        print(f"[Pipeline] WARNING: pipeline.json is malformed ({pipeline_json}): {e}. No downstream scripts will run.")
        return []
    except Exception as e:
        print(f"[Pipeline] WARNING: Could not load pipeline.json ({pipeline_json}): {e}. No downstream scripts will run.")
        return []


def _run_step_subprocess(
    *,
    job_id: str | None,
    env_base: dict,
    script_path: str,
    cwd: str,
    step_name: str,
    timeout: int | None = None,
    stdout_key: str | None = None,
    stderr_key: str | None = None,
) -> subprocess.CompletedProcess:
    _ensure_not_canceled(job_id)

    stdout_tmp = tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8", errors="replace", delete=False)
    stderr_tmp = tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8", errors="replace", delete=False)

    try:
        proc = subprocess.Popen(
            [sys.executable, script_path],
            cwd=cwd,
            env=env_base,
            stdout=stdout_tmp,
            stderr=stderr_tmp,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        start_time = time.time()

        while True:
            if _is_job_canceled(job_id):
                try:
                    proc.terminate()
                    proc.wait(timeout=5)
                except Exception:
                    try:
                        proc.kill()
                    except Exception:
                        pass
                raise RuntimeError("canceled")

            if timeout is not None and (time.time() - start_time) > timeout:
                try:
                    proc.terminate()
                    proc.wait(timeout=5)
                except Exception:
                    try:
                        proc.kill()
                    except Exception:
                        pass
                raise RuntimeError(f"{step_name} failed with timeout after {timeout} seconds")

            rc = proc.poll()
            if rc is not None:
                break

            time.sleep(0.5)

        stdout_tmp.flush()
        stderr_tmp.flush()
        stdout_tmp.seek(0)
        stderr_tmp.seek(0)

        stdout = stdout_tmp.read()
        stderr = stderr_tmp.read()

        if job_id:
            out = (stdout or "").strip()
            err = (stderr or "").strip()
            payload = {}
            if stdout_key:
                payload[stdout_key] = out[:4000]
            if stderr_key:
                payload[stderr_key] = err[:4000]
            if payload:
                _update_job(job_id, **payload)

        if proc.returncode != 0:
            if _is_job_canceled(job_id):
                raise RuntimeError("canceled")
            raise RuntimeError(f"{step_name} failed with exit code {proc.returncode}")

        return subprocess.CompletedProcess(
            args=[sys.executable, script_path],
            returncode=proc.returncode,
            stdout=stdout,
            stderr=stderr,
        )

    finally:
        try:
            if 'proc' in locals() and proc.poll() is None:
                proc.kill()
        except Exception:
            pass

        try:
            stdout_tmp.close()
        except Exception:
            pass
        try:
            stderr_tmp.close()
        except Exception:
            pass

        try:
            os.remove(stdout_tmp.name)
        except Exception:
            pass
        try:
            os.remove(stderr_tmp.name)
        except Exception:
            pass


def analyze_zip(zip_path: str, job_id: str | None = None, model_choice: str | None = None) -> dict:
    temp_dir = None
    monitor_thread = None
    stop_monitor = None

    _ensure_not_canceled(job_id)
    _update_job(job_id, progress=5, step="starting") if job_id else None

    _ensure_not_canceled(job_id)

    static_analysis_base = os.path.join(BASE_DIR, "static_analysis_output")
    if os.path.exists(static_analysis_base):
        try:
            shutil.rmtree(static_analysis_base)
        except Exception:
            pass
    os.makedirs(static_analysis_base, exist_ok=True)

    prompts_base = os.path.join(BASE_DIR, "prompts_output")
    analysis_base = os.path.join(BASE_DIR, "analysis_output")
    output_base = os.path.join(BASE_DIR, "final_output")
    static_analysis_base = os.path.join(BASE_DIR, "static_analysis_output")

    dirs_to_clean = [
        os.path.join(prompts_base, "Page_Documentation_Prompts"),
        os.path.join(prompts_base, "Utility_Documentation_Prompts"),
        os.path.join(prompts_base, "Utility_SQL_Documentation_Prompts"),
        os.path.join(prompts_base, "SQL_Documentation_Prompts"),
        os.path.join(prompts_base, "API_Documentation_Prompts"),
        os.path.join(prompts_base, "HTML_Documentation_Prompts"),
        os.path.join(prompts_base, "JS_Documentation_Prompts"),
        os.path.join(analysis_base, "Final_Documentation_Chapters"),
        os.path.join(analysis_base, "Final_Utility_Chapters"),
        os.path.join(analysis_base, "Final_Utility_SQL_Chapters"),
        os.path.join(analysis_base, "Final_SQL_Docs"),
        os.path.join(analysis_base, "Final_API_Docs"),
        os.path.join(analysis_base, "Final_HTML_Docs"),
        os.path.join(analysis_base, "Final_JS_Docs"),
        os.path.join(analysis_base, "Diagrams"),
        output_base,
        static_analysis_base
    ]

    for d in dirs_to_clean:
        if os.path.exists(d):
            try:
                shutil.rmtree(d)
            except Exception:
                pass
        try:
            os.makedirs(d, exist_ok=True)
        except Exception:
            pass

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

    sys_tmp = Path(tempfile.gettempdir())
    short_base = os.path.join(sys_tmp.drive + os.sep, "sdtg_tmp")
    os.makedirs(short_base, exist_ok=True)

    temp_dir = tempfile.mkdtemp(prefix="smarttdg_", dir=short_base)

    try:
        _update_job(job_id, progress=5, step="extracting") if job_id else None

        with zipfile.ZipFile(zip_path, 'r') as z:
            print("Files in ZIP:", [f.filename for f in z.infolist()])
            z.extractall(temp_dir)
            print("Extracted files:", list(Path(temp_dir).rglob("*")))

        _ensure_not_canceled(job_id)

        env_base = os.environ.copy()
        env_base["ANALYZER_TEMP_DIR"] = temp_dir
        if job_id:
            env_base["ANALYZER_JOB_ID"] = job_id
        if model_choice:
            env_base["ANALYSIS_MODEL"] = model_choice

        try:
            sql_files = [str(p) for p in Path(temp_dir).rglob("*.sql")]
            if sql_files:
                combined_sql_paths = ";".join(sql_files)
                env_base["ANALYZER_SQL_FILE"] = combined_sql_paths
                if job_id:
                    _update_job(job_id, analyzer_sql_file=combined_sql_paths)
                print(f"[Debug] ANALYZER_SQL_FILE set to: {combined_sql_paths} ({len(sql_files)} files)")
            else:
                env_base.pop("ANALYZER_SQL_FILE", None)
        except Exception:
            pass

        all_paths = list(Path(temp_dir).rglob("*"))
        dirs = [p for p in all_paths if p.is_dir()]

        desired_suffixes = {
            ".cs", ".vb",
            ".aspx", ".ascx", ".master",
            ".js", ".jsx",
            ".cshtml", ".cshtml.cs", ".razor", 
            ".html", ".htm",
            ".sql"
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
                "microsoftajax.js", "microsoftajax.debug.js", "microsoftajax.min.js",
                "microsoft-ajax.js", "sys.js"
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

        _update_job(job_id, progress=10, step="collecting_files", filesDiscovered=len(files_to_analyze)) if job_id else None

        if not files_to_analyze:
            result = {
                "status": "ok",
                "message": "No supported source or markup files found in archive.",
                "filesDiscovered": 0,
                "filesAnalyzed": 0,
                "filesGenerated": 0,
                "foldersVisited": len(dirs),
                "results": []
            }
            _update_job(job_id, progress=95, step="analyzer_finished", result=result) if job_id else None
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

        _update_job(job_id, progress=15, step="running_analyzer", files=len(rel_paths)) if job_id else None

        if job_id:
            stop_monitor = threading.Event()

            def _monitor():
                local_analysis_base = os.path.join(BASE_DIR, "analysis_output")
                analysis_folders = (
                    "Final_Documentation_Chapters",
                    "Final_Utility_Chapters",
                    "Final_Utility_SQL_Chapters",
                    "Final_SQL_Docs",
                    "Final_API_Docs",
                    "Final_HTML_Docs",
                    "Final_JS_Docs"
                )

                while not stop_monitor.is_set():
                    try:
                        if _is_job_canceled(job_id):
                            return

                        def _count_md_any(folder_root, af):
                            try:
                                a = os.path.join(folder_root, af)
                                if os.path.isdir(a):
                                    return sum(1 for fname in os.listdir(a) if fname.endswith(".md"))
                            except Exception:
                                pass
                            return 0

                        observed_generated = sum(_count_md_any(local_analysis_base, af) for af in analysis_folders)
                        _update_job(job_id, chapters_generated=observed_generated)

                        current_status = _get_job(job_id)
                        auth_expected = current_status.get("expected_chapters", 0)

                        if auth_expected > 0:
                            prog = int((observed_generated / auth_expected) * 100)
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

            _ensure_not_canceled(job_id)

            # ------------------------------------------------------------------
            # STEP 0: Strip comments → write stripped copies to stripped_source/
            # ------------------------------------------------------------------
            print("[Pipeline] STEP 0: Stripping comments from source files")
            stripped_dir = os.path.join(temp_dir, "stripped_source")
            os.makedirs(stripped_dir, exist_ok=True)

            stripped_rel_paths = []
            strip_files_processed = 0
            strip_lines_removed = 0

            for rp in unique_rel_paths:
                src_path = os.path.join(temp_dir, rp)
                dst_path = os.path.join(stripped_dir, rp)
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)

                ext = os.path.splitext(rp)[1].lower()
                lang = comment_stripper.EXT_TO_LANG.get(ext)

                if lang:
                    try:
                        cleaned = comment_stripper.strip_comments_from_file(src_path)
                        with open(dst_path, "w", encoding="utf-8") as _fh:
                            _fh.write(cleaned)
                        try:
                            with open(src_path, encoding="utf-8", errors="replace") as _cf:
                                orig_lines = sum(1 for _ in _cf)
                        except Exception:
                            orig_lines = 0
                        strip_lines_removed += max(0, orig_lines - len(cleaned.splitlines()))
                        strip_files_processed += 1
                    except Exception as _exc:
                        print(f"[Pipeline] Warning: comment stripping failed for {rp}: {_exc}. Using original.")
                        shutil.copy2(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)

                stripped_rel_paths.append(os.path.join("stripped_source", rp))

            print(
                f"[Pipeline] STEP 0 COMPLETE: Stripped {strip_files_processed} files, "
                f"~{strip_lines_removed} comment lines removed"
            )
            # Use stripped copies for all downstream steps (analyzer + pipeline)
            unique_rel_paths = [p.replace("\\", "/") for p in stripped_rel_paths]

            # ------------------------------------------------------------------
            _update_job(job_id, progress=20, step="running_static_analyzer") if job_id else None
            print("[Pipeline] STEP 1: Running static analyzer (Roslyn)")

            def _on_static_progress(current, total):
                if job_id and total > 0:
                    safe_current = min(current, total)
                    ratio = safe_current / total
                    prog = 20 + int(ratio * 8)
                    _update_job(job_id, progress=prog, step=f"analyzing_file_{safe_current}_of_{total}")

            try:
                analysis_result = run_analyzer(
                    *unique_rel_paths,
                    job_id=job_id,
                    progress_callback=_on_static_progress
                )
                _ensure_not_canceled(job_id)
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

            pipeline_steps = _load_pipeline_steps()
            step_progress = 30

            #_diagram_steps = [s for s in pipeline_steps if s.get("phase") == "diagram"]
            _splitter_steps = [s for s in pipeline_steps if s.get("phase") == "splitter"]
            _analysis_steps = [s for s in pipeline_steps if s.get("phase") == "analysis"]
            _compile_steps = [s for s in pipeline_steps if s.get("phase") == "compile"]

            #print("[Pipeline] STEP 1.5: Generating diagrams from static analysis")
            if job_id:
                _update_job(job_id, progress=step_progress, step="generating...")

            # for _step in _diagram_steps:
            #     _ensure_not_canceled(job_id)
            #     _name = _step["name"]
            #     _script = os.path.join(BASE_DIR, _step["script"].replace("/", os.sep))
            #     _timeout = _step.get("timeout_seconds") or None
            #     if not os.path.isfile(_script):
            #         print(f"[Pipeline] Script not found, skipping: {_script}")
            #         continue

            #     print(f"[Pipeline] Running {_name}")
            #     _run_step_subprocess(
            #         job_id=job_id,
            #         env_base=env_base,
            #         script_path=_script,
            #         cwd=temp_dir,
            #         step_name=_name,
            #         timeout=_timeout,
            #         stdout_key="diagram_stdout",
            #         stderr_key="diagram_stderr",
            #     )

            step_progress = 32

            print("[Pipeline] STEP 2: Running splitters")
            for _step in _splitter_steps:
                _ensure_not_canceled(job_id)
                _name = _step["name"]
                _script = os.path.join(BASE_DIR, _step["script"].replace("/", os.sep))
                if not os.path.isfile(_script):
                    print(f"[Pipeline] Script not found, skipping: {_script}")
                    step_progress += 6
                    continue

                if job_id:
                    _update_job(job_id, progress=step_progress, step=f"running_{_name}")
                print(f"[Pipeline] Running {_name}")

                _run_step_subprocess(
                    job_id=job_id,
                    env_base=env_base,
                    script_path=_script,
                    cwd=temp_dir,
                    step_name=_name,
                    stdout_key=f"{_name}_stdout",
                    stderr_key=f"{_name}_stderr",
                )
                step_progress += 6

            print("[Pipeline] STEP 2 COMPLETE: Splitters finished")

            if job_id:
                try:
                    _pb = os.path.join(BASE_DIR, "prompts_output")
                    _pf = (
                        "Page_Documentation_Prompts",
                        "Utility_Documentation_Prompts",
                        "SQL_Documentation_Prompts",
                        "API_Documentation_Prompts",
                        "Utility_SQL_Documentation_Prompts",
                        "HTML_Documentation_Prompts",
                        "JS_Documentation_Prompts"
                    )
                    total_prompts = 0
                    for fldr in _pf:
                        fp = os.path.join(_pb, fldr)
                        if os.path.exists(fp):
                            total_prompts += len([n for n in os.listdir(fp) if n.lower().endswith('.txt')])

                    print(f"[Pipeline] Splitters done. Authoritative Expected Chapters = {total_prompts}")
                    _update_job(job_id, expected_chapters=total_prompts)
                except Exception as e:
                    print(f"[Pipeline] Error counting prompts: {e}")

            print("[Pipeline] STEP 3: Running analysis scripts")
            for _step in _analysis_steps:
                _ensure_not_canceled(job_id)
                _name = _step["name"]
                _script = os.path.join(BASE_DIR, _step["script"].replace("/", os.sep))
                if not os.path.isfile(_script):
                    print(f"[Pipeline] Script not found, skipping: {_script}")
                    step_progress += 6
                    continue

                if job_id:
                    _update_job(job_id, progress=step_progress, step=f"running_{_name}")
                print(f"[Pipeline] Running {_name}")

                _run_step_subprocess(
                    job_id=job_id,
                    env_base=env_base,
                    script_path=_script,
                    cwd=temp_dir,
                    step_name=_name,
                    stdout_key=f"{_name}_stdout",
                    stderr_key=f"{_name}_stderr",
                )
                step_progress += 6

            print("[Pipeline] STEP 3 COMPLETE: Analysis scripts finished")

            print("[Pipeline] STEP 4: Running compiler")
            for _step in _compile_steps:
                _ensure_not_canceled(job_id)
                _name = _step["name"]
                _script = os.path.join(BASE_DIR, _step["script"].replace("/", os.sep))
                _timeout = _step.get("timeout_seconds") or None
                if not os.path.isfile(_script):
                    print(f"[Pipeline] Script not found, skipping: {_script}")
                    continue

                if job_id:
                    _update_job(job_id, progress=step_progress, step=f"running_{_name}")
                print(f"[Pipeline] Running {_name}")

                _run_step_subprocess(
                    job_id=job_id,
                    env_base=env_base,
                    script_path=_script,
                    cwd=BASE_DIR,
                    step_name=_name,
                    timeout=_timeout,
                    stdout_key=f"{_name}_stdout",
                    stderr_key=f"{_name}_stderr",
                )

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

        try:
            analysis_folders = (
                "Final_Documentation_Chapters",
                "Final_Utility_Chapters",
                "Final_SQL_Docs",
                "Final_API_Docs",
                "Final_Utility_SQL_Chapters",
                "Final_HTML_Docs",
                "Final_JS_Docs"
            )
            analysis_base = os.path.join(BASE_DIR, "analysis_output")

            def _cnt(fld):
                p = os.path.join(analysis_base, fld)
                try:
                    if not os.path.isdir(p):
                        return 0
                    all_md = [f for f in os.listdir(p) if f.endswith(".md")]
                    non_empty = []
                    empty = []
                    for fname in all_md:
                        fpath = os.path.join(p, fname)
                        try:
                            if os.path.getsize(fpath) > 0:
                                non_empty.append(fname)
                            else:
                                empty.append(fname)
                        except Exception:
                            empty.append(fname)
                    if empty:
                        print(f"[Debug] {fld} contains {len(empty)} empty .md files: {empty[:20]}")
                    return len(non_empty)
                except Exception as e:
                    print(f"[Debug] error counting .md in {p}: {e}")
                    return 0

            web_count = _cnt("Final_Documentation_Chapters")
            util_count = _cnt("Final_Utility_Chapters")
            util_sql_count = _cnt("Final_Utility_SQL_Chapters")
            sql_count = _cnt("Final_SQL_Docs")
            api_count = _cnt("Final_API_Docs")
            html_count = _cnt("Final_HTML_Docs")
            js_count = _cnt("Final_JS_Docs")

            totals_payload = {"classes": (web_count+html_count), "methods": sql_count, "others": (util_count+util_sql_count+js_count), "api": api_count}
            if isinstance(analysis_result, dict):
                analysis_result.setdefault("totals", {}).update(totals_payload)
            elif isinstance(analysis_result, list):
                analysis_result = {"analysis_list": analysis_result, "totals": totals_payload}

            computed_totals = {
                "webChapters": (web_count+html_count),
                "sqlChapters": sql_count,
                "utilityChapters": (util_count+util_sql_count+js_count),
                "apiChapters": api_count
            }
            total_chapters = web_count + util_count + sql_count + api_count + html_count + util_sql_count + js_count

            if job_id:
                expected_now = _get_job(job_id).get("expected_chapters", total_chapters)
                _update_job(
                    job_id,
                    webChapters=(web_count+html_count),
                    sqlChapters=sql_count,
                    utilityChapters=(util_count+util_sql_count+js_count),
                    apiChapters=api_count,
                    expected_chapters=max(expected_now, total_chapters),
                    chapters_generated=total_chapters
                )
        except Exception:
            computed_totals = {
                "webChapters": 0,
                "sqlChapters": 0,
                "utilityChapters": 0,
                "apiChapters": 0
            }
            total_chapters = 0

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
            "filesGenerated": total_chapters,
            "foldersVisited": len(dirs),
            "foldersWithCsSample": folders_with_cs,
            "discoveredSample": discovered_sample,
            "results": results,
            "analysisOutput": analysis_result,
            "computedTotals": computed_totals
        }

        if job_id:
            _update_job(job_id, progress=95, step="analyzer_finished", result=final)

        return final

    except Exception as ex:
        if _is_job_canceled(job_id) or str(ex).lower() == "canceled":
            if job_id:
                _update_job(
                    job_id,
                    progress=100,
                    step="canceled",
                    result={"status": "canceled", "message": "Analysis canceled"}
                )
            return {"status": "canceled", "message": "Analysis canceled", "results": []}

        _update_job(job_id, progress=100, step="error", error=str(ex)) if job_id else None
        return {"status": "error", "message": f"Analysis failed: {str(ex)}", "results": []}

    finally:
        try:
            os.remove(zip_path)
        except OSError:
            pass

        if temp_dir:
            shutil.rmtree(temp_dir, ignore_errors=True)

        if job_id:
            st = _get_job(job_id)
            final_step = st.get("step", "")
            # if final_step not in ("canceled", "cancel_requested", "error", "done"):
            #     if st.get("result") is not None:
            #         _update_job(job_id, progress=100, step="done")


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

    try:
        size_mb = round(os.path.getsize(filepath) / 1024 / 1024, 2)
    except OSError:
        size_mb = None

    start = time.perf_counter()
    try:
        result = analyze_zip(filepath, model_choice=model_choice)

        if result is None:
            result = {"status": "error", "message": "No result returned from analyzer."}
        elif not isinstance(result, dict):
            result = {"status": "ok", "data": result}

        if model_choice:
            result["analysisModel"] = model_choice
            result["model"] = result.get("model", model_choice)
            analysis_dict = result.setdefault("analysis", {})
            analysis_dict.setdefault("model", model_choice)

        try:
            final_md = os.path.join(BASE_DIR, "final_output", "Technical_Documentation.md")
            if os.path.exists(final_md):
                sz = os.path.getsize(final_md)
                result["documentationSizeBytes"] = int(sz)
                result["documentationSizeMB"] = round(sz / 1024 / 1024, 2)

                analysis_dict = result.setdefault("analysis", {})
                analysis_dict.setdefault("documentationSizeBytes", int(sz))
                analysis_dict.setdefault("documentationSizeMB", round(sz / 1024 / 1024, 2))
        except Exception:
            pass

        if result.get("analysisOutput") is not None:
            result["analysis"] = result.get("analysisOutput")
            if isinstance(result["analysisOutput"], list):
                result["results"] = result["analysisOutput"]

        if "computedTotals" in result:
            ct = result["computedTotals"]
            analysis_dict = result.setdefault("analysis", {})
            totals = analysis_dict.setdefault("totals", {})
            totals.setdefault("classes", ct.get("webChapters", 0))
            totals.setdefault("methods", ct.get("sqlChapters", 0))
            totals.setdefault("others", ct.get("utilityChapters", 0))
            totals.setdefault("api", ct.get("apiChapters", 0))

            result.setdefault("totals", {})
            result["totals"].setdefault("webChapters", ct.get("webChapters", 0))
            result["totals"].setdefault("sqlChapters", ct.get("sqlChapters", 0))
            result["totals"].setdefault("utilityChapters", ct.get("utilityChapters", 0))
            result["totals"].setdefault("apiChapters", ct.get("apiChapters", 0))

        duration_ms = int((time.perf_counter() - start) * 1000)
        result["zipFilename"] = os.path.basename(filepath)
        result["sizeMB"] = size_mb
        result["processingMs"] = duration_ms

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "zipFilename": os.path.basename(filepath),
            "sizeMB": size_mb
        }), 500


def _zip_prefix_from_request() -> str:
    try:
        z = request.args.get("zipFilename") or request.args.get("zipfilename") or ""
        if not z:
            return ""
        base = os.path.splitext(os.path.basename(z))[0]
        sanitized = re.sub(r"[^A-Za-z0-9._-]+", "_", base).strip("_")
        if not sanitized:
            return ""
        return sanitized + "_"
    except Exception:
        return ""


@app.route("/download/md_documentation", methods=["GET"])
def download_complete_documentation():
    final_dir = os.path.join(BASE_DIR, "final_output")
    filename = "Technical_Documentation.md"
    md_path = os.path.join(final_dir, filename)

    if not os.path.exists(md_path):
        return jsonify({
            "error": "Documentation not generated",
            "reason": "No documentation chapters were produced.",
            "suggestion": "The uploaded project may not contain supported files."
        }), 404

    prefix = _zip_prefix_from_request()
    download_name = f"{prefix}Technical_Documentation.md" if prefix else filename

    return send_from_directory(
        final_dir,
        filename,
        as_attachment=True,
        download_name=download_name,
        mimetype="text/markdown"
    )


@app.route("/download/word_documentation")
def download_word_documentation():
    final_dir = os.path.join(BASE_DIR, "final_output")
    docx_path = os.path.join(final_dir, "Technical_Documentation.docx")

    if not os.path.exists(docx_path):
        return jsonify({
            "error": "Documentation not generated",
            "reason": "No documentation chapters were produced.",
            "suggestion": "The uploaded project may not contain supported files."
        }), 404

    prefix = _zip_prefix_from_request()
    download_name = f"{prefix}Technical_Documentation.docx" if prefix else "Technical_Documentation.docx"

    return send_file(
        docx_path,
        as_attachment=True,
        download_name=download_name,
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


@app.route("/download/pdf_documentation")
def download_pdf():
    final_dir = os.path.join(BASE_DIR, "final_output")
    pdf_path = os.path.join(final_dir, "Technical_Documentation.pdf")

    if not os.path.exists(pdf_path):
        return jsonify({
            "error": "Documentation not generated",
            "reason": "No documentation chapters were produced.",
            "suggestion": "The uploaded project may not contain supported files."
        }), 404

    prefix = _zip_prefix_from_request()
    download_name = f"{prefix}Technical_Documentation.pdf" if prefix else "Technical_Documentation.pdf"

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name=download_name,
        mimetype="application/pdf"
    )


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def serve_spa(path):
#     file_path = os.path.join(app.static_folder, path)
#     if path and os.path.exists(file_path):
#         return send_from_directory(app.static_folder, path)
#     return send_from_directory(app.static_folder, 'index.html')

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_spa(path):
    file_path = os.path.join(app.static_folder, path)
    index_path = os.path.join(app.static_folder, "index.html")

    if path and os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)

    if os.path.exists(index_path):
        return send_from_directory(app.static_folder, "index.html")

    return "Not Found", 404

def clear_upload_folder():
    try:
        if not os.path.isdir(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            return

        for name in os.listdir(UPLOAD_FOLDER):
            path = os.path.join(UPLOAD_FOLDER, name)
            try:
                if os.path.isfile(path) or os.path.islink(path):
                    os.remove(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path, ignore_errors=True)
            except Exception as e:
                print(f"[Uploads] Failed to remove {path}: {e}")
    except Exception as e:
        print(f"[Uploads] Failed to clean upload folder: {e}")

@app.route("/analyze_async", methods=["POST"])
def analyze_async():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if not file.filename.lower().endswith(".zip"):
        return jsonify({"error": "Only .zip files are supported"}), 400

    active_job_id = _find_active_job_id()
    if active_job_id:
        return jsonify({
            "error": "Another analysis job is still running.",
            "activeJobId": active_job_id
        }), 409

    clear_upload_folder()
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    model_choice = request.form.get("model") or request.args.get("model")

    job_id = str(uuid.uuid4())
    _update_job(
        job_id,
        progress=0,
        step="queued",
        created=time.time(),
        expected_chapters=0,
        chapters_generated=0,
        canceled=False,
        zipFilename=file.filename,
        model=model_choice,
    )

    def _run():
        try:
            _update_job(job_id, progress=2, step="saved")

            try:
                size_mb = round(os.path.getsize(filepath) / 1024 / 1024, 2)
            except OSError:
                size_mb = None
            filename = os.path.basename(filepath)

            start = time.perf_counter()
            res = analyze_zip(filepath, job_id=job_id, model_choice=model_choice)
            duration_ms = int((time.perf_counter() - start) * 1000)

            if res is None:
                res = {"status": "error", "message": "No result returned from analyzer."}
            elif not isinstance(res, dict):
                res = {"status": "ok", "data": res}

            if model_choice:
                res["analysisModel"] = model_choice
                res["model"] = res.get("model", model_choice)
                res.setdefault("analysis", {}).setdefault("model", model_choice)

            try:
                final_md_async = os.path.join(BASE_DIR, "final_output", "Technical_Documentation.md")
                if os.path.exists(final_md_async):
                    sz = os.path.getsize(final_md_async)
                    res["documentationSizeBytes"] = int(sz)
                    res["documentationSizeMB"] = round(sz / 1024 / 1024, 2)
                    res.setdefault("analysis", {}).setdefault("documentationSizeBytes", int(sz))
                    res.setdefault("analysis", {}).setdefault("documentationSizeMB", round(sz / 1024 / 1024, 2))
            except Exception:
                pass

            if res.get("analysisOutput") is not None:
                res["analysis"] = res.get("analysisOutput")
                if isinstance(res["analysisOutput"], list):
                    res["results"] = res["analysisOutput"]

            if "computedTotals" in res:
                ct = res["computedTotals"]
                analysis_dict = res.setdefault("analysis", {})
                totals = analysis_dict.setdefault("totals", {})
                totals.setdefault("classes", ct.get("webChapters", 0))
                totals.setdefault("methods", ct.get("sqlChapters", 0))
                totals.setdefault("others", ct.get("utilityChapters", 0))
                totals.setdefault("api", ct.get("apiChapters", 0))

                res.setdefault("totals", {})
                res["totals"].setdefault("webChapters", ct.get("webChapters", 0))
                res["totals"].setdefault("sqlChapters", ct.get("sqlChapters", 0))
                res["totals"].setdefault("utilityChapters", ct.get("utilityChapters", 0))
                res["totals"].setdefault("apiChapters", ct.get("apiChapters", 0))

            res.update({
                "zipFilename": filename,
                "sizeMB": size_mb,
                "processingMs": duration_ms
            })

            if res.get("status") == "canceled" or _is_job_canceled(job_id):
                _update_job(job_id, progress=100, step="canceled", result=res)
            else:
                _update_job(job_id, progress=100, step="done", result=res)

        except Exception as e:
            if _is_job_canceled(job_id) or str(e).lower() == "canceled":
                _update_job(
                    job_id,
                    progress=100,
                    step="canceled",
                    result={"status": "canceled", "message": "Analysis canceled"}
                )
            else:
                _update_job(
                    job_id,
                    progress=100,
                    step="error",
                    error=str(e),
                    result={"status": "error", "message": str(e)}
                )
        finally:
            with JOB_LOCK:
                JOB_THREADS.pop(job_id, None)

    thread = threading.Thread(target=_run, daemon=True)
    with JOB_LOCK:
        JOB_THREADS[job_id] = thread
    thread.start()

    return jsonify({"jobId": job_id}), 202


@app.route("/status/<job_id>", methods=["GET"])
def job_status(job_id):
    st = _get_job(job_id)
    if not st:
        return jsonify({"error": "job not found"}), 404

    st.setdefault("expected_chapters", 0)
    st.setdefault("chapters_generated", 0)
    st.setdefault("progress", st.get("progress", 0))
    return jsonify(st)


@app.route("/cancel/<job_id>", methods=["POST"])
def cancel_job(job_id):
    st = _get_job(job_id)
    if not st:
        return jsonify({"error": "job not found"}), 404

    _update_job(
        job_id,
        step="cancel_requested",
        canceled=True
    )

    try:
        canceled = analyzer_runner.cancel_analyzer(job_id)
        _update_job(job_id, step="cancel_requested", canceled=True)

        if canceled:
            return jsonify({"status": "ok", "message": "cancel requested"}), 200
        return jsonify({"status": "ok", "message": "cancel requested (no running process found)"}), 200

    except Exception as e:
        return jsonify({"error": "cancel failed", "details": str(e)}), 500


ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_AWAYMODE_REQUIRED = 0x00000040


def _prevent_sleep() -> None:
    try:
        if platform.system() == "Windows":
            ctypes.windll.kernel32.SetThreadExecutionState(
                ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_AWAYMODE_REQUIRED
            )
            print("[KeepAwake] SetThreadExecutionState: preventing sleep")
    except Exception as e:
        print(f"[KeepAwake] unable to prevent sleep: {e}")


def _allow_sleep() -> None:
    try:
        if platform.system() == "Windows":
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
            print("[KeepAwake] SetThreadExecutionState: allowing sleep")
    except Exception as e:
        print(f"[KeepAwake] unable to restore sleep policy: {e}")


register_diagram_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)