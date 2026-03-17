import os
import re
import chardet
import shutil
import json
from pathlib import Path

# --- CONFIGURATION ---
INPUT_SQL_FILES = []

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
PROMPTS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")
OUTPUT_FOLDER = os.path.join(PROMPTS_OUTPUT_BASE, "SQL_Documentation_Prompts")

sql_env = os.environ.get("ANALYZER_SQL_FILE")
if sql_env:
    candidates = sql_env.split(";") if ";" in sql_env else [sql_env]
    for c in candidates:
        c = c.strip()
        if c and os.path.isfile(c):
            INPUT_SQL_FILES.append(c)

# Split only oversized procedures.
MAX_SQL_CHARS_PER_PROMPT = 10000
MAX_SQL_LINES_PER_PROMPT = 400
CHUNK_OVERLAP_LINES = 0
MAX_CONTEXT_DECL_LINES = 60
MAX_CONTEXT_CHARS = 2000

TEMPLATE = """
### SYSTEM ROLE
You are a Senior Database Architect. You are NOT a Coder. You MUST NOT write SQL code.

### TASK
Document the stored procedure below.
{PartInstruction}

### SOURCE METADATA
# ProcedureName: {ProcedureName}
**PartNumber:** {PartNumber}
**TotalParts:** {TotalParts}
**File:** {SourceFilename}
**Path:** {SourcePath}

### REQUIRED OUTPUT
### Purpose
(DO NOT LEAVE PURPOSE OUT.)

### Logic Flow
1.
2.
3.

### STRICT RULES
1. Start your response with exactly:
# Procedure: {ProcedureName}{PartSuffix}

2. Make sure to fill in the purpose.
3. You MUST output ALL sections exactly as shown, even if information is not present. If information is missing, write: None
4. Do NOT add any introduction or conclusion.
5. Do NOT ask follow-up questions.
6. Do NOT say things like:
   - "Here is the documentation"
   - "Overall Purpose"
   - "Do you want me to elaborate"
   - "Would you like me to"
7. Do NOT rewrite the SQL code.
8. Do NOT quote or copy SQL statements.
9. Describe behavior in plain language only.
10. Do NOT expand acronyms.
   Treat these as proper nouns: [{ACRONYM_LIST}]
11. Do NOT output a Parameters section.
12. Do NOT output schema tables, column lists, or field-by-field breakdowns.

{GlobalContextSection}

### RAW SQL INPUT
{code_chunk}

### FINAL INSTRUCTION
Return ONLY the required output format.
Do not miss out on ### Purpose.
Do not write anything before "# Procedure: {ProcedureName}{PartSuffix}".
Do not add any sections after Logic Flow. Do not add the rules given. Do not add the raw SQL input.
""".lstrip()


def detect_encoding(file_path):
    try:
        with open(file_path, "rb") as f:
            raw = f.read(50000)
        return chardet.detect(raw)["encoding"] or "utf-8"
    except Exception:
        return "latin-1"


def get_dynamic_acronyms(text):
    exclude = {
        "ADD", "ALL", "ALTER", "AND", "ANY", "AS", "ASC", "BEGIN", "CASE", "CONVERT", "CREATE", "DATABASE",
        "DECLARE", "DELETE", "DROP", "END", "EXEC", "EXISTS", "FETCH", "FOR", "FROM", "FUNCTION", "GROUP",
        "HAVING", "IF", "IN", "INSERT", "INNER", "JOIN", "LEFT", "LIKE", "ORDER", "OUTER", "PRIMARY",
        "SELECT", "SET", "TABLE", "UPDATE", "WHERE", "PROCEDURE", "PROC", "TRIGGER", "RETURN", "TRANSACTION",
        "TOP", "INTO", "OUTPUT", "NULL", "NOT", "OR", "ON", "BY", "VALUES", "MERGE", "USING", "GO",
        "TRY", "CATCH", "ROLLBACK", "COMMIT", "DISTINCT"
    }
    candidates = re.findall(r"\b[A-Z0-9_]{2,20}\b", text)
    unique = sorted(list(set([w for w in candidates if not w.isdigit() and w not in exclude])))
    return ", ".join(f'"{a}"' for a in unique)


def extract_proc_name(proc_sql):
    pattern = (
        r"(?is)\b(?:CREATE|ALTER)\s+"
        r"(?:OR\s+ALTER\s+)?"
        r"(?:PROC|PROCEDURE)\s+"
        r"(?:(?:\[[^\]]+\]|\w+)\s*\.\s*)?"
        r"\[?([A-Za-z0-9_]+)\]?"
    )
    match = re.search(pattern, proc_sql)
    return match.group(1) if match else "Unknown_Proc"


