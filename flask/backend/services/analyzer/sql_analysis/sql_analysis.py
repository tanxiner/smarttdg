import os
import re
import zlib
import shutil
import subprocess
import time
import socket
from collections import Counter
from langchain_community.llms import Ollama

# --- CONFIGURATION ---
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
PROMPTS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")
ANALYSIS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "analysis_output")

INPUT_FOLDER = os.path.join(PROMPTS_OUTPUT_BASE, "SQL_Documentation_Prompts")
OUTPUT_FOLDER = os.path.join(ANALYSIS_OUTPUT_BASE, "Final_SQL_Docs")

DEFAULT_MODEL = "gemma3:latest"
MODEL_NAME = os.environ.get("ANALYSIS_MODEL", DEFAULT_MODEL)
MAX_RETRIES = 5

def standardize_sql_headings(text: str) -> str:
    if not text:
        return text

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Keep procedure title as single #
    text = re.sub(
        r'^\s*#+\s*procedure\s*:',
        '# Procedure:',
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    # Standardize section headers to ###
    replacements = {
        "purpose": "### Purpose",
        "parameters": "### Parameters",
        "logic flow": "### Logic Flow",
        "data interactions": "### Data Interactions",
    }

    for key, replacement in replacements.items():
        text = re.sub(
            rf'^\s*#+\s*{re.escape(key)}\b.*$',
            replacement,
            text,
            flags=re.IGNORECASE | re.MULTILINE,
        )

    # Ensure exactly one blank line before each major section header
    text = re.sub(
        r'\n{0,1}(###\s+(?:Purpose|Parameters|Logic Flow|Data Interactions)\b)',
        r'\n\n\1',
        text,
        flags=re.IGNORECASE,
    )

    # Ensure procedure title is followed by a blank line
    text = re.sub(
        r'^(#\s*Procedure:.*)\n+(###\s+Purpose\b)',
        r'\1\n\n\2',
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    # Collapse excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.rstrip()

def strip_global_context_and_below(text: str) -> str:
    if not text:
        return text

    text = re.sub(
        r'\n+#+\s*GLOBAL\s+CONTEXT\b.*$',
        '',
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    return text.rstrip()

# --- 1. CLEANER ---
def clean_response(text: str) -> str:
    text = text or ""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    text = re.sub(r"```[a-zA-Z]*\n?", "", text)
    text = re.sub(
        r"^\s*(Okay|Sure|Here is|Let me|I have|Below is).*?\n",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\n*(Do you want me to .*|Would you like me to .*|Let me know if .*|I can also .*?)\s*$",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return text.strip()


def extract_expected_procedure_name(prompt_text: str) -> str:
    m = re.search(r"#\s*Procedure\s*:\s*(.+)", prompt_text, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return "Unknown_Procedure"


def enforce_sql_template(text: str, expected_proc_name: str) -> str:
    text = (text or "").strip()
    if not re.search(r"^\s*#\s*Procedure\s*:", text, flags=re.IGNORECASE | re.MULTILINE):
        text = f"# Procedure: {expected_proc_name}\n\n" + text
    return text


def detect_excessive_duplicate_lines(text, min_line_len=25, duplicate_threshold=6, dominance_threshold=0.35):
    raw_lines = [ln.strip() for ln in (text or "").splitlines()]
    raw_lines = [ln for ln in raw_lines if ln and len(ln) >= min_line_len]

    if not raw_lines:
        return False, "No meaningful lines"

    normalized = []
    for ln in raw_lines:
        ln2 = re.sub(r'^\s*(?:\d+[\.\)]\s*|[-*]\s+)', '', ln).strip()
        normalized.append(ln2)

    counts = Counter(normalized)
    _, most_common_count = counts.most_common(1)[0]

    if most_common_count >= duplicate_threshold:
        return True, f"Repeated normalized line detected {most_common_count} times"

    duplicated_total = sum(c for _, c in counts.items() if c > 1)
    if duplicated_total / len(normalized) > dominance_threshold:
        return True, f"Too many duplicated normalized lines ({duplicated_total}/{len(normalized)})"

    return False, "OK"

def detect_repeated_line_chunks(text: str, window_size: int = 3, repeat_threshold: int = 3):
    lines = [ln.strip() for ln in (text or "").splitlines()]
    lines = [ln for ln in lines if ln]

    if len(lines) < window_size * 2:
        return False, "Not enough lines for chunk check"

    normalized = []
    for ln in lines:
        ln = re.sub(r'^\s*(?:\d+[\.\)]\s*|[-*]\s+)', '', ln).strip()
        ln = re.sub(r'\s+', ' ', ln)
        normalized.append(ln)

    chunks = []
    for i in range(len(normalized) - window_size + 1):
        chunk = "\n".join(normalized[i:i + window_size])
        chunks.append(chunk)

    counts = Counter(chunks)
    most_common_chunk, most_common_count = counts.most_common(1)[0]

    if most_common_count >= repeat_threshold:
        return True, f"Repeated line chunk detected {most_common_count} times"

    return False, "OK"

def detect_duplicate_table_rows(text, threshold=6):
    rows = re.findall(r"^\|.*\|$", text or "", flags=re.MULTILINE)
    rows = [r.strip() for r in rows if ":---" not in r]

    if not rows:
        return False, "No table rows"

    counts = Counter(rows)
    _, worst_count = counts.most_common(1)[0]
    if worst_count >= threshold:
        return True, f"Duplicate table row repeated {worst_count} times"

    return False, "OK"


def contains_template_placeholders(text: str) -> bool:
    text_lower = (text or "").lower()
    placeholder_phrases = [
        "one clear sentence explaining what business task this performs.",
        "Describe the sequence of operations performed in this part of the procedure.",
        "inferred usage",
        "list tables explicitly selected from",
        "list tables inserted/updated/deleted",
        "@paramname",
        "datatype",
        "Step-by-step plain English explanation."
    ]
    return any(p in text_lower for p in placeholder_phrases)


def looks_like_raw_sql(text: str) -> bool:
    text_lower = (text or "").lower()

    if "### raw sql input" in text_lower:
        return True

    # Strong direct indicators
    if re.search(r"\b(?:create|alter)\s+(?:or\s+alter\s+)?(?:proc|procedure)\b", text_lower, flags=re.IGNORECASE):
        return True

    if re.search(r"^\s*begin\s*$", text_lower, flags=re.IGNORECASE | re.MULTILINE) and \
       re.search(r"^\s*end\s*$", text_lower, flags=re.IGNORECASE | re.MULTILINE):
        return True

    sql_patterns = [
        r"\binsert\s+into\s+[#@\[\]\w\.]+\b",
        r"\bupdate\s+[#@\[\]\w\.]+\s+set\b",
        r"\bdelete\s+from\s+[#@\[\]\w\.]+\b",
        r"\bmerge\s+into\s+[#@\[\]\w\.]+\b",
        r"\btruncate\s+table\s+[#@\[\]\w\.]+\b",
        r"\bselect\b[\s\S]{0,300}?\bfrom\s+[#@\[\]\w\.]+\b",
        r"^\s*declare\s+@\w+",
        r"^\s*set\s+nocount\s+on\b",
        r"^\s*exec(?:ute)?\s+\w+",
        r"^\s*with\s*\([^)]+\)",
    ]

    hits = 0
    for pattern in sql_patterns:
        if re.search(pattern, text_lower, flags=re.IGNORECASE | re.MULTILINE):
            hits += 1

    return hits >= 2


def validate_output(text: str):
    text = (text or "").strip()
    text_lower = text.lower()

    if len(text) < 30:
        return False, "Output empty"

    header_patterns = {
    "procedure": r"^\s*#+\s*procedure\s*:",
    "purpose": r"^\s*#+\s*purpose\b",
    "parameters": r"^\s*#+\s*parameters\b",
    "logic flow": r"^\s*#+\s*logic\s*flow\b",
    "data interactions": r"^\s*#+\s*data\s*interactions\b",
    }

    for name, pattern in header_patterns.items():
        if not re.search(pattern, text_lower, flags=re.MULTILINE):
            return False, f"Missing required section: {name}"

    if not re.match(r"^\s*#\s*Procedure\s*:\s*\S+", text, flags=re.IGNORECASE):
        return False, "Missing or invalid procedure title"

    if "| Name | Type | Purpose |" not in text:
        return False, "Missing parameters table"

    if contains_template_placeholders(text):
        return False, "Output still contains template placeholder text"

    tail = text_lower[-400:]
    for p in ["do you want me to", "would you like me to", "let me know if", "i can also"]:
        if p in tail:
            return False, "Detected conversational ending"

    if looks_like_raw_sql(text):
        return False, "Detected raw SQL code"

    if re.search(r"^\s*--", text, flags=re.MULTILINE):
        return False, "Detected SQL-style comments in output"

    proc_titles = re.findall(r"^\s*#\s*Procedure\s*:", text, flags=re.IGNORECASE | re.MULTILINE)
    if len(proc_titles) != 1:
        return False, f"Expected exactly 1 procedure title, found {len(proc_titles)}"

    if re.search(r"(final instruction:|do not write anything before|do not write anything after)", text_lower):
        return False, "Model copied prompt instructions into output"

    dup_bad, dup_reason = detect_excessive_duplicate_lines(text)
    if dup_bad:
        return False, dup_reason

    chunk_bad, chunk_reason = detect_repeated_line_chunks(text)
    if chunk_bad:
        return False, chunk_reason

    table_bad, table_reason = detect_duplicate_table_rows(text)
    if table_bad:
        return False, table_reason

    if len(text) > 300:
        compressed = zlib.compress(text.encode("utf-8"))
        ratio = len(compressed) / len(text)
        if ratio < 0.15:
            return False, f"Gibberish detected (ratio: {ratio:.2f})"

    return True, "Passed"


# --- 2. PART HELPERS ---
def parse_part_info(filename: str):
    m = re.match(r"^(?P<prefix>\d+_[^\.]+?)_part(?P<part>\d+)\.txt$", filename, flags=re.IGNORECASE)
    if not m:
        return None
    base_key = m.group("prefix")
    part_num = int(m.group("part"))
    return base_key, part_num


def summarize_output_for_next_part(text: str, max_logic_steps: int = 4) -> str:
    text = text or ""

    purpose = re.search(r"#+\s*Purpose\s*(.*?)(?=\n#+\s*Parameters)", text, flags=re.IGNORECASE | re.DOTALL)
    params = re.search(r"#+\s*Parameters\s*(.*?)(?=\n#+\s*Logic Flow)", text, flags=re.IGNORECASE | re.DOTALL)
    logic = re.search(r"#+\s*Logic Flow\s*(.*?)(?=\n#+\s*Data Interactions)", text, flags=re.IGNORECASE | re.DOTALL)
    data = re.search(r"#+\s*Data Interactions\s*(.*)$", text, flags=re.IGNORECASE | re.DOTALL)

    logic_lines = []
    if logic:
        for ln in logic.group(1).splitlines():
            cleaned = ln.strip()
            if cleaned:
                logic_lines.append(cleaned)
            if len(logic_lines) >= max_logic_steps:
                break

    parts = ["### PRIOR PART SUMMARY"]
    parts.append("Use this only as earlier context. Do not repeat it unless needed for continuity.")

    if purpose and purpose.group(1).strip():
        parts.append("\nPurpose so far:")
        parts.append(purpose.group(1).strip())

    if params and params.group(1).strip():
        parts.append("\nParameter understanding so far:")
        parts.append(params.group(1).strip())

    if logic_lines:
        parts.append("\nKey logic already established:")
        for ln in logic_lines:
            parts.append(f"- {ln}")

    if data and data.group(1).strip():
        parts.append("\nKnown data interactions so far:")
        parts.append(data.group(1).strip())

    return "\n".join(parts).strip()

def sort_key(filename):
    info = parse_part_info(filename)
    if info:
        base_key, part_num = info
        return (base_key, part_num)
    return (filename, 0)

def inject_prior_summary(prompt_text: str, prior_summary: str) -> str:
    if not prior_summary:
        return prompt_text

    insert_block = (
        f"{prior_summary}\n\n"
        "### PART-SPECIFIC INSTRUCTION\n"
        "Use the prior summary only to understand context from earlier chunks. "
        "Do not re-document the earlier chunk in full. Focus on the current SQL chunk while keeping naming and purpose consistent.\n\n"
    )

    marker = "### RAW SQL INPUT"
    if marker in prompt_text:
        return prompt_text.replace(marker, insert_block + marker, 1)

    return insert_block + prompt_text


# --- 3. OLLAMA HELPERS ---
def _is_port_open(host: str, port: int) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.8)
    try:
        s.connect((host, port))
        s.close()
        return True
    except Exception:
        return False


def ensure_ollama_running(model: str, host: str = "127.0.0.1", port: int = 11434, timeout: int = 30) -> None:
    if _is_port_open(host, port):
        return

    ollama_path = shutil.which("ollama")
    if not ollama_path:
        raise RuntimeError("`ollama` CLI not found on PATH. Install Ollama and ensure `ollama` is available.")

    try:
        subprocess.run([ollama_path, "pull", model], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    except Exception:
        pass

    server_cmds = [["serve"], ["daemon"], ["run", "serve"]]
    for cmd in server_cmds:
        try:
            proc = subprocess.Popen([ollama_path] + cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            continue

        deadline = time.time() + timeout
        while time.time() < deadline:
            if _is_port_open(host, port):
                return
            time.sleep(0.5)

        try:
            proc.terminate()
        except Exception:
            pass

    raise RuntimeError(
        f"Unable to start Ollama server (tried {server_cmds}). Start it manually and ensure it's listening on {host}:{port}."
    )


# --- 4. MAIN ---
def main():
    print("Starting sql_analysis...")
    print(f"Using model: {MODEL_NAME}")
    print(f"SQL prompts input folder: {INPUT_FOLDER}")
    print(f"SQL analysis output folder: {OUTPUT_FOLDER}")

    try:
        ensure_ollama_running(MODEL_NAME)
    except Exception as e:
        print(f"  ⚠️ Ollama not available: {e}")
        print("  Aborting sql_analysis. Start Ollama manually or adjust the helper.")
        return

    if os.path.exists(OUTPUT_FOLDER):
        print(f"Wiping existing folder: {OUTPUT_FOLDER}")
        try:
            shutil.rmtree(OUTPUT_FOLDER)
        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}.")
            return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    llm = Ollama(
        model=MODEL_NAME,
        temperature=0.1,
        num_ctx=8192,
        num_predict=4096,
        stop=["<|eot_id|>", "### SYSTEM ROLE", "### RAW SQL INPUT"],
    )

    if not os.path.isdir(INPUT_FOLDER):
        print(f"No SQL prompt folder found at '{INPUT_FOLDER}'. Skipping sql_analysis.")
        return

    files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".txt")]

    files.sort(key=sort_key)
    if not files:
        print(f"No SQL prompt files found in '{INPUT_FOLDER}'. Skipping sql_analysis.")
        return

    prior_part_summaries = {}

    for filename in files:
        output_filename = filename.replace(".txt", ".md")
        out_path = os.path.join(OUTPUT_FOLDER, output_filename)

        if os.path.exists(out_path):
            print(f"Skipping {filename} (Done)")
            continue

        print(f"\nProcessing {filename}...")
        with open(os.path.join(INPUT_FOLDER, filename), "r", encoding="utf-8") as f:
            original_prompt = f.read()

        expected_proc_name = extract_expected_procedure_name(original_prompt)
        part_info = parse_part_info(filename)
        current_prompt = original_prompt

        if part_info:
            base_key, part_num = part_info
            if part_num > 1 and base_key in prior_part_summaries:
                current_prompt = inject_prior_summary(original_prompt, prior_part_summaries[base_key])
                print(f"  ↪ Injected summary from previous part for {base_key}.")

        final_output = ""
        success = False

        for attempt in range(1, MAX_RETRIES + 1):
            print(f"  > Attempt {attempt}/{MAX_RETRIES}...", end="", flush=True)
            raw_buffer = ""

            try:
                for chunk in llm.stream(current_prompt):
                    print(chunk, end="", flush=True)   # live streaming output
                    raw_buffer += chunk
                print("\n")

            except Exception as e:
                print(f"\n  💥 Error: {e}")
                raw_buffer = ""
            
            cleaned = clean_response(raw_buffer)
            #print(raw_buffer)
            #print(cleaned)
            cleaned = strip_global_context_and_below(cleaned)
            cleaned = enforce_sql_template(cleaned, expected_proc_name)
            cleaned = standardize_sql_headings(cleaned)
            is_valid, reason = validate_output(cleaned)

            if is_valid:
                print("  ✅ PASS")
                cleaned = standardize_sql_headings(cleaned)
                final_output = cleaned
                success = True
                break

            print(f"  ❌ FAIL: {reason}")
            current_prompt = f"""
### 🛑 CRITICAL INSTRUCTION
Your previous output failed because: {reason}

Return ONLY a completed document with these headings and real content.
Do NOT repeat instruction text under any heading.

Required headings:
# Procedure: {expected_proc_name}

### Purpose
Write one sentence describing what this chunk contributes to the procedure.

### Parameters
Provide a markdown table with actual parameter meanings.

### Logic Flow
Describe the main processing steps performed in this chunk.
Write them in order.

### Data Interactions
List actual reads and writes found in this chunk.

### Error Handling


Rules:
- Do not write SQL
- Do not use SQL comments like --
- Do not include a RAW SQL INPUT section
- Describe behavior in plain language only.
- Do not add introductions
- Do not add conclusions
- Do not ask follow-up questions
- Do not write anything after the Data Interactions section
- Do not copy instruction text into the answer
- Do not include phrases like:
  - One clear sentence explaining what business task this performs.
  - Step-by-step plain English explanation.
  - Inferred usage
  - List tables explicitly selected from
  - List tables inserted/updated/deleted
- Replace all placeholder text with actual inferred content from the SQL
- If prior summary is present, use it only for continuity and do not repeat it unnecessarily

### SOURCE PROMPT
{current_prompt}
"""

        if not success:
            print(f"  ! ABORTING {filename}")
            final_output = f"""# Procedure: {expected_proc_name}

### Purpose
Generation failed validation after {MAX_RETRIES} attempts.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |

### Logic Flow
Could not reliably generate a compliant summary for this procedure.

### Data Interactions
* **Reads:** Unknown
* **Writes:** Unknown
* **Joins:** Unknown

### Error Handling
Unknown
"""

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_output)

        if part_info and success:
            base_key, _ = part_info
            prior_part_summaries[base_key] = summarize_output_for_next_part(final_output)

        print(f"  Saved: {out_path}")

    print("\nsql_analysis: DONE")


if __name__ == "__main__":
    main()