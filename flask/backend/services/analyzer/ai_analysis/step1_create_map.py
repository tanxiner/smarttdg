import json
import os

INPUT_FILE = os.path.join(os.path.expanduser("~"), "Documents", "all_analysis_results1.json")
OUTPUT_FILE = '00_START_HERE_Architecture.txt'

# Limits context to ~8k tokens (safe for local AI)
MAX_CHARS = 32000 

def main():
    print(f"Reading {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error: {e}")
        return

    # Extract clean list of files and classes
    lines = []
    
    # SORTING: Safety wrapper to prevent crashes during sort
    def sort_key_wrapper(x):
        # Try top-level namespace
        if x.get("namespaces") and len(x["namespaces"]) > 0:
            return x["namespaces"][0]
        # Try IR namespace
        if x.get("ir") and x["ir"].get("namespaces") and len(x["ir"]["namespaces"]) > 0:
            return x["ir"]["namespaces"][0]
        return "ZZ_Misc" # Puts unknown files at the end

    data.sort(key=sort_key_wrapper)

    for item in data:
        # 1. Get Namespace (FIXED LOGIC)
        ns = "Misc"
        # Check top-level
        if "namespaces" in item and item["namespaces"] and len(item["namespaces"]) > 0:
             ns = item["namespaces"][0]
        # Check nested IR
        elif "ir" in item and "namespaces" in item["ir"] and item["ir"]["namespaces"] and len(item["ir"]["namespaces"]) > 0:
             ns = item["ir"]["namespaces"][0]
        
        # 2. Get Filename
        fname = item.get("file") or item.get("fileName") or "Unknown"
        
        # 3. Get Classes
        classes = item.get("classes", [])
        if not classes and "ir" in item: classes = item["ir"].get("types", [])
        
        if not classes: continue 

        for c in classes:
            c_name = c.get("name", "Unknown")
            lines.append(f"NS: {ns} | File: {fname} | Class: {c_name}")
            
            methods = c.get("methods", [])
            if not methods and "methods" in item: methods = item["methods"]
            
            # Safety check for methods
            m_names = []
            if methods:
                m_names = [m.get("name") for m in methods if isinstance(m, dict) and m.get("name")]
            
            if m_names:
                lines.append(f"   Functions: {', '.join(m_names[:8])}") 

    # Create the Prompt
    skeleton = "\n".join(lines)
    if len(skeleton) > MAX_CHARS:
        skeleton = skeleton[:MAX_CHARS] + "\n...(truncated)..."

    prompt = f"""
### SYSTEM ROLE
You are a Software Architect.
### GOAL
Write the "High-Level Architecture" and "Table of Contents" for a Developer Guide.
### INPUT
Below is the list of every class in the system (The Skeleton).
### TASKS
1. Identify the architectural pattern (e.g., 3-Tier, MVC) based on the namespaces.
2. Group the classes into logical "Chapters" (e.g., "Chapter 1: User Management", "Chapter 2: Depot Logic").
3. Write a summary of what the system does based on the class names.
### SKELETON DATA
{skeleton}
"""

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(prompt)
    print(f"DONE. Created '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()