import subprocess
import json
import os
import signal
import threading
import re
import tempfile
from typing import Any, Dict, Optional, Callable

# Map job_id -> Popen
_PROCS: Dict[str, subprocess.Popen] = {}
_PROCS_LOCK = threading.Lock()

def _register_proc(job_id: str, proc: subprocess.Popen) -> None:
    with _PROCS_LOCK:
        _PROCS[job_id] = proc

def _unregister_proc(job_id: str) -> None:
    with _PROCS_LOCK:
        _PROCS.pop(job_id, None)

def cancel_analyzer(job_id: str) -> bool:
    """
    Attempt to terminate the running analyzer process for the given job_id.
    Returns True if a process was found and termination was attempted.
    """
    with _PROCS_LOCK:
        proc = _PROCS.get(job_id)
    if not proc:
        return False
    try:
        # POSIX: kill process group
        if os.name != "nt":
            try:
                os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
            except Exception:
                try:
                    proc.kill()
                except Exception:
                    pass
        else:
            # Windows: try CTRL_BREAK, then terminate
            try:
                proc.send_signal(signal.CTRL_BREAK_EVENT)
            except Exception:
                try:
                    proc.terminate()
                except Exception:
                    pass
    except Exception:
        # best-effort; ignore errors
        pass
    finally:
        _unregister_proc(job_id)
    return True

def _clean_and_parse_json(stdout_content: str) -> Any:
    """
    Attempts to find valid JSON within the stdout content by stripping
    potential build warnings or prefixes.
    """
    if not stdout_content:
        raise json.JSONDecodeError("Empty output", "", 0)

    # 1. Try parsing directly
    try:
        return json.loads(stdout_content)
    except json.JSONDecodeError:
        pass

    # 2. Try to find the JSON start
    # The analyzer typically returns a list [...] or an object {...}
    # We look for the FIRST occurrence of '[' or '{'
    
    # Simple index find
    idx_brace = stdout_content.find('{')
    idx_bracket = stdout_content.find('[')
    
    candidates = []
    if idx_brace != -1: candidates.append(idx_brace)
    if idx_bracket != -1: candidates.append(idx_bracket)
    
    if not candidates:
        # Maybe it's buried in lines?
        pass
    else:
        # Try from the earliest candidate
        start_idx = min(candidates)
        try:
            return json.loads(stdout_content[start_idx:])
        except json.JSONDecodeError:
            pass

    # 3. Aggressive: Line-by-line filtering to remove non-JSON lines
    # This helps if warnings are interleaved or at the very start
    lines = stdout_content.splitlines()
    json_lines = []
    started = False
    
    for line in lines:
        sline = line.strip()
        # Heuristic: Start capturing if line looks like start of JSON
        if not started:
            if sline.startswith('[') or sline.startswith('{'):
                started = True
                json_lines.append(line)
        else:
            # Once started, keep lines unless they look like specific dotnet warnings
            # that might be interleaved (unlikely but possible)
            if not sline.startswith("warning NETSDK"):
                json_lines.append(line)
    
    if json_lines:
        try:
            return json.loads('\n'.join(json_lines))
        except json.JSONDecodeError:
            pass

    raise json.JSONDecodeError("No valid JSON found after cleaning attempts", stdout_content, 0)

