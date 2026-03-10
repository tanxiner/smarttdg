import os
import re
import zlib
import shutil
import subprocess
import time
import socket
from langchain_community.llms import Ollama
from collections import Counter

# --- CONFIGURATION ---
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))                         # flask/backend/services/analyzer/api_analysis
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))       # flask/backend

PROMPTS_INPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")                # flask/backend/prompts_output
ANALYSIS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "analysis_output")              # flask/backend/analysis_output

INPUT_FOLDER = os.path.join(PROMPTS_INPUT_BASE, "API_Documentation_Prompts")
OUTPUT_FOLDER = os.path.join(ANALYSIS_OUTPUT_BASE, "Final_API_Docs")

DEFAULT_MODEL = "gemma3:latest"
MODEL_NAME = os.environ.get("ANALYSIS_MODEL", DEFAULT_MODEL)
MAX_RETRIES = 3
MIN_ENTROPY_RATIO = 0.12
MIN_ENTROPY_LENGTH = 300


# --- CLEANER ---
def clean_response(text):
    if not text:
        return text
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    text = re.sub(r'^```[a-zA-Z]*\n', '', text)
    text = re.sub(r'\n```$', '', text)

    lines = text.splitlines()
    leading_patterns = [
        r'^(Based on|I have|This endpoint|The provided).*?(\.|:)\s*$',
        r'^(Okay|Sure|Here is|Let me|Below is|The following).*?(\:)?\s*$',
        r'^.*?(generated|documentation|analysis).*?:\s*$'
    ]
    max_head = min(8, len(lines))
    remove_count = 0
    for i in range(max_head):
        line = lines[i].strip()
        matched = any(re.match(p, line, flags=re.IGNORECASE) for p in leading_patterns)
        if matched:
            remove_count += 1
        else:
            break
    if remove_count > 0:
        lines = lines[remove_count:]

    text = "\n".join(lines)

    text = re.sub(
        r'\n*(I hope this helps|Let me know.*|Feel free to ask.*|Do you want me to.*|Would you like me to.*|I can also.*)\s*$',
        '',
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    return text.strip()

def extract_expected_endpoint_title(prompt_text: str) -> str:
    m = re.search(r'#\s*API Endpoint:\s*(.+)', prompt_text, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return "Unknown_Endpoint"

def enforce_api_template(text: str, expected_title: str) -> str:
    text = (text or "").strip()

    if not re.search(r'^\s*#\s*API Endpoint\s*:', text, flags=re.IGNORECASE | re.MULTILINE):
        text = f"# API Endpoint: {expected_title}\n\n" + text

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

# --- VALIDATOR ---
def validate_output(text):
    text = (text or "").strip()
    text_lower = text.lower()

    if len(text) < 30:
        return False, "Output was empty or too short."

    required_headers = [
        "# api endpoint:",
        "**kind:**",
        "**controller / service:**",
        "**operation:**",
        "**source file:**",
        "**route:**",
        "**http methods:**",
        "### parameters",
        "### return type",
        "### purpose & behaviour",
    ]

    for h in required_headers:
        if h not in text_lower:
            return False, f"Missing required section: {h}"

    if not re.match(r'^\s*#\s*API Endpoint\s*:\s*\S+', text, flags=re.IGNORECASE):
        return False, "Missing or invalid API endpoint title"

    if "| Name | Type |" not in text:
        return False, "Missing parameters table"

    # reject copied prompt instructions
    if re.search(r'(instruction:|raw endpoint metadata|do not write anything before|do not write anything after)', text_lower):
        return False, "Model copied prompt instructions into output"

    # code block checks
    if "```csharp" in text_lower or "```cs" in text_lower or "```sql" in text_lower or "```vb" in text_lower or "```json" in text_lower:
        return False, "Detected code block in output"

    forbidden = ["public partial class", "protected void", "private void"]
    for kw in forbidden:
        if kw in text_lower:
            return False, f"Detected code keyword: '{kw}'"

    # conversational ending
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

    # duplicate line check
    dup_bad, dup_reason = detect_excessive_duplicate_lines(text)
    if dup_bad:
        return False, dup_reason

    # duplicate table row check
    table_bad, table_reason = detect_duplicate_table_rows(text)
    if table_bad:
        return False, table_reason

    # entropy check
    if len(text) > MIN_ENTROPY_LENGTH:
        compressed = zlib.compress(text.encode("utf-8"))
        ratio = len(compressed) / len(text)
        if ratio < MIN_ENTROPY_RATIO:
            return False, f"Detected repetitive content (entropy: {ratio:.2f})"

    return True, "Passed"

# --- Ollama helpers (mirrors sql_analysis.py) ---
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


def main():
    print("Starting api_analysis...")
    print(f"Using model: {MODEL_NAME}")
    print(f"API prompts input folder: {INPUT_FOLDER}")
    print(f"API analysis output folder: {OUTPUT_FOLDER}")

    # If no prompts folder exists, there are no API endpoints to document
    if not os.path.isdir(INPUT_FOLDER):
        print(f"No API prompt folder found at '{INPUT_FOLDER}'. Skipping api_analysis.")
        return

    files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(".txt")]
    files.sort(key=str.lower)

    if not files:
        print(f"No API prompt files found in '{INPUT_FOLDER}'. Skipping api_analysis.")
        return

    # Ensure Ollama is available
    try:
        ensure_ollama_running(MODEL_NAME)
    except Exception as e:
        print(f"  ⚠️ Ollama not available: {e}")
        print("  Aborting api_analysis. Start Ollama manually or adjust the helper.")
        return

    llm = Ollama(
        model=MODEL_NAME,
        temperature=0.1,
        num_ctx=8192,
        num_predict=4096,
        stop=["<|eot_id|>", "### SYSTEM ROLE", "### ⬇️ RAW ENDPOINT METADATA ⬇️"]
    )

    # Prepare output folder
    if os.path.exists(OUTPUT_FOLDER):
        print(f"Wiping existing folder: {OUTPUT_FOLDER}")
        try:
            shutil.rmtree(OUTPUT_FOLDER)
        except OSError as e:
            print(f"Error removing {OUTPUT_FOLDER}: {e}")
            return
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for filename in files:
        output_filename = filename.replace(".txt", ".md")
        out_path = os.path.join(OUTPUT_FOLDER, output_filename)
        if os.path.exists(out_path):
            print(f"  Skipping {filename} (Done)")
            continue

        print(f"\n  Processing {filename}...")
        with open(os.path.join(INPUT_FOLDER, filename), "r", encoding="utf-8") as f:
            original_prompt = f.read()

        current_prompt = original_prompt
        expected_endpoint_title = extract_expected_endpoint_title(original_prompt)
        final_output = ""
        success = False

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
            cleaned = enforce_api_template(cleaned, expected_endpoint_title)
            is_valid, reason = validate_output(cleaned)

            if is_valid:
                print("  ✅ PASS")
                final_output = cleaned
                success = True
                break
            else:
                print(f"  ❌ FAIL: {reason}")

                current_prompt = f"""
### VALIDATION FAILURE
Your previous output failed because: {reason}

You must now return ONLY this exact structure:

# API Endpoint: {expected_endpoint_title}

**Kind:** value
**Controller / Service:** value
**Operation:** value
**Source File:** value
**Route:** value
**HTTP Methods:** value

### Parameters
| Name | Type |
| :--- | :--- |
| parameter | type |

### Return Type
value

### Purpose & Behaviour
Describe what this endpoint does in plain English based only on the provided metadata.
If unknown, write: Purpose unknown — insufficient metadata.

Rules:
- Do not write code
- Do not write JSON
- Do not add introductions
- Do not add conclusions
- Do not ask follow-up questions
- Do not write anything after the Purpose & Behaviour section

### SOURCE PROMPT
{original_prompt}
"""

        if not success:
            print(f"  ! ABORTING {filename}")
            final_output = f"""# API Endpoint: {expected_endpoint_title}

**Kind:** Not specified
**Controller / Service:** Not specified
**Operation:** Not specified
**Source File:** Not specified
**Route:** Not specified
**HTTP Methods:** Not specified

### Parameters
| Name | Type |
| :--- | :--- |
| (none) | |

### Return Type
Not specified

### Purpose & Behaviour
Generation failed validation after {MAX_RETRIES} attempts.
"""

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_output)
        print(f"  Saved: {out_path}")

    print("\napi_analysis: DONE")


if __name__ == "__main__":
    main()
