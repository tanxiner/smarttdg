#!/usr/bin/env python3
"""
CPU-only SQL stored-procedure documentation generator using Ollama.

Features:
- Pulls the model via `ollama pull <model>` (best-effort).
- Warms up the model with a short request.
- Runs as many concurrent workers as CPU cores.
- Caches summaries to avoid redundant LLM calls for unchanged procedures.
- Periodic interim saves of output and a final markdown output at the end.

Usage: edit MODEL_NAME and the path to your SQL file if needed, then run:
    python -u generate_sql_documentation.py

Notes:
- Requires `ollama` in PATH for pre-pull/warm operations (script continues if ollama isn't found).
"""

import os
import re
import time
import json
import chardet
import hashlib
import subprocess
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Semaphore

from langchain_ollama import OllamaLLM

# --- CONFIG ---
MODEL_NAME = "llama4:latest"           # Model name used with Ollama
OUTPUT_FILE = "sql.md"                  # Final markdown file
CACHE_FILE = "sql_cache.json"           # Cache for summaries (keeps re-runs fast)
HEARTBEAT_FILE = "heartbeat.json"       # Heartbeat/status file updated as we progress
INTERIM_SAVE_EVERY = 10                 # Save interim markdown after this many new summaries
WARMUP_PROMPT = "Say 'hello' in one word."  # Warmup prompt to load the model
READ_PATH = os.path.join(os.path.expanduser("~"), "Documents", "script.sql")

# --- Helpers ---

def run_cmd(cmd):
    try:
        result = subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120
        )
        return result.stdout.decode("utf-8", errors="replace").strip()
    except Exception as e:
        return None

def has_local_model(model_name):
    try:
        # Try to start Ollama (will error if already running, that's okay)
        subprocess.run(
            ["ollama", "run", model_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=10
        )
    except Exception:
    #     pass  # Ignore errors if Ollama is already running
    # try:
    #     result = subprocess.run(
    #         ["ollama", "list"],
    #         stdout=subprocess.PIPE,
    #         stderr=subprocess.PIPE,
    #         timeout=30
    #     )
    #     output = result.stdout.decode("utf-8", errors="replace")
    #     # Check if model_name (or just its base name) exists
    #     return model_name.split(":")[0] in output
    # except Exception:
        return False

def pull_and_warm_model(model_name=MODEL_NAME, warm_prompt=WARMUP_PROMPT):
    print(f"[{time.strftime('%H:%M:%S')}] Checking for local model {model_name}...")
    if has_local_model(model_name):
        print(f"[{time.strftime('%H:%M:%S')}] Model {model_name} is already downloaded locally.", flush=True)
        # Only perform warmup (optional)
        try:
            llm = OllamaLLM(model=model_name)
            res = llm.invoke(warm_prompt)
            print(f"[{time.strftime('%H:%M:%S')}] Warm-up succeeded.", flush=True)
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] Warm-up failed: {e}", flush=True)
    else:
        #Only pull if not present!
        try:
            out = subprocess.run(
                ["ollama", "pull", model_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=120
            )
            print(f"[{time.strftime('%H:%M:%S')}] ollama pull completed.", flush=True)
        except subprocess.TimeoutExpired:
            print(f"[{time.strftime('%H:%M:%S')}] ollama pull timed out after 120 seconds; continuing.", flush=True)
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] ollama pull failed: {e}; continuing.", flush=True)
        # Optional: perform warmup as above


def detect_encoding(path):
    with open(path, "rb") as f:
        raw = f.read()
    result = chardet.detect(raw)
    return result.get("encoding") or "utf-8"

import re

def read_procedures_from_sql_file(output_path_sql):
    encoding = detect_encoding(output_path_sql)
    with open(output_path_sql, "r", encoding=encoding, errors="replace") as f:
        lines = f.readlines()

    procedures = []
    current_proc = []
    in_proc = False

    for line in lines:
        if re.match(r'(?i)^\s*CREATE\s+(?:OR\s+ALTER\s+)?(?:PROC|PROCEDURE)\b', line):
            in_proc = True
            current_proc = [line]
            continue

        if in_proc:
            if re.match(r'(?i)^\s*GO\s*$', line):
                # remove trailing GO from procedure
                procedures.append(''.join(current_proc).strip())
                current_proc = []
                in_proc = False
            else:
                current_proc.append(line)

    if current_proc:
        procedures.append(''.join(current_proc).strip())

    return procedures