def analyze_code(*file_paths: str, job_id: Optional[str] = None, progress_callback: Optional[Callable[[int, int], None]] = None) -> Any:
    """
    Run the respective analyzers on the given file(s).
    Accepts one or more file paths and returns JSON output as a Python object.
    Optional job_id registers the child process for cancellation.
    Optional progress_callback(processed_count, total_files) to receive updates during execution.
    """
    if len(file_paths) == 0:
        # Return empty list if no files - consistent with analyzer behavior
        return []

    this_dir = os.path.dirname(__file__)
    analyzer_project_dir = os.path.abspath(os.path.join(this_dir, "../../../../Roslyn"))

    # Determine command arguments
    # To fix WinError 206 (filename too long), we write the list of files to a temporary file
    # and pass that single file path to the analyzer.
    # The analyzer (Program.cs) must handle args[0] as a file list if it ends in .txt.
    
    list_file_path = None
    try:
        # Create a temp file list in the system temp directory
        # We use delete=False so we can close it before passing to subprocess, 
        # and then delete it manually in finally block.
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as tf:
            list_file_path = tf.name
            for fp in file_paths:
                tf.write(fp + "\n")
        
        args = [list_file_path]
    except Exception as e:
        # Fallback to direct ref if temp file creation fails (unlikely, but safe)
        print(f"[Warn] Failed to create arg list file: {e}. Falling back to CLI args.")
        args = list(file_paths)

    # Use dotnet directly  avoid requiring a .env file via `dotenv run`
    # cmd = [
    #     "dotnet", "run",
    #     "--project", analyzer_project_dir,
    #     "--",
    # ] + args

    cmd = [
    "dotnet", "run",
    "--project", analyzer_project_dir,
    "-p:RunAnalyzers=false",
    "-p:BuildProjectReferences=false",
    "--",
] + args

    # cmd = [
    #     "dotnet",
    #     os.path.join(analyzer_project_dir, "bin", "Release", "net6.0", "Roslyn.dll"),
    # ] + args

    env = os.environ.copy()
    final_output = os.path.abspath(os.path.join(this_dir, "..", "..", "static_analysis_output"))
    os.makedirs(final_output, exist_ok=True)
    env["ANALYZER_OUTPUT_DIR"] = final_output
    env["DOTNET_SKIP_FIRST_TIME_EXPERIENCE"] = "1"
    env["DOTNET_CLI_TELEMETRY_OPTOUT"] = "1"
    env["DOTNET_NOLOGO"] = "1"

    flask_root = os.path.abspath(os.path.join(this_dir, "..", "..", ".."))
    if os.path.isdir(flask_root):
        env["FLASK_ROOT"] = flask_root

    # Platform-specific process-group handling so we can kill entire tree
    popen_kwargs = {
        "stdout": subprocess.PIPE,
        "stderr": subprocess.PIPE,
        "text": True,
        "encoding": "utf-8",
        "errors": "replace",
        "env": env,
        "bufsize": 1 # Line buffered
    }

    if os.name == "nt":
        # Create new process group so CTRL_BREAK_EVENT targets it
        popen_kwargs["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
    else:
        # POSIX: start new session -> new process group
        popen_kwargs["preexec_fn"] = os.setsid

    proc = subprocess.Popen(cmd, **popen_kwargs)

    if job_id:
        _register_proc(job_id, proc)

    # Capture outputs
    captured_stdout = []
    captured_stderr = []

    # Thread for stderr to capture logs without blocking stdout reading
    def read_stderr(p, out_list):
        try:
            for line in p.stderr:
                out_list.append(line)
        except:
            pass
    
    stderr_thread = threading.Thread(target=read_stderr, args=(proc, captured_stderr))
    stderr_thread.start()

    # Tracking vars for progress
    total_files_known = len(file_paths)
    processed_count = 0

    try:
        # Read stdout line by line to detect progress in real-time
        # We iterate proc.stdout directly; it yields lines as they are flushed
        for line in proc.stdout:
            captured_stdout.append(line)
            
            # Heuristic detection of progress logic
            if progress_callback:
                sline = line.strip()
                
                # Check for Roslyn activity markers (either JSON debug or plain text)
                activity_detected = False
                
                # 1. Check for JSON debug lines: { "debug": "Analyzing file...", ... }
                if sline.startswith("{") and sline.endswith("}"):
                    try:
                        data = json.loads(sline)
                        if isinstance(data, dict):
                            # If tool reports count explicitly
                            if "count" in data and isinstance(data["count"], int):
                                total_files_known = data["count"]
                            
                            # If tool reports file analysis
                            if "debug" in data and ("Analyzing" in data["debug"] or "Processing" in data["debug"]):
                                activity_detected = True
                    except:
                        pass
                
                # 2. Check for plain text logs: "[Info] Analyzing file X" or just "Analyzing..."
                elif "Analyzing" in sline or "Processing" in sline:
                    activity_detected = True

                if activity_detected:
                    processed_count += 1
                    # Fire callback
                    progress_callback(processed_count, total_files_known)

        # Wait for exit
        proc.wait()
        stderr_thread.join(timeout=2.0)

    finally:
        if job_id:
            _unregister_proc(job_id)
        
        # Clean up temp list file
        if list_file_path and os.path.exists(list_file_path):
            try:
                os.remove(list_file_path)
            except:
                pass

    stdout = "".join(captured_stdout).strip()
    stderr = "".join(captured_stderr).strip()

    if proc.returncode != 0:
        raise RuntimeError(f"Analyzer failed (returncode={proc.returncode}):\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}")

    analysis_file = os.path.join(final_output, "all_analysis_results.json")

    if os.path.exists(analysis_file):
        try:
            with open(analysis_file, "r", encoding="utf-8") as f:
                parsed = json.load(f)
        except Exception as e:
            return {
                "error": f"Failed to read analyzer output file: {e}",
                "raw": stdout,
                "stderr": stderr
            }
    else:
        try:
            parsed = json.loads(stdout)
        except json.JSONDecodeError:
            try:
                parsed = _clean_and_parse_json(stdout)
            except json.JSONDecodeError:
                return {"error": "Invalid output from analyzer", "raw": stdout, "stderr": stderr}

    if isinstance(parsed, dict):
        parsed["runner_stdout"] = stdout
        parsed["runner_stderr"] = stderr
        return parsed
    else:
        return {"analysis": parsed, "runner_stdout": stdout, "runner_stderr": stderr}

