import subprocess
import json
import os
from typing import Any

def analyze_code(*file_paths: str) -> Any:
    """
    Runs the Roslyn Analyzer C# project on the given file(s).
    Accepts one or more file paths and returns JSON output as a Python object.
    """
    if len(file_paths) == 0:
        raise ValueError("analyze_code requires at least one file path")

    # Resolve the analyzer project directory relative to this file
    this_dir = os.path.dirname(__file__)
    analyzer_project_dir = os.path.abspath(os.path.join(this_dir, "../../../../Roslyn"))

    cmd = [
        "dotnet", "run",
        "--project", analyzer_project_dir,
        "--",  # ensure following args are passed to the app, not dotnet
    ] + list(file_paths)

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        # Include both stdout and stderr for diagnostics
        raise RuntimeError(f"Analyzer failed:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")

    stdout = result.stdout.strip()

    # Try parsing full stdout first
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        # Fallback: find the last JSON-looking line
        for line in reversed(stdout.splitlines()):
            s = line.strip()
            if s.startswith("{") or s.startswith("["):
                try:
                    return json.loads(s)
                except json.JSONDecodeError:
                    continue

    # If still not JSON, return diagnostic info
    return {"error": "Invalid output from analyzer", "raw": stdout, "stderr": result.stderr}
