import json
import os
import copy
from collections import defaultdict

INPUT_FILE = os.path.join(os.path.expanduser("~"), "Documents", "all_analysis_results1.json")
OUTPUT_DIR = 'Page_Documentation_Prompts'
MAX_CHARS = 12000 

# --- V7 TEMPLATE: PAGE FUNCTIONALITY ---
TEMPLATE = """
### SYSTEM ROLE
You are a **Technical Writer** specializing in Legacy Web Applications.
You are NOT a Developer. You DO NOT write code.

### OBJECTIVE
Analyze the "Code Behind" files to create a **Page Functionality Reference**.

### 🛑 HARD NEGATIVE CONSTRAINTS
1. **NO** C# or SQL code blocks.
2. **NO** "Installation" or "Setup" sections.
3. **NO** explanation of standard ASP.NET concepts (e.g., don't explain what Page_Load is; explain what *this specific page* does inside it).
4. **NO** mentions of `.designer.cs` or auto-generated controls.

### ✅ STRICT OUTPUT FORMAT
For every Page/Control found in the input, output this structure:

# Page: {PageName}
**File:** {Filename}

### 1. User Purpose
{One sentence explaining what the user does here. E.g., "Users fill out this form to request x."}

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| {MethodName} | {Plain English description of what happens. E.g., "Validates inputs, calls DAO to save, sends email."} |

### 3. Data Interactions
* **Reads:** {List entities/tables loaded (e.g., User, BlockedTar)}
* **Writes:** {List entities/tables saved or updated}

---

### ⬇️ RAW CODE BEHIND INPUT ⬇️
{code_chunk}

### ⬆️ END OF INPUT ⬆️
**INSTRUCTION:** Document the page logic above. Focus on User Actions and Data Flow.
"""

def clean_data(item):
    """Removes noise to save tokens."""
    clean_item = copy.deepcopy(item)
    keys_to_remove = ["dependencies", "usings", "assemblies", "imports", "file_level_sql"]
    
    for key in keys_to_remove:
        if key in clean_item: del clean_item[key]
        if "ir" in clean_item and key in clean_item["ir"]: del clean_item["ir"][key]
            
    return clean_item

def is_page_file(filename):
    """Returns True if this is a relevant Web Forms code-behind file."""
    if not filename: return False
    lower_name = filename.lower()
    
    # We want Code Behinds (.cs) for Pages (.aspx), Masters (.master), and Controls (.ascx)
    relevant_extensions = (".aspx.cs", ".master.cs", ".ascx.cs")
    
    # We specifically DO NOT want Designer files (auto-generated noise)
    if lower_name.endswith(".designer.cs"): return False
    
    return lower_name.endswith(relevant_extensions)

def main():
    print(f"Reading {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error: {e}")
        return

    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

    # Group strictly by "Pages" (using the filename as the grouper might be too granular, 
    # so we'll group by Folder/Namespace to keep related pages together).
    groups = defaultdict(list)
    
    found_count = 0
    for item in data:
        # Get filename
        fname = item.get("file", "") or item.get("fileName", "") or ""
        if "ir" in item and "path" in item["ir"]: fname = item["ir"]["path"]

        # FILTER: Is this a Page?
        if is_page_file(fname):
            # Clean it
            cleaned = clean_data(item)
            
            # Group by Namespace (e.g., TAMS, TAMS.Admin)
            ns = "Unknown"
            if "namespaces" in item and item["namespaces"]: ns = item["namespaces"][0]
            elif "ir" in item and "namespaces" in item["ir"]: ns = item["ir"]["namespaces"][0]
            
            groups[ns].append(cleaned)
            found_count += 1

    print(f"Found {found_count} pages across {len(groups)} namespaces. Generating prompts...")

    for ns, items in groups.items():
        chunk_str = ""
        part = 1
        
        # Sort by filename so related pages (e.g. Login.aspx.cs) appear alphabetically
        items.sort(key=lambda x: x.get("file", ""))

        for item in items:
            item_dump = json.dumps(item, indent=2)
            if len(chunk_str) + len(item_dump) > MAX_CHARS:
                save_file(ns, part, chunk_str)
                part += 1
                chunk_str = ""
            chunk_str += item_dump + "\n"
        
        if chunk_str:
            save_file(ns, part, chunk_str)

    print(f"DONE! Page prompts saved in '{OUTPUT_DIR}'.")

def save_file(ns, part, content):
    clean_ns = ns.replace('.', '_').replace('/', '_').replace('\\', '_')
    fname = f"Pages_{clean_ns}_Part{part}.txt"
    final_content = TEMPLATE.replace("{code_chunk}", content)
    
    with open(os.path.join(OUTPUT_DIR, fname), 'w', encoding='utf-8') as f:
        f.write(final_content)

if __name__ == "__main__":
    main()