def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)


def extract_parameter_block(proc_sql: str) -> str:
    lines = proc_sql.replace("\r\n", "\n").replace("\r", "\n").splitlines()

    start_idx = None
    for i, line in enumerate(lines):
        if re.search(r"(?i)\b(?:CREATE|ALTER)\s+(?:OR\s+ALTER\s+)?(?:PROC|PROCEDURE)\b", line):
            start_idx = i
            break

    if start_idx is None:
        return "None"

    collected = []
    paren_depth = 0
    saw_proc_header = False

    for i in range(start_idx, len(lines)):
        line = lines[i].rstrip()

        if not saw_proc_header:
            saw_proc_header = True
            continue

        paren_depth += line.count("(") - line.count(")")

        if paren_depth <= 0 and re.match(r"^\s*AS\b", line, flags=re.IGNORECASE):
            break

        if line.strip():
            collected.append(line.strip())

    if not collected:
        return "None"

    param_lines = [ln for ln in collected if "@" in ln]
    if not param_lines:
        return "None"

    return "\n".join(param_lines[:MAX_CONTEXT_DECL_LINES])


def extract_key_declarations(proc_sql: str, limit: int = 120) -> str:
    decls = []

    for line in proc_sql.splitlines():
        stripped = line.strip()

        m = re.match(r"(?i)^declare\s+(@\w+)", stripped)
        if m:
            decls.append(m.group(1))
            continue

        m2 = re.match(r"(?i)^create\s+table\s+(#\#?\w+)", stripped)
        if m2:
            decls.append(m2.group(1))
            continue

        m3 = re.match(r"(?i)^select\b.*\binto\s+(#\#?\w+)", stripped)
        if m3:
            decls.append(m3.group(1))
            continue

    if not decls:
        return "None"

    seen = []
    used = set()
    for d in decls:
        key = d.lower()
        if key not in used:
            used.add(key)
            seen.append(d)

    return ", ".join(seen[:limit])


def extract_temp_objects(proc_sql: str) -> str:
    objs = set()

    # local/global temp tables
    for name in re.findall(r"(?i)\bcreate\s+table\s+(#\#?\w+)", proc_sql):
        objs.add(name)

    for name in re.findall(r"(?i)\bselect\b[\s\S]*?\binto\s+(#\#?\w+)", proc_sql):
        objs.add(name)

    for name in re.findall(r"(?i)\b(?:from|join|into|update|merge\s+into|delete\s+from)\s+(#\#?\w+)", proc_sql):
        objs.add(name)

    # table variables
    for name in re.findall(r"(?i)\bdeclare\s+(@\w+)\s+table\b", proc_sql):
        objs.add(name)

    for name in re.findall(r"(?i)\b(?:from|join|into|update|merge\s+into|delete\s+from)\s+(@\w+)", proc_sql):
        objs.add(name)

    if not objs:
        return "None"

    return ", ".join(sorted(objs, key=str.lower))


def extract_main_table_refs(proc_sql: str, limit: int = 40) -> str:
    refs = []

    patterns = [
        r"(?i)\bfrom\s+([@#\[\]\w\.]+)",
        r"(?i)\bjoin\s+([@#\[\]\w\.]+)",
        r"(?i)\binsert\s+into\s+([@#\[\]\w\.]+)",
        r"(?i)\bupdate\s+([@#\[\]\w\.]+)",
        r"(?i)\bdelete\s+from\s+([@#\[\]\w\.]+)",
        r"(?i)\bmerge\s+into\s+([@#\[\]\w\.]+)",
    ]

    for pattern in patterns:
        for m in re.finditer(pattern, proc_sql):
            refs.append(m.group(1))

    cleaned = []
    seen = set()

    for ref in refs:
        ref = ref.strip().rstrip(",;")
        if ref.startswith("("):
            continue

        parts = re.findall(r"\[([^\]]+)\]|([@#A-Za-z0-9_]+)", ref)
        tokens = [a or b for a, b in parts if (a or b)]
        if not tokens:
            continue

        if tokens[0].startswith("@") or tokens[0].startswith("#"):
            final_name = tokens[0]
        else:
            final_name = tokens[-1]

        key = final_name.lower()
        if key not in seen:
            seen.add(key)
            cleaned.append(final_name)

    if not cleaned:
        return "None"

    return ", ".join(cleaned[:limit])


