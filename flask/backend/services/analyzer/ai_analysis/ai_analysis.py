import os
import re
import zlib
import textwrap
import shutil
import subprocess
import time
import socket
from langchain_community.llms import Ollama

# --- CONFIGURATION ---
# Process both page prompts and utility/module prompts (if present)
INPUT_OUTPUT_PAIRS = [
    ("Page_Documentation_Prompts", "Final_Documentation_Chapters"),
    ("Utility_Documentation_Prompts", "Final_Utility_Chapters"),
]
DEFAULT_MODEL = "gemma3:latest"
# allow runtime override via environment variable ANALYSIS_MODEL
MODEL_NAME = os.environ.get("ANALYSIS_MODEL", DEFAULT_MODEL)
MAX_RETRIES = 5

# Base paths
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))                         # flask/backend/services/analyzer/ai_analysis
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))       # flask/backend

# --- INPUT SOURCE: read prompts from flask/backend/prompts_output ---
PROMPTS_INPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")                # flask/backend/prompts_output

# --- OUTPUT BASE: place analysis results under flask/backend/analysis_output (unchanged) ---
ANALYSIS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "analysis_output")              # flask/backend/analysis_output

def remove_raw_input_block(text: str) -> str:
    marker = re.search(r'RAW INPUT', text, flags=re.IGNORECASE)
    if marker:
        return text[:marker.start()].rstrip()
    return text

