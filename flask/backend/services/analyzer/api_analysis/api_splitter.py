import json
import os
import shutil

# --- OUTPUT BASE: place prompts under flask/backend/prompts_output ---
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))  # flask/backend/services/analyzer/api_analysis
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))  # flask/backend
PROMPTS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")

# Input: flask/backend/static_analysis_output/all_analysis_results.json
STATIC_OUTPUT_DIR = os.path.join(BACKEND_DIR, "static_analysis_output")
STATIC_ANALYSIS_FILE = os.path.join(STATIC_OUTPUT_DIR, "all_analysis_results.json")

API_OUTPUT_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "API_Documentation_Prompts")
MAX_FILENAME_LENGTH = 200

# --- PROMPT TEMPLATE ---
API_TEMPLATE = """
### SYSTEM ROLE
You are a **Technical Writer** documenting API endpoints for a legacy ASP.NET system.
You are NOT a Developer. You DO NOT write code.

### OBJECTIVE
Produce a concise API Reference entry for the endpoint described below.
Focus on what the endpoint does, its inputs, outputs, and any relevant behaviour.

### HARD CONSTRAINTS
1. NO code blocks (C#, VB.NET, SQL, JSON).
2. NO speculative assertions beyond what is explicitly provided.
3. If a field is unknown or empty, write "Not specified" rather than guessing.

### OUTPUT FORMAT
# API Endpoint: {endpoint_title}

**Kind:** {kind}
**Controller / Service:** {controller}
**Operation:** {operation}
**Source File:** {source_file}
**Route:** {route}
**HTTP Methods:** {http_methods}

### Parameters
| Name | Type |
| :--- | :--- |
{parameters_table}

### Return Type
{return_type}

### Purpose & Behaviour
{Describe what this endpoint does in plain English based on the metadata below.
If the purpose cannot be determined, write "Purpose unknown — insufficient metadata."}

---

### RAW ENDPOINT METADATA 
{metadata_chunk}
### END OF METADATA 

Instruction: Document the API endpoint above. Focus on purpose, parameters, return value, and expected behaviour.
"""


def _safe_filename(s: str) -> str:
    if not s:
        return "unknown"
    return "".join(c if c.isalnum() or c in "-._" else "_" for c in s)[:MAX_FILENAME_LENGTH]


def main():
    print(f"Reading {STATIC_ANALYSIS_FILE}...")
    try:
        with open(STATIC_ANALYSIS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading input: {e}")
        return

    job_id = os.environ.get("ANALYZER_JOB_ID") or os.environ.get("JOB_ID") or "global"

    # Collect all api_endpoints from the static analysis results
    all_endpoints = []
    for item in data:
        endpoints = item.get("api_endpoints")
        if not endpoints:
            continue
        for ep in endpoints:
            all_endpoints.append(ep)

    if not all_endpoints:
        print("No API endpoints detected in static analysis output. Skipping api_splitter.")
        # Write an empty manifest so merge_manifests.py knows the API stream contributed 0
        try:
            os.makedirs(PROMPTS_OUTPUT_BASE, exist_ok=True)
            manifest = {"job_id": job_id, "expected": 0, "files": []}
            manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_api_{job_id}.json")
            with open(manifest_path, "w", encoding="utf-8") as mf:
                json.dump(manifest, mf, indent=2)
            print(f"Wrote empty API manifest (expected=0): {manifest_path}")
        except Exception as e:
            print(f"Error writing empty manifest: {e}")
        return

    # Prepare output folder (wipe and recreate)
    os.makedirs(PROMPTS_OUTPUT_BASE, exist_ok=True)
    if os.path.exists(API_OUTPUT_DIR):
        shutil.rmtree(API_OUTPUT_DIR)
    os.makedirs(API_OUTPUT_DIR, exist_ok=True)

    created_files = []
    for idx, ep in enumerate(all_endpoints, start=1):
        kind = ep.get("Kind") or ep.get("kind") or "unknown"
        controller = ep.get("ControllerOrServiceName") or ep.get("controllerOrServiceName") or ""
        operation = ep.get("OperationName") or ep.get("operationName") or ""
        source_file = ep.get("FilePath") or ep.get("filePath") or ""
        route = ep.get("Route") or ep.get("route") or ""
        http_methods_list = ep.get("HttpMethods") or ep.get("httpMethods") or []
        parameters = ep.get("parameters") or ep.get("Parameters") or []
        return_type = ep.get("ReturnType") or ep.get("returnType") or "void"
        evidence = ep.get("Evidence") or ep.get("evidence") or ""

        http_methods_str = ", ".join(http_methods_list) if http_methods_list else "Not specified"
        endpoint_title = f"{controller}.{operation}" if controller else operation

        # Build parameters table rows
        if parameters:
            param_rows = "\n".join(
                f"| {p.get('Name') or p.get('name') or ''} | {p.get('Type') or p.get('type') or ''} |"
                for p in parameters
            )
        else:
            param_rows = "| (none) | |"

        content = API_TEMPLATE
        content = content.replace("{endpoint_title}", endpoint_title)
        content = content.replace("{kind}", kind)
        content = content.replace("{controller}", controller or "Not specified")
        content = content.replace("{operation}", operation or "Not specified")
        content = content.replace("{source_file}", source_file or "Not specified")
        content = content.replace("{route}", route or "Not specified")
        content = content.replace("{http_methods}", http_methods_str)
        content = content.replace("{parameters_table}", param_rows)
        content = content.replace("{return_type}", return_type or "Not specified")
        content = content.replace("{metadata_chunk}", json.dumps(ep, indent=2))

        safe_controller = _safe_filename(controller)
        safe_operation = _safe_filename(operation)
        filename = f"{idx:03d}_{kind}_{safe_controller}_{safe_operation}.txt"
        out_path = os.path.join(API_OUTPUT_DIR, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        created_files.append(out_path)
        print(f"Saved API prompt: {out_path}")

    # Write per-job manifest
    try:
        manifest = {
            "job_id": job_id,
            "expected": len(created_files),
            "files": [
                os.path.relpath(p, PROMPTS_OUTPUT_BASE).replace("\\", "/")
                for p in created_files
            ]
        }
        manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_api_{job_id}.json")
        with open(manifest_path, "w", encoding="utf-8") as mf:
            json.dump(manifest, mf, indent=2)
        print(f"Wrote API manifest: {manifest_path} (expected={manifest['expected']})")
    except Exception as e:
        print(f"Error writing manifest: {e}")

    print(f"DONE! {len(created_files)} API prompt files saved in '{API_OUTPUT_DIR}'.")


if __name__ == "__main__":
    main()
