import os
import re

# --- CONFIGURATION ---
DOCS_FOLDER = 'Final_Documentation_Chapters'
UTIL_FOLDER = 'Final_Utility_Chapters'
SQL_FOLDER = 'Final_SQL_Docs'
API_FOLDER = 'Final_API_Docs'
OUTPUT_FILENAME = 'Complete_Documentation.md'

# Base paths
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))  # flask/backend
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR))  # flask/backend
FINAL_OUTPUT_DIR = os.path.join(BACKEND_DIR, 'final_output')  # flask/backend/final_output


def get_file_order(filename):
    """
    Helper to sort files naturally (Part1, Part2, Part10...)
    instead of alphabetically (Part1, Part10, Part2).
    """
    numbers = re.findall(r'\d+', filename)
    if numbers:
        return int(numbers[-1])
    return 0


def clean_title(raw_title):
    """
    Extracts the core title from a header text.
    Removes 'Page:', 'Module:' and 'Procedure:' prefixes for a cleaner TOC.
    """
    if not raw_title:
        return ""
    text = raw_title.strip()
    text = re.sub(r'(?i)^(Page:|Module:|Procedure:)\s*', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text


def make_slug(section_name, base_name, idx, title):
    """
    Build a stable slug using section, filename base and index (to avoid collisions).
    """
    title_part = title.lower().replace(' ', '-').replace('.', '').replace('_', '-')
    slug_base = f"{section_name}-{base_name}-{idx}-{title_part}"
    slug = re.sub(r'[^a-z0-9-]', '', slug_base)
    return slug


def normalize_whitespace(text):
    """
    Normalize whitespace in markdown text to prevent extra blank lines in compiled output:
    - Strip trailing spaces from each line.
    - Convert whitespace-only lines into truly empty lines.
    - Collapse 3 or more consecutive newlines into 2 (preserve paragraph breaks).
    """
    lines = text.split('\n')
    lines = [line.rstrip() for line in lines]
    text = '\n'.join(lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def process_folder(folder_path, section_name, toc_lines, body_content, is_module=False):
    """
    Reads each .md/.txt file and creates a TOC entry and anchor for every H1 header
    inside the file.

    If is_module is False (default) this emits sections under the normal documentation
    heading (preserving 'Page:' and other conventions). If is_module is True, the
    items are treated as Modules/Utilities (TOC header adjusted and H1 'Module:' prefix
    normalized).
    """
    if not folder_path or not os.path.exists(folder_path):
        print(f"Warning: Folder '{folder_path}' not found. Skipping.")
        return

    # 1. Get Files (look for .md AND .txt)
    try:
        files = [f for f in os.listdir(folder_path) if f.lower().endswith((".md", ".txt"))]
    except Exception as e:
        print(f"Error reading folder '{folder_path}': {e}")
        return

    # Sort files
    files.sort(key=lambda x: (re.sub(r'\d+', '', x).lower(), get_file_order(x)))

    if not files:
        print(f"No files found in '{folder_path}'.")
        return

    # Build a human-friendly section header.
    # If caller already provided a module-focused name (e.g., "Modules"), avoid duplication.
    if is_module:
        kind_label = section_name if "module" in section_name.lower() else section_name + " (Modules)"
    else:
        kind_label = section_name

    print(f"Processing '{kind_label}' ({len(files)} files) from '{folder_path}'...")

    # Add Section Header to TOC
    toc_lines.append(f"\n### {kind_label}")

    for filename in files:
        filepath = os.path.join(folder_path, filename)
        try:
            with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except Exception as e:
            print(f"  Skipping file (read error): {filepath} - {e}")
            continue

        if not content or not content.strip():
            print(f"  Skipping empty file: {filepath}")
            continue

        base_name = os.path.splitext(filename)[0]

        # Find all H1 headers and their positions
        header_iter = list(re.finditer(r'^\s*#\s+(.+)$', content, flags=re.MULTILINE))
        if not header_iter:
            # No H1 headers: treat entire file as one section
            title = base_name
            slug = make_slug(kind_label, base_name, 1, title)
            toc_lines.append(f"- [{title}](#{slug})")
            body_content.append(f"\n<a id='{slug}'></a>\n")
            body_content.append(normalize_whitespace(content.strip()))
            body_content.append("\n\n---\n\n")
            continue

        # Split content into sections based on header positions
        sections = []
        for i, m in enumerate(header_iter):
            start = m.start()
            end = header_iter[i+1].start() if i+1 < len(header_iter) else len(content)
            header_text = m.group(1).strip()
            section_text = content[start:end].rstrip()
            sections.append((header_text, section_text))

        # Emit each section with unique slug and TOC entry
        for idx, (header_text, section_text) in enumerate(sections, start=1):
            cleaned_title = clean_title(header_text)
            title = cleaned_title if cleaned_title else base_name
            slug = make_slug(kind_label, base_name, idx, title)
            toc_lines.append(f"- [{title}](#{slug})")
            body_content.append(f"\n<a id='{slug}'></a>\n")
            # If module, normalize header tokens like "Module:" in the output section body
            if is_module:
                # replace leading "# Module:" with a clean H1 using cleaned_title
                section_text = re.sub(r'^\s*#\s*Module\s*:\s*.*$', f"# {title}", section_text, flags=re.IGNORECASE | re.MULTILINE)
            body_content.append(normalize_whitespace(section_text.strip()))
            body_content.append("\n\n---\n\n")


def find_folder(folder_name):
    """
    Locate folder_name in a set of reasonable places:
      - relative to this script (flask/backend)
      - prefer backend/analysis_output (where analyzers write final docs) then backend/prompts_output
      - inside services/analyzer subfolders (ai_analysis, sql_analysis)
      - fallback: walk the backend tree and return the first match
    Returns absolute path or None.
    """
    base = os.path.abspath(os.path.dirname(__file__))  # flask/backend
    candidates = [
        os.path.join(base, folder_name),
        os.path.join(base, "analysis_output", folder_name),
        os.path.join(base, "prompts_output", folder_name),
        os.path.join(base, "services", "analyzer", "ai_analysis", folder_name),
        os.path.join(base, "services", "analyzer", "sql_analysis", folder_name),
        os.path.join(base, "services", "analyzer", "api_analysis", folder_name),
        os.path.join(base, "services", "analyzer", folder_name)
    ]

    for c in candidates:
        if os.path.exists(c):
            print(f"Found '{folder_name}' at: {c}")
            return c

    # Fallback: walk the backend tree (limited depth)
    for root, dirs, files in os.walk(base):
        if folder_name in dirs:
            found = os.path.join(root, folder_name)
            print(f"Found '{folder_name}' by walking: {found}")
            return found

    print(f"Folder '{folder_name}' not found under '{base}'")
    return None


def main():
    toc_lines = ["# Technical Documentation", "", "## Table of Contents"]
    body_content = []

    # Attempt to locate the folders used by the analyzer scripts
    docs_path = find_folder(DOCS_FOLDER)
    util_path = find_folder(UTIL_FOLDER)
    sql_path = find_folder(SQL_FOLDER)
    api_path = find_folder(API_FOLDER)

    # --- PROCESS FOLDER 1: Documentation Chapters (Web Pages) ---
    if docs_path:
        process_folder(docs_path, "Web Pages", toc_lines, body_content, is_module=False)
    else:
        print(f"No documentation chapters found (expected folder '{DOCS_FOLDER}').")

    # --- PROCESS FOLDER 2: Utility / Module Chapters ---
    if util_path:
        process_folder(util_path, "Modules/Others", toc_lines, body_content, is_module=True)
    else:
        print(f"No utility/module chapters found (expected folder '{UTIL_FOLDER}').")

    # --- PROCESS FOLDER 3: SQL Reference ---
    if sql_path:
        process_folder(sql_path, "Database Reference (SQL)", toc_lines, body_content, is_module=False)
    else:
        print(f"No SQL docs found (expected folder '{SQL_FOLDER}').")

    # --- PROCESS FOLDER 4: API Reference ---
    if api_path:
        process_folder(api_path, "API Reference", toc_lines, body_content, is_module=False)
    else:
        print(f"No API docs found (expected folder '{API_FOLDER}').")

    # --- WRITE MASTER FILE ---
    if not body_content:
        print("❌ No content found to write. Ensure analyzer scripts produced output in the analyzer folders.")
        return

    final_text = "\n".join(toc_lines) + "\n\n<br>\n\n" + "".join(body_content)

    try:
        os.makedirs(FINAL_OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(FINAL_OUTPUT_DIR, OUTPUT_FILENAME)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_text)
        print(f"✅ Success! Created '{output_path}'")
    except Exception as e:
        print(f"Failed to write '{OUTPUT_FILENAME}': {e}")


if __name__ == "__main__":
    main()