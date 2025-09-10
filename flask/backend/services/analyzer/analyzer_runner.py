import subprocess
import json
import os

def analyze_code(file_path: str):
    """
    Runs the Roslyn Analyzer C# project on the given file.
    Returns JSON output as a Python dictionary.
    """
    # Resolve the analyzer project directory relative to this file
    this_dir = os.path.dirname(__file__)
    analyzer_project_dir = os.path.abspath(os.path.join(this_dir, "../../../../Roslyn"))

    cmd = [
        "dotnet", "run",
        "--project", analyzer_project_dir,
        "--",  # ensure following arg is passed to the app, not dotnet
        file_path
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Analyzer failed: {result.stderr}")

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