# --- 1. CLEANER FUNCTION (Avoids Retries) ---
def clean_response(text):
    """
    Sanitizes the AI output while avoiding removing valid in-document sentences.
    Only strip common boilerplate from the very beginning of the response (leading lines).
    """
    if not text:
        return text

    # Remove <think> blocks (Reasoning models)
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)

    # Remove Markdown Code Fences
    text = re.sub(r'^```[a-zA-Z]*\n', '', text)
    text = re.sub(r'\n```$', '', text)

    # Split into lines and remove only leading boilerplate lines (first N lines)
    lines = text.splitlines()
    cleaned_lines = list(lines)  # copy

    # Patterns that indicate a boilerplate/opening conversational line
    leading_patterns = [
        r'^(Based on|I have|This page|The provided).*?(\.|:)\s*$',
        r'^(Okay|Sure|Here is|Let me|Below is|The following).*?(\:)?\s*$',
        r'^.*?(generated|documentation|analysis).*?:\s*$'
    ]

    max_head_lines = min(8, len(lines))  # only inspect the first up to 8 lines
    remove_count = 0
    for i in range(max_head_lines):
        line = lines[i].strip()
        matched = False
        for p in leading_patterns:
            if re.match(p, line, flags=re.IGNORECASE):
                matched = True
                break
        if matched:
            remove_count += 1
        else:
            break

    if remove_count > 0:
        cleaned_lines = lines[remove_count:]

    text = "\n".join(cleaned_lines)

    # Remove conversational filler at the END (only a few trailing phrases)
    text = re.sub(r'(I hope this helps|Let me know|Feel free to ask).*?$', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = remove_raw_input_block(text)

    return text.strip()

# --- 2. VALIDATOR (Fatal Errors Only) ---
def validate_critical_errors(text):
    text_lower = (text or "").lower()

    if not text or len(text.strip()) < 10:
        return False, "Output was empty or too short."

    # existing code checks here...

    # duplicate line check
    dup_bad, dup_reason = detect_excessive_duplicate_lines(text)
    if dup_bad:
        return False, dup_reason

    # duplicate markdown table row check
    table_bad, table_reason = detect_duplicate_table_rows(text)
    if table_bad:
        return False, table_reason

    # lighter compression safety net
    if len(text) > 300:
        compressed = zlib.compress(text.encode('utf-8'))
        ratio = len(compressed) / len(text)
        if ratio < 0.18:
            return False, f"Detected highly repetitive output (Entropy: {ratio:.2f})"

    return True, "Passed"

# --- Helpers for per-item fallback ---
def extract_code_chunk(prompt_text):
    """Return the code_chunk content between the RAW markers (or None).
    Support both page and module markers used by the splitter.
    """
    m = re.search(r'### ⬇️ RAW (?:CODE BEHIND INPUT|MODULE INPUT) ⬇️\n(.*?)\n### ⬆️ END OF INPUT ⬆️', prompt_text, flags=re.DOTALL)
    return m.group(1) if m else None

def split_json_blocks(code_chunk):
    """
    Split concatenated pretty-printed JSON objects that ai_splitter writes.
    Splits on '}\n{' safely and returns each block as a valid JSON-ish string (with braces).
    """
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
    """Count documented sections produced by the model (Page/Module/Utility headings)."""
    if not text:
        return 0
    # model output may use headings starting with '# Page:', '# Module:' or '# Utility'
    return (
        len(re.findall(r'^\s*#\s*Page\s*:', text, flags=re.MULTILINE))
        + len(re.findall(r'^\s*#\s*Module\s*:', text, flags=re.MULTILINE))
        + len(re.findall(r'^\s*#\s*Utility', text, flags=re.MULTILINE))
    )

def generate_single_item_output(llm, prompt_text, single_block):
    """Build a per-item prompt by replacing the chunk with single_block and stream one response."""
    pattern = r'(### ⬇️ RAW (?:CODE BEHIND INPUT|MODULE INPUT) ⬇️\n)(.*?)(\n### ⬆️ END OF INPUT ⬆️)'
    replacement = r'\1' + single_block + r'\3'
    per_item_prompt = re.sub(pattern, replacement, prompt_text, flags=re.DOTALL)
    # streaming
    raw = ""
    try:
        for chunk in llm.stream(per_item_prompt):
            raw += chunk
    except Exception:
        raw = ""
    return clean_response(raw), raw

# --- NEW: Ensure Ollama is installed and running (best-effort) ---
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
    """
    Best-effort helper:
    - checks whether Ollama HTTP server is reachable at host:port
    - attempts to locate `ollama` CLI
    - runs `ollama pull <model>` to ensure model is present (non-fatal)
    - tries to start the local Ollama server using common subcommands if not already running
    Raises RuntimeError if ollama is not installed and cannot be started.
    """
    if _is_port_open(host, port):
        return

    ollama_path = shutil.which("ollama")
    if not ollama_path:
        raise RuntimeError("`ollama` CLI not found on PATH. Install Ollama and ensure `ollama` is available.")

    # Try to pull model (non-fatal)
    try:
        subprocess.run([ollama_path, "pull", model], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    except Exception:
        pass

    # Try common server subcommands; update list if your version uses a different verb.
    server_cmds = [["serve"], ["daemon"], ["run", "serve"]]
    for cmd in server_cmds:
        try:
            proc = subprocess.Popen([ollama_path] + cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            continue
        # wait until port is open or timeout
        deadline = time.time() + timeout
        while time.time() < deadline:
            if _is_port_open(host, port):
                return
            time.sleep(0.5)
        # didn't start successfully; try to terminate and try next command
        try:
            proc.terminate()
        except Exception:
            pass

    raise RuntimeError(f"Unable to start Ollama server (tried {server_cmds}). Start it manually and ensure it's listening on {host}:{port}.")

def main():
    print("Starting ai_analysis...")
    print(f"Using model: {MODEL_NAME}")

    # Ensure Ollama server is available and model is pulled (attempt start)
    try:
        ensure_ollama_running(MODEL_NAME)
    except Exception as e:
        print(f"  ⚠️ Ollama not available: {e}")
        print("  Aborting ai_analysis. You can start Ollama manually or adjust the helper if your CLI differs.")
        return

    # Initialize LLM once
    llm = Ollama(
        model=MODEL_NAME,
        temperature=0.1,
        num_ctx=8192,
        num_predict=4096,
        stop=["<|eot_id|>", "### SYSTEM ROLE", "### ⬇️ RAW"]
    )

    # Ensure base output folder exists
    os.makedirs(ANALYSIS_OUTPUT_BASE, exist_ok=True)
    print(f"Analysis output base: {ANALYSIS_OUTPUT_BASE}")
    print(f"Prompts input base: {PROMPTS_INPUT_BASE}")

    for input_folder, output_folder in INPUT_OUTPUT_PAIRS:
        # Resolve input folder under backend/prompts_output (where ai_splitter writes prompts)
        abs_input = os.path.abspath(os.path.join(PROMPTS_INPUT_BASE, input_folder))
        # Resolve output folder under backend/analysis_output/<output_folder>
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

        files = sorted([f for f in os.listdir(abs_input) if f.endswith(".txt")])

        for filename in files:
            output_filename = filename.replace(".txt", ".md")
            out_path = os.path.join(abs_output, output_filename)
            if os.path.exists(out_path):
                print(f"  Skipping {filename} (Done)")
                continue

            print(f"\n  Processing {filename}...")
            with open(os.path.join(abs_input, filename), "r", encoding="utf-8") as f:
                original_prompt = f.read()

            current_prompt = original_prompt
            final_output = ""
            success = False

            for attempt in range(1, MAX_RETRIES + 1):
                print(f"    > Attempt {attempt}/{MAX_RETRIES}...")
                raw_buffer = ""
                print("    ", end="")

                # Streaming Loop
                try:
                    for chunk in llm.stream(current_prompt):
                        print(chunk, end="", flush=True)
                        raw_buffer += chunk
                    print("\n")
                except Exception as e:
                    print(f"\n    💥 Generation Error: {e}")
                    raw_buffer = ""

                # --- PHASE 1: AUTO-FIX ---
                cleaned_text = clean_response(raw_buffer)

                # --- PHASE 2: CRITICAL VALIDATION ---
                is_valid, reason = validate_critical_errors(cleaned_text)

                if is_valid:
                    print("    ✅ VALIDATION PASSED (Auto-Cleaned)")
                    final_output = cleaned_text
                    success = True
                    break
                else:
                    print(f"    ❌ FATAL ERROR: {reason}")

                # --- PHASE 3: SMART RETRY ---
                current_prompt = textwrap.dedent(f"""
                ### 🛑 CRITICAL INSTRUCTION - READ CAREFULLY
                **Your previous output failed because: {reason}**
                1. You MUST NOT write Code (C#, VB.NET, or SQL).
                2. You MUST NOT repeat text.
                3. Write ONLY English descriptions.

                {original_prompt}
                """)

            # If top-level attempt succeeded but produced fewer sections than items, do per-item fallback
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
                        ok, _ = validate_critical_errors(cleaned_single)
                        if ok:
                            per_item_results.append(cleaned_single)
                        else:
                            per_item_results.append(cleaned_single or raw_single)
                    final_output = "\n\n".join(per_item_results)
            else:
                print(f"    ! ABORTING {filename} - Saving partial output.")
                final_output = cleaned_text if cleaned_text else raw_buffer

            # Write output file
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(final_output)
            print(f"    Saved: {out_path}")

    print("\nai_analysis: DONE")

if __name__ == "__main__":
    main()