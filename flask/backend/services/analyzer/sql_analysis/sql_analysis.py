import os
import re
import zlib
import shutil
import subprocess
import time
import socket
from langchain_community.llms import Ollama
from pathlib import Path

# --- CONFIGURATION ---
# These used to be relative to cwd; make them absolute under backend so
# the splitter/monitor/compile steps all agree on locations.
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))            # flask/backend/services/analyzer/sql_analysis
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))  # flask/backend
PROMPTS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")
ANALYSIS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "analysis_output")

INPUT_FOLDER = os.path.join(PROMPTS_OUTPUT_BASE, "SQL_Documentation_Prompts")
OUTPUT_FOLDER = os.path.join(ANALYSIS_OUTPUT_BASE, "Final_SQL_Docs")

DEFAULT_MODEL = "gemma3:latest"
# allow runtime override via environment variable ANALYSIS_MODEL
MODEL_NAME = os.environ.get("ANALYSIS_MODEL", DEFAULT_MODEL)
MAX_RETRIES = 3

# --- 1. CLEANER (Removes AI thinking/filler) ---
def clean_response(text):
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
# --- 2. SQL VALIDATOR ---
def validate_output(text):
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

    # must start with procedure heading
    if not re.match(r'^\s*#\s*Procedure\s*:\s*\S+', text, flags=re.IGNORECASE):
        return False, "Missing or invalid procedure title"

    # parameters table header must exist
    if "| Name | Type | Purpose |" not in text:
        return False, "Missing parameters table"

    # block conversational endings
    banned_tail_patterns = [
        r"do you want me to",
        r"would you like me to",
        r"let me know if",
        r"i can also",
    ]
    tail = text_lower[-400:]
    for p in banned_tail_patterns:
        if p in tail:
            return False, "Detected conversational ending"

    # raw SQL leakage
    if "create procedure" in text_lower or "create proc" in text_lower:
        if "set nocount on" in text_lower or "as\nbegin" in text_lower or "alter procedure" in text_lower:
            return False, "Detected raw SQL code"

    # entropy / repetition
    if len(text) > 300:
        compressed = zlib.compress(text.encode("utf-8"))
        ratio = len(compressed) / len(text)
        if ratio < 0.15:
            return False, f"Gibberish detected (ratio: {ratio:.2f})"

    return True, "Passed"

# --- Helpers to ensure Ollama is available (best-effort) ---
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
    print("Starting sql_analysis...")
    print(f"Using model: {MODEL_NAME}")
    print(f"SQL prompts input folder: {INPUT_FOLDER}")
    print(f"SQL analysis output folder: {OUTPUT_FOLDER}")

    # Ensure Ollama server is available and model is pulled (attempt start)
    try:
        ensure_ollama_running(MODEL_NAME)
    except Exception as e:
        print(f"  ⚠️ Ollama not available: {e}")
        print("  Aborting sql_analysis. Start Ollama manually or adjust the helper.")
        return

    # Clear previous output (we write into centralized analysis_output)
    if os.path.exists(OUTPUT_FOLDER):
        print(f"Wiping existing folder: {OUTPUT_FOLDER}")
        try:
            shutil.rmtree(OUTPUT_FOLDER)  # This deletes the folder and ALL contents
        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}.")
            return

    # Re-create the empty folder
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    llm = Ollama(
        model=MODEL_NAME,
        temperature=0.1,
        num_ctx=8192,      # Large context for SQL files
        num_predict=4096,
        stop=["<|eot_id|>", "### SYSTEM ROLE", "### ⬇️ RAW SQL INPUT ⬇️"]
    )

    # Read prompt files from centralized prompts_output
    if not os.path.isdir(INPUT_FOLDER):
        print(f"No SQL prompt folder found at '{INPUT_FOLDER}'. Skipping sql_analysis.")
        return

    files = sorted([f for f in os.listdir(INPUT_FOLDER) if f.endswith(".txt")])

    # If there are no SQL prompt files, skip the SQL analysis early (no-op)
    if not files:
        print(f"No SQL prompt files found in '{INPUT_FOLDER}'. Skipping sql_analysis.")
        return

    for filename in files:
        output_filename = filename.replace(".txt", ".md")
        if os.path.exists(os.path.join(OUTPUT_FOLDER, output_filename)):
            print(f"Skipping {filename} (Done)")
            continue

        print(f"\nProcessing {filename}...")
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
                current_prompt = f"""
                ### 🛑 CRITICAL INSTRUCTION
                **Your previous output failed: {reason}**
                1. Do NOT write SQL code blocks.
                2. Explain the LOGIC in English only.
                3. List the Tables used.

                {original_prompt}
                """

        if not success:
            print(f"  ! ABORTING {filename}")
            final_output = cleaned if cleaned else raw_buffer

        with open(os.path.join(OUTPUT_FOLDER, output_filename), "w", encoding="utf-8") as f:
            f.write(final_output)

if __name__ == "__main__":
    main()