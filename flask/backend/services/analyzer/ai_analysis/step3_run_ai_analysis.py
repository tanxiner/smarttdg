import os
import re
import zlib
from langchain_community.llms import Ollama

# --- CONFIGURATION ---
INPUT_FOLDER = 'Page_Documentation_Prompts'
OUTPUT_FOLDER = 'Final_Documentation_Chapters'
MODEL_NAME = "gpt-oss:latest" 
MAX_RETRIES = 3

# --- 1. CLEANER FUNCTION (Avoids Retries) ---
def clean_response(text):
    """
    Sanitizes the AI output using Python instead of asking the AI to do it.
    """
    # Remove <think> blocks (Reasoning models)
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    
    # Remove Markdown Code Fences (The ``` wrapper)
    # We strip the wrapper but keep the content inside
    text = re.sub(r'^```[a-zA-Z]*\n', '', text) 
    text = re.sub(r'\n```$', '', text)          
    
    # Remove Conversational Filler at the start
    # Matches "Okay,", "Here is", "Sure", "I have generated"
    patterns = [
        r'^(Okay|Sure|Here is|Let me|I have|Below is|The following).*?(\n|:)',
        r'^.*?(generated|documentation|analysis).*?:'
    ]
    for p in patterns:
        text = re.sub(p, '', text, flags=re.IGNORECASE | re.MULTILINE)

    return text.strip()

# --- 2. VALIDATOR (Fatal Errors Only) ---
def validate_critical_errors(text):
    text_lower = text.lower()

    # Empty Check
    if not text or len(text) < 10:
        return False, "Output was empty or too short."

    # HARD SYNTAX CHECK (C# Code)
    # We only fail if we see clear C# signatures that Regex couldn't clean
    if "{" in text and "}" in text and ";" in text and ("void" in text or "public" in text):
        return False, "Detected C# Code Syntax"

    # SMART CODE BLOCK CHECK
    # Only fail if it specifically tries to write C# or SQL code.
    # We allow generic "```" blocks for text diagrams.
    if "```csharp" in text_lower or "```cs" in text_lower or "```sql" in text_lower:
        return False, "Detected C# or SQL Code Block"

    # KEYWORD BANS
    forbidden_keywords = ["public partial class", "protected void", "private void"]
    for kw in forbidden_keywords:
        if kw in text_lower: return False, f"Detected Code Keyword: '{kw}'"

    # GIBBERISH / LOOP CHECK
    if len(text) > 300:
        compressed = zlib.compress(text.encode('utf-8'))
        ratio = len(compressed) / len(text)
        if ratio < 0.15:
            return False, f"Detected Repetitive Gibberish (Entropy: {ratio:.2f})"

    return True, "Passed"

def main():
    if not os.path.exists(OUTPUT_FOLDER): os.makedirs(OUTPUT_FOLDER)
    
    # --- CRITICAL CONFIGURATION FIXES ---
    llm = Ollama(
        model=MODEL_NAME, 
        temperature=0.1, 
        
        # INCREASE CONTEXT WINDOW (Default is 2048 - too small for retries)
        num_ctx=8192,  
        
        # Stop generation after 2048 new tokens (Prevents infinite loops)
        num_predict=4096, 
        
        # Stop signals
        stop=["<|eot_id|>", "### SYSTEM ROLE", "### ⬇️ RAW"]
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
            print(f"  > Attempt {attempt}/{MAX_RETRIES}...")
            
            raw_buffer = ""
            print("    ", end="") 
            
            # Streaming Loop
            try:
                for chunk in llm.stream(current_prompt):
                    print(chunk, end="", flush=True)
                    raw_buffer += chunk
                print("\n") 
            except Exception as e:
                print(f"\n  💥 Generation Error: {e}")
                raw_buffer = ""

            # --- PHASE 1: AUTO-FIX ---
            # Clean the text using Python before judging it
            cleaned_text = clean_response(raw_buffer)

            # --- PHASE 2: CRITICAL VALIDATION ---
            is_valid, reason = validate_critical_errors(cleaned_text)

            if is_valid:
                print("  ✅ VALIDATION PASSED (Auto-Cleaned)")
                final_output = cleaned_text
                success = True
                break
            else:
                print(f"  ❌ FATAL ERROR: {reason}")
                
                # --- PHASE 3: SMART RETRY ---
                # We put the warning AT THE TOP so it's the first thing the model sees.
                # We do NOT append to the bottom to avoid context fragmentation.
                current_prompt = f"""
                ### 🛑 CRITICAL INSTRUCTION - READ CAREFULLY
                **Your previous output failed because: {reason}**
                1. You MUST NOT write C# code.
                2. You MUST NOT repeat text.
                3. Write ONLY English descriptions.

                {original_prompt}
                """

        if not success:
            print(f"  ! ABORTING {filename} - Saving partial output.")
            final_output = cleaned_text if cleaned_text else raw_buffer

        with open(os.path.join(OUTPUT_FOLDER, output_filename), "w", encoding="utf-8") as f:
            f.write(final_output)

if __name__ == "__main__":
    main()