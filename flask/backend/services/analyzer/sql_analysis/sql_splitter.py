import os
import re
import chardet
import shutil
import json
from pathlib import Path

# --- CONFIGURATION ---
# (no Documents fallback used anymore)
INPUT_SQL_FILES = []

# Centralized prompts output (so monitor can see SQL prompts)
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))  # flask/backend/services/analyzer/sql_analysis
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))  # flask/backend
PROMPTS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")
OUTPUT_FOLDER = os.path.join(PROMPTS_OUTPUT_BASE, "SQL_Documentation_Prompts")

# Allow explicit SQL file(s) passed by app.py
# Updated to support multiple files separated by ;
sql_env = os.environ.get("ANALYZER_SQL_FILE")
if sql_env:
    # If it contains semicolons, split it. Otherwise treat as single path.
    if ";" in sql_env:
        candidates = sql_env.split(";")
    else:
        candidates = [sql_env]
    
    for c in candidates:
        c = c.strip()
        if c and os.path.isfile(c):
            INPUT_SQL_FILES.append(c)

# --- TEMPLATE ---
TEMPLATE = """
### SYSTEM ROLE
You are a **Senior Database Architect**.
You are NOT a Coder. You DO NOT write SQL code.

### OBJECTIVE
Document the logic of the Stored Procedure provided below.

### 🛑 STRICT CONSTRAINTS
1. **NO SQL CODE BLOCKS.** Do not rewrite the procedure code.
2. **NO** "Here is the documentation" filler.
3. **NO** generic explanations.
4. **DO NOT EXPAND ACRONYMS.**
   (Treat these as proper nouns: [{ACRONYM_LIST}])

### ✅ REQUIRED OUTPUT FORMAT
Output exactly this structure:

# Procedure: {ProcedureName}

### Purpose
{One clear sentence explaining what business task this performs.}

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | {Inferred usage} |

### Logic Flow
{Step-by-step plain English explanation.}

### Data Interactions
* **Reads:** {List tables explicitly selected from}
* **Writes:** {List tables inserted/updated/deleted}

---

### ⬇️ RAW SQL INPUT ⬇️
{code_chunk}
### ⬆️ END OF INPUT ⬆️
**INSTRUCTION:** Document the logic above in English.
"""

# --- HELPERS ---

def detect_encoding(file_path):
    try:
        with open(file_path, 'rb') as f:
            raw = f.read(50000)
        return chardet.detect(raw)['encoding'] or 'utf-8'
    except:
        return 'latin-1'

def get_dynamic_acronyms(text):
    exclude = {
        "ADD","ALL","ALTER","AND","ANY","AS","ASC","BEGIN","CASE","CONVERT","CREATE","DATABASE",
        "DECLARE","DELETE","DROP","END","EXEC","EXISTS","FETCH","FOR","FROM","FUNCTION","GROUP",
        "HAVING","IF","IN","INSERT","INNER","JOIN","LEFT","LIKE","ORDER","OUTER","PRIMARY",
        "SELECT","SET","TABLE","UPDATE","WHERE","PROCEDURE","PROC","TRIGGER","RETURN","TRANSACTION"
    }
    candidates = re.findall(r'\b[A-Z0-9_]{2,12}\b', text)
    unique = sorted(list(set([w for w in candidates if not w.isdigit() and w not in exclude])))
    return ", ".join(f'"{a}"' for a in unique)

def extract_proc_name(proc_sql):
    pattern = (
        r'(?:CREATE|ALTER)\s+'
        r'(?:OR\s+ALTER\s+)?'
        r'(?:PROC|PROCEDURE)\s+'
        r'(?:\[?\w+\]?\.?)?'
        r'\[?([a-zA-Z0-9_]+)\]?'
    )
    match = re.search(pattern, proc_sql, re.IGNORECASE)
    if match:
        return match.group(1)
    # Fallback: try to find filename hint if present in comments? No, just unknown.
    return "Unknown_Proc"

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

# --- READING LOGIC ---

def read_procedures(file_path: str):
    print(f"Reading {file_path}...")
    encoding = detect_encoding(file_path)
    try:
        with open(file_path, "r", encoding=encoding, errors="replace") as f:
            lines = f.readlines()
    except Exception as ex:
        print(f"Error reading {file_path}: {ex}")
        return []

    procedures = []
    current_proc = []
    in_proc = False

    for line in lines:
        # Simple regex to detect CREATE PROCEDURE start
        if re.match(r'(?i)^\s*(?:CREATE\s+(?:OR\s+ALTER\s+)?|ALTER\s+)(?:PROC|PROCEDURE)\s+', line):
            if in_proc and current_proc:
                procedures.append(''.join(current_proc).strip())
            in_proc = True
            current_proc = [line]
            continue

        if in_proc:
            if re.match(r'(?i)^\s*GO\s*$', line):
                procedures.append(''.join(current_proc).strip())
                current_proc = []
                in_proc = False
            else:
                current_proc.append(line)

    if current_proc:
        procedures.append(''.join(current_proc).strip())

    return procedures