def build_global_context(proc_name: str, proc_sql: str) -> str:
    param_block = extract_parameter_block(proc_sql)
    temp_objs = extract_temp_objects(proc_sql)
    table_refs = extract_main_table_refs(proc_sql)

    context = (
        f"Procedure Name: {proc_name}\n\n"
        f"Parameters:\n{param_block}\n\n"
        f"Temp/Table Objects: {temp_objs}\n\n"
        f"Main Table References: {table_refs}"
    )

    if len(context) > MAX_CONTEXT_CHARS:
        context = context[:MAX_CONTEXT_CHARS].rstrip() + "\n\n[Context truncated due to length.]"

    return context


def choose_split_index(lines, start, hard_end):
    """
    Prefer to split near logical SQL boundaries instead of blindly at hard_end.
    """
    candidates = []

    search_start = max(start + 1, hard_end - 80)
    search_end = min(len(lines), hard_end + 1)

    boundary_patterns = [
        r"(?i)^\s*IF\b",
        r"(?i)^\s*ELSE\b",
        r"(?i)^\s*BEGIN\b",
        r"(?i)^\s*END\b",
        r"(?i)^\s*WITH\b",
        r"(?i)^\s*SELECT\b",
        r"(?i)^\s*INSERT\b",
        r"(?i)^\s*UPDATE\b",
        r"(?i)^\s*DELETE\b",
        r"(?i)^\s*MERGE\b",
        r"(?i)^\s*CREATE\s+TABLE\b",
        r"(?i)^\s*DECLARE\b",
    ]

    for i in range(search_start, search_end):
        line = lines[i].strip()
        if not line:
            candidates.append(i)
            continue

        for pat in boundary_patterns:
            if re.match(pat, line):
                candidates.append(i)
                break

    if candidates:
        return max(candidates)

    return hard_end


def split_proc_if_too_long(proc_sql: str):
    line_count = proc_sql.count("\n") + 1
    if len(proc_sql) <= MAX_SQL_CHARS_PER_PROMPT and line_count <= MAX_SQL_LINES_PER_PROMPT:
        return [proc_sql]

    lines = proc_sql.splitlines(keepends=True)
    chunks = []
    start = 0

    while start < len(lines):
        current_lines = []
        current_len = 0
        end = start

        while end < len(lines):
            next_line = lines[end]
            if current_lines and (
                current_len + len(next_line) > MAX_SQL_CHARS_PER_PROMPT
                or len(current_lines) >= MAX_SQL_LINES_PER_PROMPT
            ):
                break
            current_lines.append(next_line)
            current_len += len(next_line)
            end += 1

        if end < len(lines):
            preferred_end = choose_split_index(lines, start, end - 1)
            if preferred_end >= start:
                current_lines = lines[start:preferred_end + 1]
                end = preferred_end + 1

        chunk = "".join(current_lines).strip()
        if chunk:
            chunks.append(chunk)

        if end >= len(lines):
            break

        start = end if CHUNK_OVERLAP_LINES <= 0 else max(end - CHUNK_OVERLAP_LINES, start + 1)

    return chunks


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

    start_re = re.compile(r"(?i)^\s*(?:CREATE\s+(?:OR\s+ALTER\s+)?|ALTER\s+)(?:PROC|PROCEDURE)\s+")
    go_re = re.compile(r"(?i)^\s*GO\s*$")

    for line in lines:
        if start_re.match(line):
            if in_proc and current_proc:
                procedures.append("".join(current_proc).strip())
            in_proc = True
            current_proc = [line]
            continue

        if in_proc:
            if go_re.match(line):
                procedures.append("".join(current_proc).strip())
                current_proc = []
                in_proc = False
            else:
                current_proc.append(line)

    if current_proc:
        procedures.append("".join(current_proc).strip())

    return procedures


def write_empty_manifest(job_id: str):
    try:
        os.makedirs(PROMPTS_OUTPUT_BASE, exist_ok=True)
        manifest = {"job_id": job_id, "expected": 0, "files": []}
        manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_sql_{job_id}.json")
        with open(manifest_path, "w", encoding="utf-8") as mf:
            json.dump(manifest, mf, indent=2)
        print(f"Wrote empty SQL manifest (expected=0): {manifest_path}")
    except Exception as e:
        print(f"Error writing empty manifest: {e}")