# def save_all_procedures_to_single_file(output_path_sql, out_file=READ_PATH):
#     procedures = read_procedures_from_sql_file(output_path_sql)
#     with open(out_file, "w", encoding="utf-8") as f:
#         for idx, proc in enumerate(procedures, start=1):
#             f.write(f"\n/****** START PROCEDURE {idx} ******/\n")
#             # Optionally, include the procedure name in the marker
#             name = extract_proc_name(proc, idx)
#             f.write(f"-- PROCEDURE NAME: {name}\n")
#             f.write(proc)
#             f.write(f"\n/****** END PROCEDURE {idx} ******/\n")
#     print(f"Saved {len(procedures)} procedures in {out_file}")

def extract_proc_name(proc_sql: str, idx: int) -> str:
    m = re.search(
        r'CREATE\s+(?:OR\s+ALTER\s+)?(?:PROC|PROCEDURE)\s+('
        r'(?:\[[^\]]+\]|[A-Za-z0-9_]+)'
        r'(?:\s*\.\s*(?:\[[^\]]+\]|[A-Za-z0-9_]+))*'
        r')',
        proc_sql,
        re.IGNORECASE | re.DOTALL
    )
    if m:
        name = m.group(1)
        name = re.sub(r'[\[\]\s]+', '', name)
        name = re.sub(r'\.+', '.', name)
        return name
    m2 = re.search(r'CREATE\s+(?:OR\s+ALTER\s+)?(?:PROC|PROCEDURE)\s+([^\s\(\)]+)', proc_sql, re.IGNORECASE)
    if m2:
        fallback = re.sub(r'[\[\]]', '', m2.group(1).strip())
        return fallback
    return f"UnknownProcedure_{idx}"

def save_heartbeat(processed, total, current_name):
    hb = {
        "last_update_ts": int(time.time()),
        "processed": processed,
        "total": total,
        "current": current_name
    }
    try:
        tmp = HEARTBEAT_FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(hb, f, indent=2)
        os.replace(tmp, HEARTBEAT_FILE)
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Failed to write heartbeat: {e}", flush=True)

def save_markdown(output_file, summaries, total):
    try:
        tmp = output_file + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write("# SQL Stored Procedures Documentation\n\n")
            f.write(f"Total Procedures Found: {total}\n\n")
            f.write("---\n\n")
            for name in sorted(summaries.keys()):
                f.write(f"## {name}\n\n")
                f.write(summaries[name].strip() + "\n\n")
                f.write("---\n\n")
        os.replace(tmp, output_file)
        print(f"[{time.strftime('%H:%M:%S')}] Markdown successfully written to {os.path.abspath(output_file)}", flush=True)
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Failed to write markdown: {e}", flush=True)

def load_cache(cache_file):
    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_cache(cache_file, cache):
    try:
        tmp = cache_file + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(cache, f, indent=2, ensure_ascii=False)
        os.replace(tmp, cache_file)
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Failed to save cache: {e}", flush=True)

# --- Main pipeline ---

PROMPT_TEMPLATE_1 = """You are an expert SQL summarizer who will not refactor. Do not refactor the code. Do not include any internal thoughts or commentary.
Do not provide excerpt. Do not refactor anything.
Provide a concise summary (bulleted list) that covers:
- overall workflow
- input/output parameters
- tables read/written
- important conditional logic or business rules

Use the acronyms exactly as they appear in the input. Do not expand, spell out, or provide definitions for any acronyms at any point. 
Wherever an acronym appears, leave it as-is without any additional explanation.

Procedure:
{proc_sql}
"""

PROMPT_TEMPLATE_2 =  """You are an expert SQL summarizer who will not refactor. Do not refactor the code. Do not include any internal thoughts or commentary.
Do not provide excerpt.
Provide a short summary of the stored procedure in 2-3 sentences, focusing on its main purpose and functionality. Do not elaborate.
Use the acronyms exactly as they appear in the input. Do not expand, spell out, or provide definitions for any acronyms at any point. 
Wherever an acronym appears, leave it as-is without any additional explanation. Do not refactor anything. 

Procedure:
{proc_sql}
"""


