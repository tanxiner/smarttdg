import os
import re
import zlib
import textwrap
import shutil
import subprocess
import time
import socket
from langchain_community.llms import Ollama
from collections import Counter

# --- CONFIGURATION ---
INPUT_OUTPUT_PAIRS = [
    ("Page_Documentation_Prompts", "Final_Documentation_Chapters"),
    ("Utility_Documentation_Prompts", "Final_Utility_Chapters"),
]
DEFAULT_MODEL = "gemma3:latest"
MODEL_NAME = os.environ.get("ANALYSIS_MODEL", DEFAULT_MODEL)
MAX_RETRIES = 5

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
PROMPTS_INPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")
ANALYSIS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "analysis_output")


def remove_raw_input_block(text: str) -> str:
    marker = re.search(r'RAW INPUT', text, flags=re.IGNORECASE)
    if marker:
        return text[:marker.start()].rstrip()
    return text


def clean_response(text):
    if not text:
        return text

    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    text = re.sub(r'^```[a-zA-Z]*\n', '', text)
    text = re.sub(r'\n```$', '', text)

    lines = text.splitlines()
    cleaned_lines = list(lines)

    leading_patterns = [
        r'^(Based on|I have|This page|The provided|Okay|Sure|Here is|Let me|Below is|The following).*?(\.|:)?\s*$',
        r'^.*?(generated|documentation|analysis).*?:\s*$'
    ]

    max_head_lines = min(8, len(lines))
    remove_count = 0
    for i in range(max_head_lines):
        line = lines[i].strip()
        matched = any(re.match(p, line, flags=re.IGNORECASE) for p in leading_patterns)
        if matched:
            remove_count += 1
        else:
            break

    if remove_count > 0:
        cleaned_lines = lines[remove_count:]

    text = "\n".join(cleaned_lines)

    # remove conversational endings
    text = re.sub(
        r'\n*(I hope this helps|Let me know.*|Feel free to ask.*|Do you want me to.*|Would you like me to.*|I can also.*)\s*$',
        '',
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    # strip leaked retry wrapper if model copied it
    text = re.sub(
        r'###\s*\s*CRITICAL INSTRUCTION.*?$',
        '',
        text,
        flags=re.IGNORECASE | re.DOTALL
    )
    text = re.sub(
        r'###\s*SOURCE PROMPT.*?$',
        '',
        text,
        flags=re.IGNORECASE | re.DOTALL
    )
    text = re.sub(
        r'###\s*SOURCE MATERIAL.*?$',
        '',
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    text = remove_raw_input_block(text)
    return text.strip()


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


def detect_prompt_type(prompt_text: str) -> str:
    t = (prompt_text or "").lower()

    if "output format (one document per page)" in t or "# page:" in t:
        return "page"
    if "output format (one document per module)" in t or "# module:" in t:
        return "module"
    return "unknown"


def extract_expected_title(prompt_text: str, prompt_type: str) -> str:
    if prompt_type == "page":
        m = re.search(r'#\s*Page:\s*(.+)', prompt_text, flags=re.IGNORECASE)
        if m:
            return m.group(1).strip()

    if prompt_type == "module":
        m = re.search(r'#\s*Module:\s*(.+)', prompt_text, flags=re.IGNORECASE)
        if m:
            return m.group(1).strip()

    return "Unknown"


def enforce_output_template(text: str, prompt_type: str, expected_title: str) -> str:
    text = (text or "").strip()

    if prompt_type == "page":
        if not re.search(r'^\s*#+\s*Page\s*:', text, flags=re.IGNORECASE | re.MULTILINE):
            text = f"# Page: {expected_title}\n\n" + text

    elif prompt_type == "module":
        if not re.search(r'^\s*#+\s*Module\s*:', text, flags=re.IGNORECASE | re.MULTILINE):
            text = f"# Module: {expected_title}\n\n" + text

    return text


def validate_required_structure(text: str, prompt_type: str):
    text = (text or "").strip()
    text_lower = text.lower()

    if prompt_type == "page":
        header_patterns = {
            "page": r"^\s*#+\s*page\s*:",
            "web page file": r"^\s*\**web\s*page\s*file:\**\s*.+$",
            "code-behind file": r"^\s*\**code\s*-\s*behind\s*file:\**\s*.+$",
            "user purpose": r"^\s*#+\s*1\.\s*user\s*purpose\b",
            "key events & logic": r"^\s*#+\s*2\.\s*key\s*events\s*&?\s*logic\b",
            "data interactions": r"^\s*#+\s*3\.\s*data\s*interactions\b",
        }

        for name, pattern in header_patterns.items():
            if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                return False, f"Missing required section: {name}"

        if "| Event / Method | Business Logic Summary |" not in text:
            return False, "Missing page events table"

        tail = text_lower[-400:]
        for p in ["do you want me to", "would you like me to", "let me know if", "i can also"]:
            if p in tail:
                return False, "Detected conversational ending"

        return True, "Passed"

    if prompt_type == "module":
        header_patterns = {
            "module": r"^\s*#+\s*module\s*:",
            "file": r"^\s*\*\*file:\*\*\s*.+$",
            "purpose": r"^\s*#+\s*1\.\s*purpose\b",
            "key declarations": r"^\s*#+\s*2\.\s*key\s*declarations\b",
            "important behavior & side effects": r"^\s*#+\s*3\.\s*important\s*behavior\s*&?\s*side\s*effects\b",
            "data interactions": r"^\s*#+\s*4\.\s*data\s*interactions\b",
        }

        for name, pattern in header_patterns.items():
            if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                return False, f"Missing required section: {name}"

        if "| Symbol | Kind | Description |" not in text:
            return False, "Missing module declarations table"

        tail = text_lower[-400:]
        for p in ["do you want me to", "would you like me to", "let me know if", "i can also"]:
            if p in tail:
                return False, "Detected conversational ending"

        return True, "Passed"

    return True, "Passed"


def validate_critical_errors(text, prompt_type="unknown"):
    text = (text or "").strip()
    text_lower = text.lower()

    if not text or len(text) < 10:
        return False, "Output was empty or too short."

    # Strong C# detection only — avoid false positives from prose/jQuery examples
    csharp_patterns = [
        r'^\s*(public|private|protected|internal)\s+(partial\s+)?class\b',
        r'^\s*(public|private|protected|internal)\s+\w[\w<>\[\],\s]*\s+\w+\s*\([^)]*\)\s*\{?',
        r'^\s*using\s+[A-Za-z0-9_.]+\s*;',
        r'^\s*namespace\s+[A-Za-z0-9_.]+\s*\{?',
        r'^\s*\[(HttpGet|HttpPost|HttpPut|HttpDelete|Route|Authorize)[^\]]*\]',
        r'^\s*return\s+View\s*\(',
        r'^\s*return\s+Json\s*\(',
        r'^\s*model\s+[A-Za-z0-9_.<>]+\s*$',
        r'^\s*@model\s+[A-Za-z0-9_.<>]+\s*$',
    ]
    for pattern in csharp_patterns:
        if re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
            return False, "Detected C# Code Syntax"

    # Strong VB.NET detection
    vb_patterns = [
        r'^\s*(Public|Private|Protected|Friend)\s+(Class|Module|Sub|Function)\b',
        r'^\s*End\s+(Sub|Function|Class|Module)\b',
        r'^\s*Dim\s+\w+\s+As\s+\w+',
        r'^\s*Imports\s+[A-Za-z0-9_.]+',
        r'^\s*Inherits\s+[A-Za-z0-9_.]+',
        r'^\s*Handles\s+[A-Za-z0-9_.]+',
    ]
    for pattern in vb_patterns:
        if re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
            return False, "Detected VB.NET Code Structure"

    # Explicit code fences
    if re.search(r'```(csharp|cs|sql|vb|javascript|js|json|html)?', text_lower):
        return False, "Detected Code Block"

    # Strong forbidden phrases
    forbidden_keywords = [
        "public partial class",
        "protected void",
        "private void",
        "partial public class",
        "end sub",
        "end function",
        "end class",
    ]
    for kw in forbidden_keywords:
        if kw in text_lower:
            return False, f"Detected Code Keyword: '{kw}'"

    dup_bad, dup_reason = detect_excessive_duplicate_lines(text)
    if dup_bad:
        return False, dup_reason

    table_bad, table_reason = detect_duplicate_table_rows(text)
    if table_bad:
        return False, table_reason

    ok_struct, struct_reason = validate_required_structure(text, prompt_type)
    if not ok_struct:
        return False, struct_reason

    if len(text) > 300:
        compressed = zlib.compress(text.encode("utf-8"))
        ratio = len(compressed) / len(text)
        if ratio < 0.18:
            return False, f"Detected highly repetitive output (Entropy: {ratio:.2f})"

    return True, "Passed"


def extract_code_chunk(prompt_text):
    m = re.search(r'### RAW (?:CODE BEHIND INPUT|MODULE INPUT)\n(.*?)\n### END OF INPUT', prompt_text, flags=re.DOTALL)
    return m.group(1) if m else None


def split_json_blocks(code_chunk):
    if not code_chunk:
        return []
    parts = re.split(r'\n}\s*\n{', code_chunk)
    blocks = []
    for i, p in enumerate(parts):
        if i == 0:
            if not p.strip().startswith('{'):
                p = '{' + p
        else:
            p = '{' + p
        if not p.strip().endswith('}'):
            p = p + '}'
        blocks.append(p)
    return blocks


def count_expected_items_in_prompt(prompt_text):
    code_chunk = extract_code_chunk(prompt_text)
    if not code_chunk:
        return 0
    return len(split_json_blocks(code_chunk))


def count_sections_in_output(text):
    if not text:
        return 0
    return (
        len(re.findall(r'^\s*#\s*Page\s*:', text, flags=re.MULTILINE))
        + len(re.findall(r'^\s*#\s*Module\s*:', text, flags=re.MULTILINE))
        + len(re.findall(r'^\s*#\s*Utility', text, flags=re.MULTILINE))
    )

def natural_sort_key(filename: str):
    stem = os.path.splitext(filename)[0]
    parts = re.split(r'(\d+)', stem.lower())
    return [int(p) if p.isdigit() else p for p in parts]

def generate_single_item_output(llm, prompt_text, single_block):
    pattern = r'(### RAW (?:CODE BEHIND INPUT|MODULE INPUT)\n)(.*?)(\n### END OF INPUT)'
    replacement = r'\1' + single_block + r'\3'
    per_item_prompt = re.sub(pattern, replacement, prompt_text, flags=re.DOTALL)

    raw = ""
    try:
        for chunk in llm.stream(per_item_prompt):
            raw += chunk
    except Exception:
        raw = ""

    return clean_response(raw), raw


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

    raise RuntimeError(f"Unable to start Ollama server (tried {server_cmds}). Start it manually and ensure it's listening on {host}:{port}.")


def main():
    print("Starting ai_analysis...")
    print(f"Using model: {MODEL_NAME}")

    try:
        ensure_ollama_running(MODEL_NAME)
    except Exception as e:
        print(f"  ⚠️ Ollama not available: {e}")
        print("  Aborting ai_analysis. You can start Ollama manually or adjust the helper if your CLI differs.")
        return

    llm = Ollama(
        model=MODEL_NAME,
        temperature=0.1,
        num_ctx=8192,
        num_predict=4096,
        stop=["<|eot_id|>", "### SYSTEM ROLE", "### RAW"]
    )

    os.makedirs(ANALYSIS_OUTPUT_BASE, exist_ok=True)
    print(f"Analysis output base: {ANALYSIS_OUTPUT_BASE}")
    print(f"Prompts input base: {PROMPTS_INPUT_BASE}")

    for input_folder, output_folder in INPUT_OUTPUT_PAIRS:
        abs_input = os.path.abspath(os.path.join(PROMPTS_INPUT_BASE, input_folder))
        abs_output = os.path.abspath(os.path.join(ANALYSIS_OUTPUT_BASE, output_folder))

        print(f"\nProcessing input folder: '{abs_input}' -> output folder: '{abs_output}'")
        if not os.path.exists(abs_input):
            print(f"  Skipping (folder not found): {abs_input}")
            continue

        if os.path.exists(abs_output):
            print(f"  Wiping existing folder: {abs_output}")
            try:
                shutil.rmtree(abs_output)
            except OSError as e:
                print(f"  Error removing {abs_output}: {e}")
                continue

        os.makedirs(abs_output, exist_ok=True)

        files = [f for f in os.listdir(abs_input) if f.lower().endswith(".txt")]

        files.sort(key=natural_sort_key)

        for filename in files:
            output_filename = filename.replace(".txt", ".md")
            out_path = os.path.join(abs_output, output_filename)
            if os.path.exists(out_path):
                print(f"  Skipping {filename} (Done)")
                continue

            print(f"\n  Processing {filename}...")
            with open(os.path.join(abs_input, filename), "r", encoding="utf-8") as f:
                original_prompt = f.read()

            prompt_type = detect_prompt_type(original_prompt)
            expected_title = extract_expected_title(original_prompt, prompt_type)

            current_prompt = original_prompt
            final_output = ""
            success = False
            cleaned_text = ""
            raw_buffer = ""

            for attempt in range(1, MAX_RETRIES + 1):
                print(f"    > Attempt {attempt}/{MAX_RETRIES}...")
                raw_buffer = ""
                print("    ", end="")

                try:
                    for chunk in llm.stream(current_prompt):
                        print(chunk, end="", flush=True)
                        raw_buffer += chunk
                    print("\n")
                except Exception as e:
                    print(f"\n    💥 Error: {e}")
                    raw_buffer = ""

                cleaned_text = clean_response(raw_buffer)
                cleaned_text = enforce_output_template(cleaned_text, prompt_type, expected_title)

                is_valid, reason = validate_critical_errors(cleaned_text, prompt_type)

                if is_valid:
                    print("    ✅ VALIDATION PASSED (Auto-Cleaned)")
                    final_output = cleaned_text
                    success = True
                    break
                else:
                    print(f"    ❌ FATAL ERROR: {reason}")

                if prompt_type == "page":
                    current_prompt = textwrap.dedent(f"""
Return ONLY the completed document below.
Do not add any text before it.
Do not add any text after it.
Do not include instructions.
Do not write code.
If something cannot be determined, write: Not specified.

# Page: {expected_title}
Web Page File: Not specified
Code-Behind File: Not specified

### 1. User Purpose
Not specified

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Not specified | Not specified |

### 3. Data Interactions
* **Reads:** Not specified
* **Writes:** Not specified

Use the source material below to replace the placeholder content above.

### SOURCE MATERIAL
{original_prompt}
""")

                elif prompt_type == "module":
                    current_prompt = textwrap.dedent(f"""
Return ONLY the completed document below.
Do not add any text before it.
Do not add any text after it.
Do not include instructions.
Do not write code.
If something cannot be determined, write: Not specified.

# Module: {expected_title}
**File:** Not specified

### 1. Purpose
Not specified

### 2. Key Declarations
| Symbol | Kind | Description |
| :--- | :--- | :--- |
| Not specified | Not specified | Not specified |

### 3. Important Behavior & Side Effects
- Not specified

### 4. Data Interactions
* **Reads:** Not specified
* **Writes:** Not specified

Use the source material below to replace the placeholder content above.

### SOURCE MATERIAL
{original_prompt}
""")

                else:
                    current_prompt = textwrap.dedent(f"""
Return ONLY the completed document.
Do not add any extra text.
Use the source material below.

### SOURCE MATERIAL
{original_prompt}
""")

            if success:
                expected = count_expected_items_in_prompt(original_prompt)
                produced = count_sections_in_output(final_output)
                if expected > produced:
                    print(f"    ⚠️ Output contains {produced}/{expected} sections. Falling back to per-item generation...")
                    code_chunk = extract_code_chunk(original_prompt)
                    blocks = split_json_blocks(code_chunk)
                    per_item_results = []
                    for b in blocks:
                        cleaned_single, raw_single = generate_single_item_output(llm, original_prompt, b)
                        cleaned_single = enforce_output_template(cleaned_single, prompt_type, expected_title)
                        ok, _ = validate_critical_errors(cleaned_single, prompt_type)
                        if ok:
                            per_item_results.append(cleaned_single)
                        else:
                            per_item_results.append(cleaned_single or raw_single)
                    final_output = "\n\n".join(per_item_results)
            else:
                print(f"    ! ABORTING {filename} - Using fallback template.")

                if prompt_type == "page":
                    final_output = f"""# Page: {expected_title}
Web Page File: Not specified
Code-Behind File: Not specified

### 1. User Purpose
Generation failed after {MAX_RETRIES} attempts.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Unknown | Generation failed |

### 3. Data Interactions
* **Reads:** Not specified
* **Writes:** Not specified
"""

                elif prompt_type == "module":
                    final_output = f"""# Module: {expected_title}
**File:** Not specified

### 1. Purpose
Generation failed after {MAX_RETRIES} attempts.

### 2. Key Declarations
| Symbol | Kind | Description |
| :--- | :--- | :--- |
| Unknown | Unknown | Generation failed |

### 3. Important Behavior & Side Effects
- Unable to determine behavior due to repeated validation failure.

### 4. Data Interactions
* **Reads:** Not specified
* **Writes:** Not specified
"""

                else:
                    final_output = cleaned_text if cleaned_text else raw_buffer
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(final_output)
            print(f"    Saved: {out_path}")

    print("\nai_analysis: DONE")


if __name__ == "__main__":
    main()