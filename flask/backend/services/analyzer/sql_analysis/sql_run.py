import os
import re
import zlib
from langchain_community.llms import Ollama

# --- CONFIGURATION ---
INPUT_FOLDER = 'SQL_Documentation_Prompts'
OUTPUT_FOLDER = 'Final_SQL_Docs'
MODEL_NAME = "gpt-oss:latest" 
MAX_RETRIES = 3

# --- 1. CLEANER (Removes AI thinking/filler) ---
def clean_response(text):
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    text = re.sub(r'^```[a-zA-Z]*\n', '', text) 
    text = re.sub(r'\n```$', '', text)          
    patterns = [r'^(Okay|Sure|Here is|Let me|I have).*?(\n|:)', r'^.*?(generated|documentation).*?:']
    for p in patterns:
        text = re.sub(p, '', text, flags=re.IGNORECASE | re.MULTILINE)
    return text.strip()

# --- 2. SQL VALIDATOR ---
def validate_output(text):
    text_lower = text.lower()

    if not text or len(text) < 10: return False, "Output empty"

    # CRITICAL: Did it rewrite the code?
    # If we see "CREATE PROCEDURE" inside the output, it probably failed to document 
    # and just regurgitated the input.
    if "create procedure" in text_lower or "create proc" in text_lower:
        # Exception: It might be quoting the name. We check for a block.
        if "as\nbegin" in text_lower or "set nocount on" in text_lower:
            return False, "Detected Raw SQL Code (Do not rewrite the code!)"

    # ENTROPY CHECK
    if len(text) > 300:
        compressed = zlib.compress(text.encode('utf-8'))
        ratio = len(compressed) / len(text)
        if ratio < 0.15: return False, f"Gibberish Detected (Ratio: {ratio:.2f})"

    return True, "Passed"

def main():
    if not os.path.exists(OUTPUT_FOLDER): os.makedirs(OUTPUT_FOLDER)
    
    llm = Ollama(
        model=MODEL_NAME, 
        temperature=0.1, 
        num_ctx=8192,      # Large context for SQL files
        num_predict=4096,  
        stop=["<|eot_id|>", "### SYSTEM ROLE", "### ⬇️ RAW SQL INPUT ⬇️"]
    )

    files = sorted([f for f in os.listdir(INPUT_FOLDER) if f.endswith(".txt")])
    
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