def generate_sql_documentation(output_path_sql=READ_PATH, output_file=OUTPUT_FILE):
    procedures = read_procedures_from_sql_file(output_path_sql)
    total = len(procedures)
    print(f"[{time.strftime('%H:%M:%S')}] Found {total} stored procedures in {output_path_sql}", flush=True)

    pull_and_warm_model(MODEL_NAME)

    # Load cache if present (cache keyed by SHA256 of proc text)
    cache = load_cache(CACHE_FILE)
    summaries_1 = {}
    summaries_2 = {}
    processed = 0
    new_count = 0
    workers = 2  # adjust if needed
    sem = Semaphore(workers)

    print(f"[{time.strftime('%H:%M:%S')}] Using up to {workers} concurrent LLM calls.", flush=True)
    save_heartbeat(processed, total, "")

    def worker_task(proc_sql, idx):
        nonlocal cache
        proc_name = extract_proc_name(proc_sql, idx)
        proc_text = proc_sql.strip()
        h = hashlib.sha256(proc_text.encode("utf-8")).hexdigest()

        if h in cache and cache[h].get("name") == proc_name:
            print(f"[{time.strftime('%H:%M:%S')}] Cache hit: {proc_name}", flush=True)
            # Return 0 time for cached entries
            return proc_name, cache[h]["summary_1"], cache[h]["summary_2"], h, 0.0

        sem.acquire()
        start_time = time.time()
        try:
            llm = OllamaLLM(model=MODEL_NAME)

            prompt_1 = PROMPT_TEMPLATE_1.format(proc_sql=proc_text)
            try:
                result_1 = llm.invoke(prompt_1)
            except Exception as e:
                result_1 = f"ERROR: LLM invocation failed (prompt 1): {e}\n{traceback.format_exc()}"

            prompt_2 = PROMPT_TEMPLATE_2.format(proc_sql=proc_text)
            try:
                result_2 = llm.invoke(prompt_2)
            except Exception as e:
                result_2 = f"ERROR: LLM invocation failed (prompt 2): {e}\n{traceback.format_exc()}"

        finally:
            sem.release()
            duration = time.time() - start_time

        return proc_name, result_1, result_2, h, duration


    # --- Run tasks in a thread pool ---
    from concurrent.futures import ThreadPoolExecutor, as_completed
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(worker_task, proc_sql, idx): idx for idx, proc_sql in enumerate(procedures, start=1)}

        for future in as_completed(futures):
            idx = futures[future]
            try:
                name, result_1, result_2, h, duration = future.result()
            except Exception as e:
                name = f"UnknownProcedure_{idx}"
                result_1 = f"ERROR: worker exception: {e}\n{traceback.format_exc()}"
                result_2 = result_1
                h = hashlib.sha256(procedures[idx-1].encode("utf-8")).hexdigest()
                duration = 0.0

            # Update cache
            cache[h] = {
                "name": name,
                "summary_1": result_1,
                "summary_2": result_2,
                "hash": h,
                "timestamp": int(time.time()),
                "duration_sec": duration
            }

            # Store summaries
            summaries_1[name] = result_1
            summaries_2[name] = result_2
            processed += 1
            new_count += 1

            save_heartbeat(processed, total, name)
            print(f"[{time.strftime('%H:%M:%S')}] Processed {processed}/{total}: {name} ({duration:.2f}s)", flush=True)

            if new_count % INTERIM_SAVE_EVERY == 0: 
                save_cache(CACHE_FILE, cache) 
                save_markdown(output_file + ".prompt1.partial.md", summaries_1, total) 
                save_markdown(output_file + ".prompt2.partial.md", summaries_2, total) 
                print(f"[{time.strftime('%H:%M:%S')}] Interim save after {new_count} new summaries.", flush=True)

    # --- Final save ---
    save_cache(CACHE_FILE, cache)
    save_markdown(output_file + ".prompt1.md", summaries_1, total)
    save_markdown(output_file + ".prompt2.md", summaries_2, total)
    save_heartbeat(processed, total, "")
    print(f"[{time.strftime('%H:%M:%S')}] ✓ Completed. Documentation written to {output_file}", flush=True)




def extract_overall_workflow(summary):
    
    #result = extract_overall_workflow(summary)
   
    pattern = re.compile(
        r'(?i)\bworkflow\b[\s*:]*([\s\S]*?)[\s*:]*\binput\/output\b',
        re.IGNORECASE
    )

    match = pattern.search(summary)
    if match:
        # Extracted content
        content = match.group(1)

        # Remove all remaining '*' in the content
        content = content.replace('*', '')

        # Strip leading/trailing whitespace
        return content.strip()

    # Fallback: first 180 characters
    return summary.strip()[:180]


def save_workflow_summary(summaries, output_file="workflow_summary.txt"):
    try:
        tmp = output_file + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            for name in sorted(summaries.keys()):
                workflow = extract_overall_workflow(summaries[name])
                f.write(f"{name}:\n{workflow}\n\n")
        os.replace(tmp, output_file)
        print(f"Saved workflow summary to {os.path.abspath(output_file)}", flush=True)
    except Exception as e:
        print(f"Failed to write workflow summary: {e}", flush=True)

if __name__ == "__main__":
    try:
        generate_sql_documentation(READ_PATH, OUTPUT_FILE)
        #save_all_procedures_to_single_file(READ_PATH, "all_procs_extracted.sql")

    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Fatal error: {e}", flush=True)
        print(traceback.format_exc(), flush=True)
