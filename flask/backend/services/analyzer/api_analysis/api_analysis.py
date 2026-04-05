import os
import re
import zlib
import shutil
import subprocess
import time
import socket
from langchain_community.llms import Ollama
from collections import Counter
from urllib.parse import urlparse

# --- CONFIGURATION ---
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))                         # flask/backend/services/analyzer/api_analysis
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))       # flask/backend

PROMPTS_INPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")                # flask/backend/prompts_output
ANALYSIS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "analysis_output")              # flask/backend/analysis_output

INPUT_FOLDER = os.path.join(PROMPTS_INPUT_BASE, "API_Documentation_Prompts")
OUTPUT_FOLDER = os.path.join(ANALYSIS_OUTPUT_BASE, "Final_API_Docs")

DEFAULT_MODEL = "gemma3:latest"
MODEL_NAME = os.environ.get("ANALYSIS_MODEL", DEFAULT_MODEL)
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
MAX_RETRIES = 3
MIN_ENTROPY_RATIO = 0.12
MIN_ENTROPY_LENGTH = 300


# --- CLEANER ---
def clean_response(text: str) -> str:
    if not text:
        return ""

    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
    text = re.sub(r"\n```$", "", text)

    lines = text.splitlines()
    leading_patterns = [
        r"^(Based on|I have|The provided|Okay|Sure|Here is|Below is|Let me|The following).*?(\.|:)?\s*$",
        r"^.*?(generated|documentation|analysis).*?:\s*$",
    ]
    max_head = min(8, len(lines))
    remove_count = 0
    for i in range(max_head):
        line = lines[i].strip()
        if any(re.match(p, line, flags=re.IGNORECASE) for p in leading_patterns):
            remove_count += 1
        else:
            break
    if remove_count > 0:
        lines = lines[remove_count:]

    text = "\n".join(lines)

    text = re.sub(
        r"\n*(I hope this helps|Let me know.*|Feel free to ask.*|Do you want me to.*|Would you like me to.*|I can also.*)\s*$",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    return text.strip()


def normalize_api_purpose_body(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n").strip()

    # Remove markdown heading if model included it
    text = re.sub(r"(?im)^\s*###\s*Purpose\s*&\s*Behaviour\s*$\n?", "", text).strip()

    # Remove plain repeated label if model included it as body text
    text = re.sub(r"(?im)^\s*Purpose\s*&\s*Behaviour\s*$\n?", "", text).strip()

    # Remove accidental repeated copies at the top
    text = re.sub(
        r"(?im)^(This endpoint.*?\.)\s*\n+\1\s*$",
        r"\1",
        text,
    ).strip()

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def extract_expected_field(prompt_text: str, field_name: str) -> str:
    m = re.search(
        rf"(?im)^\*\*{re.escape(field_name)}:\*\*[ \t]*([^\n]*)$",
        prompt_text,
    )
    return m.group(1).strip() if m else ""


def extract_parameters_table(prompt_text: str) -> str:
    m = re.search(
        r"(?is)###\s*PARAMETERS TABLE\s*(\|.*?)(?=^\s*###\s|\Z)",
        prompt_text,
        flags=re.MULTILINE,
    )
    if not m:
        return "| Name | Type |\n| :--- | :--- |\n| (none) | |"

    table = m.group(1).strip()
    return table if table else "| Name | Type |\n| :--- | :--- |\n| (none) | |"


def extract_expected_endpoint_title(prompt_text: str) -> str:
    m = re.search(r"(?im)^\*\*EndpointTitle:\*\*[ \t]*([^\n]+)$", prompt_text)
    if m:
        return m.group(1).strip()

    m = re.search(r"(?im)^#\s*API Endpoint:\s*([^\n]+)$", prompt_text)
    if m:
        return m.group(1).strip()

    return "Unknown_Endpoint"


def build_injected_api_output(body_text: str, fields: dict) -> str:
    body_text = (body_text or "").strip()

    # remove any model-generated copies
    patterns = [
        r"(?im)^\s*#\s*API Endpoint\s*:.*$\n?",
        r"(?im)^\s*\|[ \t]*Field[ \t]*\|[ \t]*Value[ \t]*\|\s*$\n?",
        r"(?im)^\s*\|[-| :]+\|\s*$\n?",
        r"(?im)^\s*\|[ \t]*Kind[ \t]*\|.*$\n?",
        r"(?im)^\s*\|[ \t]*Controller / Service[ \t]*\|.*$\n?",
        r"(?im)^\s*\|[ \t]*Operation[ \t]*\|.*$\n?",
        r"(?im)^\s*\|[ \t]*Source File[ \t]*\|.*$\n?",
        r"(?im)^\s*\|[ \t]*Route[ \t]*\|.*$\n?",
        r"(?im)^\s*\|[ \t]*HTTP Methods[ \t]*\|.*$\n?",
        r"(?is)^\s*###\s*Parameters\b.*?(?=^\s*###\s*Return Type\b|^\s*###\s*Purpose\s*&\s*Behaviour\b|\Z)",
        r"(?is)^\s*###\s*Return Type\b.*?(?=^\s*###\s*Purpose\s*&\s*Behaviour\b|\Z)",
    ]
    for pat in patterns:
        body_text = re.sub(pat, "", body_text, flags=re.MULTILINE | re.DOTALL)

    body_text = normalize_api_purpose_body(body_text)
    if not body_text:
        body_text = "Purpose unknown — insufficient metadata."

    body_text = f"### Purpose & Behaviour\n{body_text}"

    header = f"""# API Endpoint: {fields['endpoint_title']}

| Field | Value |
|------|------|
| Kind | {fields['kind']} |
| Controller / Service | {fields['controller']} |
| Operation | {fields['operation']} |
| Source File | {fields['source_file']} |
| Route | {fields['route']} |
| HTTP Methods | {fields['http_methods']} |

### Parameters
{fields['parameters_table']}

### Return Type
{fields['return_type']}
"""

    return f"{header}\n\n{body_text}".strip()


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
    rows = re.findall(r"^\s*\|.*\|\s*$", text or "", flags=re.MULTILINE)
    rows = [r.strip() for r in rows if ":---" not in r and "------" not in r]

    if not rows:
        return False, "No table rows"

    counts = Counter(rows)
    _, worst_count = counts.most_common(1)[0]

    if worst_count >= threshold:
        return True, f"Duplicate table row repeated {worst_count} times"

    return False, "OK"


def natural_sort_key(filename: str):
    stem = os.path.splitext(filename)[0]
    parts = re.split(r"(\d+)", stem.lower())
    return [int(p) if p.isdigit() else p for p in parts]


# --- VALIDATOR ---
def validate_output(text: str):
    text = (text or "").strip()
    text_lower = text.lower()

    if len(text) < 30:
        return False, "Output was empty or too short."

    required_headers = [
        "# api endpoint:",
        "| field | value |",
        "| kind |",
        "| controller / service |",
        "| operation |",
        "| source file |",
        "| route |",
        "| http methods |",
        "### parameters",
        "### return type",
        "### purpose & behaviour",
    ]

    for h in required_headers:
        if h not in text_lower:
            return False, f"Missing required section: {h}"

    if not re.match(r"^\s*#\s*API Endpoint\s*:\s*\S+", text, flags=re.IGNORECASE):
        return False, "Missing or invalid API endpoint title"

    if "| Name | Type |" not in text:
        return False, "Missing parameters table"

    if re.search(r"(instruction:|raw endpoint metadata|source metadata|do not write anything before|do not write anything after|end of input)", text_lower):
        return False, "Model copied prompt instructions into output"

    if any(x in text_lower for x in ["```csharp", "```cs", "```sql", "```vb", "```json", "```"]):
        return False, "Detected code block in output"

    forbidden = ["public partial class", "protected void", "private void"]
    for kw in forbidden:
        if kw in text_lower:
            return False, f"Detected code keyword: '{kw}'"

    tail = text_lower[-400:]
    for p in ["do you want me to", "would you like me to", "let me know if", "i can also"]:
        if p in tail:
            return False, "Detected conversational ending"

    dup_bad, dup_reason = detect_excessive_duplicate_lines(text)
    if dup_bad:
        return False, dup_reason

    table_bad, table_reason = detect_duplicate_table_rows(text)
    if table_bad:
        return False, table_reason

    if len(text) > MIN_ENTROPY_LENGTH:
        compressed = zlib.compress(text.encode("utf-8"))
        ratio = len(compressed) / len(text)
        if ratio < MIN_ENTROPY_RATIO:
            return False, f"Detected repetitive content (entropy: {ratio:.2f})"

    return True, "Passed"


# --- Ollama helpers ---
def _is_port_open(host: str, port: int) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.8)
    try:
        s.connect((host, port))
        s.close()
        return True
    except Exception:
        return False


def ensure_ollama_running(model: str) -> None:
    base_url = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
    parsed = urlparse(base_url)

    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or 11434

    if _is_port_open(host, port):
        return

    ollama_path = shutil.which("ollama")
    if not ollama_path:
        raise RuntimeError(
            "`ollama` CLI not found on PATH. Install Ollama and ensure `ollama` is available."
        )

    try:
        subprocess.run(
            [ollama_path, "pull", model],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False
        )
    except Exception:
        pass

    server_cmds = [["serve"], ["daemon"], ["run", "serve"]]

    for cmd in server_cmds:
        try:
            proc = subprocess.Popen(
                [ollama_path] + cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except FileNotFoundError:
            continue

        deadline = time.time() + 30

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

    if not os.path.isdir(INPUT_FOLDER):
        print(f"No API prompt folder found at '{INPUT_FOLDER}'. Skipping api_analysis.")
        return

    files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(".txt")]
    files.sort(key=natural_sort_key)

    if not files:
        print(f"No API prompt files found in '{INPUT_FOLDER}'. Skipping api_analysis.")
        return

    try:
        ensure_ollama_running(MODEL_NAME)
    except Exception as e:
        print(f"  ⚠️ Ollama not available: {e}")
        print("  Aborting api_analysis. Start Ollama manually or adjust the helper.")
        return

    llm = Ollama(
        model=MODEL_NAME,
        #base_url=OLLAMA_BASE_URL,
        temperature=0.1,
        num_ctx=8192,
        num_predict=4096,
        stop=["<|eot_id|>", "### SYSTEM ROLE", "### END OF INPUT"]
    )

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

        print(f"\n  Processing {filename}...")
        with open(os.path.join(INPUT_FOLDER, filename), "r", encoding="utf-8") as f:
            original_prompt = f.read()

        endpoint_title = extract_expected_endpoint_title(original_prompt)
        kind = extract_expected_field(original_prompt, "Kind") or "Not specified"
        controller = extract_expected_field(original_prompt, "Controller / Service") or "Not specified"
        operation = extract_expected_field(original_prompt, "Operation") or "Not specified"
        source_file = extract_expected_field(original_prompt, "Source File") or "Not specified"
        route = extract_expected_field(original_prompt, "Route") or "Not specified"
        http_methods = extract_expected_field(original_prompt, "HTTP Methods") or "Not specified"
        return_type = extract_expected_field(original_prompt, "Return Type") or "Not specified"
        parameters_table = extract_parameters_table(original_prompt)

        fields = {
            "endpoint_title": endpoint_title,
            "kind": kind,
            "controller": controller,
            "operation": operation,
            "source_file": source_file,
            "route": route,
            "http_methods": http_methods,
            "return_type": return_type,
            "parameters_table": parameters_table,
        }

        current_prompt = original_prompt
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
            cleaned = normalize_api_purpose_body(cleaned)

            if not cleaned:
                cleaned = "Purpose unknown — insufficient metadata."

            cleaned = build_injected_api_output(cleaned, fields)
            is_valid, reason = validate_output(cleaned)

            if is_valid:
                print("  ✅ PASS")
                final_output = cleaned
                success = True
                break

            print(f"  ❌ FAIL: {reason}")
            current_prompt = f"""
### VALIDATION FAILURE
Your previous output failed because: {reason}

Return ONLY:

### Purpose & Behaviour
One short paragraph explaining what the endpoint does in plain English based only on the provided metadata, including parameters and return type.
If unknown, write exactly:
Purpose unknown — insufficient metadata.

Rules:
- Do not output title, tables, parameters, return type, file, route, or HTTP methods
- Do not repeat the heading twice
- Do not write code
- Do not write JSON
- Do not add introductions
- Do not add conclusions
- Do not ask follow-up questions

### SOURCE PROMPT
{original_prompt}
""".strip()

        if not success:
            print(f"  ! ABORTING {filename}")
            final_output = build_injected_api_output(
                f"Generation failed validation after {MAX_RETRIES} attempts.",
                fields,
            )

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_output)

        print(f"  Saved: {out_path}")

    print("\napi_analysis: DONE")


if __name__ == "__main__":
    main()