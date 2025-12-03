import os
import re

# --- CONFIGURATION ---
DOCS_FOLDER = 'Final_Documentation_Chapters'
SQL_FOLDER = 'Final_SQL_Docs'
OUTPUT_FILE = 'Complete_TAMS_Documentation.md'

def get_file_order(filename):
    """
    Helper to sort files naturally (Part1, Part2, Part10...)
    instead of alphabetically (Part1, Part10, Part2).
    """
    numbers = re.findall(r'\d+', filename)
    if numbers:
        return int(numbers[-1]) 
    return 0

def clean_title(raw_line):
    """
    Extracts the core title from headers.
    Removes '# ', 'Page:', and 'Procedure:' prefixes for a cleaner TOC.
    """
    # Remove markdown header marker
    text = re.sub(r'^#\s+', '', raw_line).strip()
    # Remove specific prefixes (case insensitive)
    text = re.sub(r'(?i)^(Page:|Procedure:)\s*', '', text)
    return text

def process_folder(folder_path, section_name, toc_lines, body_content):
    """
    Reads a folder, adds its files to the body, and updates the TOC.
    """
    if not os.path.exists(folder_path):
        print(f"Warning: Folder '{folder_path}' not found. Skipping.")
        return

    # 1. Get Files (look for .md AND .txt)
    files = [f for f in os.listdir(folder_path) if f.lower().endswith((".md", ".txt"))]
    
    # Sort files
    files.sort(key=lambda x: (re.sub(r'\d+', '', x), get_file_order(x)))

    if not files:
        print(f"No files found in '{folder_path}'.")
        return

    print(f"Processing '{section_name}' ({len(files)} files)...")

    # Add Section Header to TOC
    toc_lines.append(f"\n### {section_name}")

    # 2. Process Each File
    for filename in files:
        filepath = os.path.join(folder_path, filename)
        
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read().strip()
        
        if not content: continue

        # --- Extract Title ---
        # Finds the first H1 header (# Title)
        title = filename # Default
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            title = clean_title(match.group(0))
        
        # Create Anchor Link
        # Unique slug strategy: section_name + title to avoid duplicates
        slug = f"{section_name}-{title}".lower().replace(' ', '-').replace('.', '').replace('_', '-')
        # Clean up slug (remove special chars)
        slug = re.sub(r'[^a-z0-9-]', '', slug)

        toc_lines.append(f"- [{title}](#{slug})")

        # Add to body
        body_content.append(f"\n<a id='{slug}'></a>\n") 
        body_content.append(content)
        body_content.append("\n\n---\n\n") 

def main():
    toc_lines = ["# TAMS Technical Documentation", "", "## Table of Contents"]
    body_content = []

    # --- PROCESS FOLDER 1: Documentation Chapters ---
    process_folder(DOCS_FOLDER, "System Documentation", toc_lines, body_content)

    # --- PROCESS FOLDER 2: SQL Reference ---
    process_folder(SQL_FOLDER, "Database Reference (SQL)", toc_lines, body_content)

    # --- WRITE MASTER FILE ---
    if not body_content:
        print("❌ No content found to write.")
        return

    final_text = "\n".join(toc_lines) + "\n\n<br>\n\n" + "".join(body_content)
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_text)

    print(f"✅ Success! Created '{OUTPUT_FILE}'")

if __name__ == "__main__":
    main()