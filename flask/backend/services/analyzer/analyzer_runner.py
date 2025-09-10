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
    # Adjust if your analyzer project is in a different location
    analyzer_project_dir = os.path.abspath(os.path.join(this_dir, "../../../../Roslyn"))

    cmd = [
        "dotnet", "run",
        "--project", analyzer_project_dir,
        file_path
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Analyzer failed: {result.stderr}")

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"error": "Invalid output from analyzer", "raw": result.stdout}
