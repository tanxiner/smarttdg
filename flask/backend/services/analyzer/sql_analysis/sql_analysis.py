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
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))            # flask/backend/services/analyzer/sql_analysis
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))  # flask/backend
PROMPTS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")
ANALYSIS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "analysis_output")

INPUT_FOLDER = os.path.join(PROMPTS_OUTPUT_BASE, "SQL_Documentation_Prompts")
OUTPUT_FOLDER = os.path.join(ANALYSIS_OUTPUT_BASE, "Final_SQL_Docs")

DEFAULT_MODEL = "gemma3:latest"
MODEL_NAME = os.environ.get("ANALYSIS_MODEL", DEFAULT_MODEL)
MAX_RETRIES = 5


# --- 1. CLEANER ---
def clean_response(text: str) -> str:
    text = text or ""

    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    text = re.sub(r'^```[a-zA-Z]*\n', '', text)
    text = re.sub(r'\n```$', '', text)

    # remove common opening filler
    text = re.sub(
        r'^\s*(Okay|Sure|Here is|Let me|I have|Below is).*?\n',
        '',
        text,
        flags=re.IGNORECASE
    )

    # remove trailing conversational prompts
    text = re.sub(
        r'\n*(Do you want me to .*|Would you like me to .*|Let me know if .*|I can also .*?)\s*$',
        '',
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    return text.strip()


def extract_expected_procedure_name(prompt_text: str) -> str:
    m = re.search(r'#\s*Procedure\s*:\s*(.+)', prompt_text, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return "Unknown_Procedure"


def enforce_sql_template(text: str, expected_proc_name: str) -> str:
    text = (text or "").strip()

    if not re.search(r'^\s*#\s*Procedure\s*:', text, flags=re.IGNORECASE | re.MULTILINE):
        text = f"# Procedure: {expected_proc_name}\n\n" + text

    return text


def detect_excessive_duplicate_lines(text, min_line_len=25, duplicate_threshold=8, dominance_threshold=0.35):
    lines = [ln.strip() for ln in (text or "").splitlines()]
    lines = [ln for ln in lines if ln and len(ln) >= min_line_len]

    if not lines:
        return False, "No meaningful lines"

    counts = Counter(lines)
    _, most_common_count = counts.most_common(1)[0]

    if most_common_count >= duplicate_threshold:
        return True, f"Repeated line detected {most_common_count} times"

    duplicated_total = sum(c for _, c in counts.items() if c > 1)
    if duplicated_total / len(lines) > dominance_threshold:
        return True, f"Too many duplicated lines ({duplicated_total}/{len(lines)})"

    return False, "OK"


def detect_duplicate_table_rows(text, threshold=6):
    rows = re.findall(r'^\|.*\|$', text or "", flags=re.MULTILINE)
    rows = [r.strip() for r in rows if ':---' not in r]

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
        "step-by-step plain english explanation.",
        "inferred usage",
        "list tables explicitly selected from",
        "list tables inserted/updated/deleted",
        "@paramname",
        "datatype",
    ]

    return any(p in text_lower for p in placeholder_phrases)


# --- 2. SQL VALIDATOR ---
def validate_output(text: str):
    text = (text or "").strip()
    text_lower = text.lower()

    if len(text) < 30:
        return False, "Output empty"

    required_headers = [
        "# procedure:",
        "### purpose",
        "### parameters",
        "### logic flow",
        "### data interactions",
    ]

    for h in required_headers:
        if h not in text_lower:
            return False, f"Missing required section: {h}"

    if not re.match(r'^\s*#\s*Procedure\s*:\s*\S+', text, flags=re.IGNORECASE):
        return False, "Missing or invalid procedure title"

    if "| Name | Type | Purpose |" not in text:
        return False, "Missing parameters table"

    if contains_template_placeholders(text):
        return False, "Output still contains template placeholder text"

    banned_tail_patterns = [
        "do you want me to",
        "would you like me to",
        "let me know if",
        "i can also",
    ]
    tail = text_lower[-400:]
    for p in banned_tail_patterns:
        if p in tail:
            return False, "Detected conversational ending"

    # raw SQL leakage
    if "create procedure" in text_lower or "create proc" in text_lower:
        if "set nocount on" in text_lower or "as\nbegin" in text_lower or "alter procedure" in text_lower:
            return False, "Detected raw SQL code"

    # reject SQL-style comment prose
    if re.search(r'^\s*--', text, flags=re.MULTILINE):
        return False, "Detected SQL-style comments in output"

    # only one procedure document per file
    proc_titles = re.findall(r'^\s*#\s*Procedure\s*:', text, flags=re.IGNORECASE | re.MULTILINE)
    if len(proc_titles) != 1:
        return False, f"Expected exactly 1 procedure title, found {len(proc_titles)}"

    # copied prompt instructions
    if re.search(r'(final instruction:|do not write anything before|do not write anything after)', text_lower):
        return False, "Model copied prompt instructions into output"

    # repeated lines / rows
    dup_bad, dup_reason = detect_excessive_duplicate_lines(text)
    if dup_bad:
        return False, dup_reason

    table_bad, table_reason = detect_duplicate_table_rows(text)
    if table_bad:
        return False, table_reason

    # entropy / repetition
    if len(text) > 300:
        compressed = zlib.compress(text.encode("utf-8"))
        ratio = len(compressed) / len(text)
        if ratio < 0.15:
            return False, f"Gibberish detected (ratio: {ratio:.2f})"

    return True, "Passed"


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
        f"Unable to start Ollama server (tried {server_cmds}). "
        f"Start it manually and ensure it's listening on {host}:{port}."
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
        stop=["<|eot_id|>", "### SYSTEM ROLE", "### ⬇️ RAW SQL INPUT ⬇️"]
    )

    if not os.path.isdir(INPUT_FOLDER):
        print(f"No SQL prompt folder found at '{INPUT_FOLDER}'. Skipping sql_analysis.")
        return

    files = sorted([f for f in os.listdir(INPUT_FOLDER) if f.endswith(".txt")])

    if not files:
        print(f"No SQL prompt files found in '{INPUT_FOLDER}'. Skipping sql_analysis.")
        return

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
        current_prompt = original_prompt
        final_output = ""
        success = False
        cleaned = ""
        raw_buffer = ""

        for attempt in range(1, MAX_RETRIES + 1):
            print(f"  > Attempt {attempt}/{MAX_RETRIES}...", end="", flush=True)
            raw_buffer = ""

            try:
                for chunk in llm.stream(current_prompt):
                    print(chunk, end="", flush=True)
                    raw_buffer += chunk
                print("\n")
            except Exception as e:
                print(f"\n  💥 Error: {e}")
                raw_buffer = ""

            cleaned = clean_response(raw_buffer)
            cleaned = enforce_sql_template(cleaned, expected_proc_name)
            is_valid, reason = validate_output(cleaned)

            if is_valid:
                print("  ✅ PASS")
                final_output = cleaned
                success = True
                break
            else:
                print(f"  ❌ FAIL: {reason}")
                current_prompt = f"""
### 🛑 CRITICAL INSTRUCTION
Your previous output failed because: {reason}

Return ONLY this exact format:

# Procedure: {expected_proc_name}

### Purpose
One clear sentence explaining what business task this performs.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | Inferred usage |

### Logic Flow
Step-by-step plain English explanation.

### Data Interactions
* **Reads:** List tables explicitly selected from
* **Writes:** List tables inserted/updated/deleted

Rules:
- Do not write SQL
- Do not use SQL comments like --
- Do not add introductions
- Do not add conclusions
- Do not ask follow-up questions
- Do not write anything after the Data Interactions section
- Do not copy the template wording literally
- Replace all placeholder text with actual inferred content from the SQL

### SOURCE PROMPT
{original_prompt}
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
"""

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_output)

        print(f"  Saved: {out_path}")

    print("\nsql_analysis: DONE")


if __name__ == "__main__":
    main()