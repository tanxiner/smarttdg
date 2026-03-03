import os
import re
import zlib
import shutil
import subprocess
import time
import socket
from langchain_community.llms import Ollama

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
    text = re.sub(r'(I hope this helps|Let me know|Feel free to ask).*?$', '', text,
                  flags=re.IGNORECASE | re.DOTALL)
    return text.strip()


# --- VALIDATOR ---
def validate_output(text):
    text_lower = (text or "").lower()
    if not text or len(text.strip()) < 10:
        return False, "Output was empty or too short."

    # Code block checks
    if "```csharp" in text_lower or "```cs" in text_lower or "```sql" in text_lower or "```vb" in text_lower:
        return False, "Detected code block in output"

    forbidden = ["public partial class", "protected void", "private void"]
    for kw in forbidden:
        if kw in text_lower:
            return False, f"Detected code keyword: '{kw}'"

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

    files = sorted([f for f in os.listdir(INPUT_FOLDER) if f.endswith(".txt")])
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
            is_valid, reason = validate_output(cleaned)

            if is_valid:
                print("  ✅ PASS")
                final_output = cleaned
                success = True
                break
            else:
                print(f"  ❌ FAIL: {reason}")
                current_prompt = (
                    f"### 🛑 CRITICAL INSTRUCTION\n"
                    f"**Your previous output failed: {reason}**\n"
                    f"1. Do NOT write code blocks.\n"
                    f"2. Describe the API endpoint in English only.\n\n"
                    f"{original_prompt}"
                )

        if not success:
            print(f"  ! ABORTING {filename}")
            final_output = cleaned if cleaned else raw_buffer

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_output)
        print(f"  Saved: {out_path}")

    print("\napi_analysis: DONE")


if __name__ == "__main__":
    main()