def main():
    analyzer_temp = os.environ.get("ANALYZER_TEMP_DIR") or os.environ.get("ANALYZER_WORK_DIR")
    job_id = os.environ.get("ANALYZER_JOB_ID") or os.environ.get("JOB_ID")

    if not INPUT_SQL_FILES and analyzer_temp and os.path.isdir(analyzer_temp):
        print(f"Scanning ANALYZER_TEMP_DIR for .sql files: {analyzer_temp}")
        for p in Path(analyzer_temp).rglob("*.sql"):
            INPUT_SQL_FILES.append(str(p))

    if not INPUT_SQL_FILES:
        print("No SQL source detected. Skipping sql_splitter.")
        if job_id:
            write_empty_manifest(job_id)
        return

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
        source_filename = os.path.basename(sql_path)
        analyzer_root = os.environ.get("ANALYZER_TEMP_DIR") or os.environ.get("ANALYZER_WORK_DIR")

        if analyzer_root and sql_path.startswith(analyzer_root):
            source_path = os.path.relpath(sql_path, analyzer_root)
        else:
            source_path = os.path.basename(sql_path)

        source_path = source_path.replace("\\", "/")

        print(f"  > Found {len(file_procs)} procedures in {source_filename}")
        for proc in file_procs:
            all_procs.append({
                "proc_code": proc,
                "source_filename": source_filename,
                "source_path": source_path,
            })

    print(f"Total found: {len(all_procs)} stored procedures.")

    if not all_procs:
        print("No procedures found across all files.")
        if job_id:
            write_empty_manifest(job_id)
        return

    created_files = []
    total_created = 0

    for i, proc_item in enumerate(all_procs, start=1):
        proc_code = proc_item["proc_code"]
        source_filename = proc_item["source_filename"]
        source_path = proc_item["source_path"]
        proc_name = extract_proc_name(proc_code)
        if proc_name == "Unknown_Proc":
            proc_name = f"Unknown_Proc_{i}"

        acronyms = get_dynamic_acronyms(proc_code)
        safe_name = sanitize_filename(proc_name)
        parts = split_proc_if_too_long(proc_code)
        context_block = build_global_context(proc_name, proc_code) if len(parts) > 1 else ""

        if len(parts) == 1:
            fname = f"{i:03d}_{safe_name}.txt"
            final_content = (
                TEMPLATE.replace("{ProcedureName}", proc_name)
                .replace("{PartSuffix}", "")
                .replace("{PartInstruction}", "")
                .replace("{SourceFilename}", source_filename)
                .replace("{SourcePath}", source_path)
                .replace("{ACRONYM_LIST}", acronyms)
                .replace("{GlobalContextSection}", "")
                .replace("{code_chunk}", parts[0])
                .replace("{PartNumber}", "")
                .replace("{TotalParts}", "")
            )
            out_path = os.path.join(OUTPUT_FOLDER, fname)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(final_content)
            created_files.append(out_path)
            total_created += 1
            print(f"Saved: {out_path}")
        else:
            global_context_section = f"### GLOBAL CONTEXT\n{context_block}\n\n"
            print(f"Procedure '{proc_name}' is long; splitting into {len(parts)} parts...")
            for part_idx, part_sql in enumerate(parts, start=1):
                fname = f"{i:03d}_{safe_name}_part{part_idx}.txt"
                part_suffix = f" (Part {part_idx} of {len(parts)})"
                part_instruction = (
                    f"This file contains only one chunk of the full procedure. "
                    f"Document this chunk as Part {part_idx} of {len(parts)} while keeping terminology consistent with the full procedure."
                    f"Use it only to understand earlier setup. Document only the current chunk's contribution. Do NOT repeat steps already described in earlier parts."
                )
                final_content = (
                    TEMPLATE.replace("{ProcedureName}", proc_name)
                    .replace("{PartSuffix}", part_suffix)
                    .replace("{PartInstruction}", part_instruction)
                    .replace("{SourceFilename}", source_filename)
                    .replace("{SourcePath}", source_path)
                    .replace("{ACRONYM_LIST}", acronyms)
                    .replace("{GlobalContextSection}", global_context_section)
                    .replace("{code_chunk}", part_sql)
                    .replace("{PartNumber}", str(part_idx))
                    .replace("{TotalParts}", str(len(parts)))
                )
                out_path = os.path.join(OUTPUT_FOLDER, fname)
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(final_content)
                created_files.append(out_path)
                total_created += 1
                print(f"Saved: {out_path}")

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