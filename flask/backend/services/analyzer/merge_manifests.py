import os
import json
from pathlib import Path

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))  # flask/backend/services/analyzer
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))  # flask/backend
PROMPTS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")
PAGE_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "Page_Documentation_Prompts")
UTIL_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "Utility_Documentation_Prompts")
UTIL_SQL_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "Utility_SQL_Documentation_Prompts")
SQL_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "SQL_Documentation_Prompts")
API_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "API_Documentation_Prompts")
HTML_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "HTML_Documentation_Prompts")

def read_manifest(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def collect_txt_files():
    files = []
    for d in (PAGE_DIR, UTIL_DIR, SQL_DIR, API_DIR, UTIL_SQL_DIR, HTML_DIR):
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.endswith(".txt"):
                    files.append(os.path.join(os.path.relpath(d, PROMPTS_OUTPUT_BASE), f).replace("\\", "/"))
    return files

def main():
    job_id = os.environ.get("ANALYZER_JOB_ID") or os.environ.get("JOB_ID") or "global"
    ai_manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_ai_{job_id}.json")
    sql_manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_sql_{job_id}.json")
    api_manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_api_{job_id}.json")
    final_manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_{job_id}.json")


    files_set = set()

    ai_m = read_manifest(ai_manifest_path)
    if ai_m and isinstance(ai_m.get("files"), list):
        files_set.update(ai_m["files"])

    sql_m = read_manifest(sql_manifest_path)
    if sql_m and isinstance(sql_m.get("files"), list):
        files_set.update(sql_m["files"])

    api_m = read_manifest(api_manifest_path)
    if api_m and isinstance(api_m.get("files"), list):
        files_set.update(api_m["files"])

    # If any manifest is missing, fall back to scanning prompt folders to be safe
    if not ai_m or not sql_m or not api_m:
        files_set.update(collect_txt_files())

    files = sorted(files_set)
    manifest = {
        "job_id": job_id,
        "expected": len(files),
        "files": files
    }
    try:
        os.makedirs(PROMPTS_OUTPUT_BASE, exist_ok=True)
        with open(final_manifest_path, "w", encoding="utf-8") as mf:
            json.dump(manifest, mf, indent=2)
        print(f"Wrote merged manifest: {final_manifest_path} (expected={manifest['expected']})")
    except Exception as e:
        print(f"Failed to write merged manifest: {e}")

if __name__ == "__main__":
    main()