# --- MAIN EXECUTION ---

def main():
    analyzer_temp = os.environ.get("ANALYZER_TEMP_DIR") or os.environ.get("ANALYZER_WORK_DIR")
    job_id = os.environ.get("ANALYZER_JOB_ID") or os.environ.get("JOB_ID")

    # If env didn't give us valid files (INPUT_SQL_FILES is empty), fallback to scanning temp dir
    if not INPUT_SQL_FILES and analyzer_temp and os.path.isdir(analyzer_temp):
        print(f"Scanning ANALYZER_TEMP_DIR for .sql files: {analyzer_temp}")
        for p in Path(analyzer_temp).rglob("*.sql"):
            INPUT_SQL_FILES.append(str(p))

    # If still no SQL source found: write an empty manifest so monitor knows SQL contributed 0.
    if not INPUT_SQL_FILES:
        print("No SQL source detected. Skipping sql_splitter.")
        if job_id:
            try:
                os.makedirs(PROMPTS_OUTPUT_BASE, exist_ok=True)
                manifest = {"job_id": job_id, "expected": 0, "files": []}
                manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_sql_{job_id}.json")
                with open(manifest_path, "w", encoding="utf-8") as mf:
                    json.dump(manifest, mf, indent=2)
                print(f"Wrote empty SQL manifest (expected=0): {manifest_path}")
            except Exception as e:
                print(f"Error writing empty manifest: {e}")
        return

    # Ensure centralized output folder
    # Only wipe if it exists and we haven't already processed (conceptually unsafe to wipe if running in parallel, but here ok)
    # Actually, we should wipe once.
    if os.path.exists(OUTPUT_FOLDER):
        print(f"Wiping existing folder: {OUTPUT_FOLDER}")
        try:
            shutil.rmtree(OUTPUT_FOLDER)
        except OSError as e:
            print(f"Error removing {OUTPUT_FOLDER}: {e}")
            return
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    all_procs = []
    print(f"Processing {len(INPUT_SQL_FILES)} SQL file(s)...")
    
    for sql_path in INPUT_SQL_FILES:
        file_procs = read_procedures(sql_path)
        print(f"  > Found {len(file_procs)} procedures in {os.path.basename(sql_path)}")
        all_procs.extend(file_procs)

    print(f"Total found: {len(all_procs)} stored procedures.")

    if not all_procs:
        print("No procedures found across all files.")
        if job_id:
            try:
                os.makedirs(PROMPTS_OUTPUT_BASE, exist_ok=True)
                manifest = {"job_id": job_id, "expected": 0, "files": []}
                manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_sql_{job_id}.json")
                with open(manifest_path, "w", encoding="utf-8") as mf:
                    json.dump(manifest, mf, indent=2)
                print(f"Wrote empty SQL manifest (expected=0): {manifest_path}")
            except Exception as e:
                print(f"Error writing empty manifest: {e}")
        return

    created_files = []
    total_created = 0

    for i, proc_code in enumerate(all_procs, start=1):
        proc_name = extract_proc_name(proc_code)
        if proc_name == "Unknown_Proc":
            proc_name = f"Unknown_Proc_{i}"
            
        acronyms = get_dynamic_acronyms(proc_code)
        safe_name = sanitize_filename(proc_name)
        # Ensure filenames are unique (collision might happen if same proc name in different files, but i helps)
        fname = f"{i:03d}_{safe_name}.txt"
        
        final_content = TEMPLATE.replace("{ProcedureName}", proc_name) \
                                .replace("{ACRONYM_LIST}", acronyms) \
                                .replace("{code_chunk}", proc_code)
        out_path = os.path.join(OUTPUT_FOLDER, fname)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        created_files.append(out_path)
        total_created += 1
        print(f"Saved: {out_path}")

    # Write per-job manifest into prompts_output so monitor can use it
    try:
        if job_id:
            os.makedirs(PROMPTS_OUTPUT_BASE, exist_ok=True)
            manifest = {
                "job_id": job_id,
                "expected": total_created,
                "files": [os.path.relpath(p, PROMPTS_OUTPUT_BASE).replace("\\", "/") for p in created_files]
            }
            manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_sql_{job_id}.json")
            with open(manifest_path, "w", encoding="utf-8") as mf:
                json.dump(manifest, mf, indent=2)
            print(f"Wrote SQL manifest: {manifest_path} (expected={manifest['expected']})")
    except Exception as e:
        print(f"Error writing manifest: {e}")

    print(f"✅ Success! Created {total_created} SQL prompt files in '{OUTPUT_FOLDER}'.")

if __name__ == "__main__":
    main()