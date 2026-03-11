import os
import re

# --- CONFIGURATION ---
DOCS_FOLDER = 'Final_Documentation_Chapters'
UTIL_FOLDER = 'Final_Utility_Chapters'
UTIL_SQL_FOLDER = 'Final_Utility_SQL_Chapters'
SQL_FOLDER = 'Final_SQL_Docs'
API_FOLDER = 'Final_API_Docs'
OUTPUT_FILENAME = 'Technical_Documentation.md'

# Base paths
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))  # flask/backend
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR))  # flask/backend
FINAL_OUTPUT_DIR = os.path.join(BACKEND_DIR, 'final_output')  # flask/backend/final_output

# Track generated slugs across the whole run so anchors are globally unique
_USED_SLUGS = set()


def get_file_order(filename):
    """
    Helper to sort files naturally (Part1, Part2, Part10...)
    instead of alphabetically (Part1, Part10, Part2).
    """
    numbers = re.findall(r'\d+', filename)
    if numbers:
        return int(numbers[-1])
    return 0


def parse_part_info(filename: str):
    """
    Extract base key + numeric part from names like:
    001_MyProc_part1.md
    001_MyProc_part2.txt
    """
    m = re.match(
        r"^(?P<prefix>.+?)_part(?P<part>\d+)\.(md|txt)$",
        filename,
        flags=re.IGNORECASE
    )
    if not m:
        return None
    base_key = m.group("prefix")
    part_num = int(m.group("part"))
    return base_key, part_num


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
    Keep result lowercase and limited to letters, numbers and hyphens.
    """
    title_part = (title or "").lower().replace(' ', '-').replace('.', '').replace('_', '-')
    sec = re.sub(r'[^a-z0-9-]', '', section_name.lower().replace(' ', '-'))
    base = re.sub(r'[^a-z0-9-]', '', base_name.lower().replace(' ', '-'))
    slug_base = f"{sec}-{base}-{idx}-{title_part}"
    slug = re.sub(r'[^a-z0-9-]', '', slug_base)
    slug = re.sub(r'-{2,}', '-', slug).strip('-')
    if not slug:
        slug = f"section-{base or 'item'}-{idx}"
    return slug


def _ensure_unique_slug(slug: str) -> str:
    """
    Ensure the slug is unique across this process run by appending a numeric suffix
    when a collision is detected. Records used slugs in _USED_SLUGS.
    """
    if slug not in _USED_SLUGS:
        _USED_SLUGS.add(slug)
        return slug

    i = 2
    while True:
        candidate = f"{slug}-{i}"
        if candidate not in _USED_SLUGS:
            _USED_SLUGS.add(candidate)
            return candidate
        i += 1


def normalize_whitespace(text):
    """
    Normalize whitespace in markdown text to prevent extra blank lines in compiled output:
    - Strip trailing spaces from each line.
    - Convert whitespace-only lines into truly empty lines.
    - Collapse 3 or more consecutive newlines into 2.
    """
    lines = text.split('\n')
    lines = [line.rstrip() for line in lines]
    text = '\n'.join(lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text

def sql_sort_key(filename):
    stem = os.path.splitext(filename)[0]

    m = re.match(r'^(?P<seq>\d+)_?(?P<name>.*?)(?:_part(?P<part>\d+))?$', stem, flags=re.IGNORECASE)
    if m:
        seq = int(m.group("seq"))
        name = (m.group("name") or "").lower()
        part = int(m.group("part")) if m.group("part") else 0
        return (seq, name, part)

    # fallback natural sort
    parts = re.split(r'(\d+)', stem.lower())
    return tuple(int(p) if p.isdigit() else p for p in parts)


def api_sort_key(filename):
    stem = os.path.splitext(filename)[0]
    parts = re.split(r'(\d+)', stem.lower())
    return [int(p) if p.isdigit() else p for p in parts]


def non_sql_sort_key(filename):
    stem = os.path.splitext(filename)[0]

    m = re.match(r'^(Page_.+?)_(\d+)_(.+)$', stem, flags=re.IGNORECASE)
    if m:
        prefix = m.group(1).lower()
        idx = int(m.group(2))
        rest = m.group(3).lower()
        return (0, prefix, idx, rest)

    m = re.match(r'^(Module_.+?)_(\d+)_(.+)$', stem, flags=re.IGNORECASE)
    if m:
        prefix = m.group(1).lower()
        idx = int(m.group(2))
        rest = m.group(3).lower()
        return (1, prefix, idx, rest)

    parts = re.split(r'(\d+)', stem.lower())
    natural = [int(p) if p.isdigit() else p for p in parts]
    return (2, *natural)

def process_folder(folder_path, section_name, toc_lines, body_content, is_module=False):
    """
    Reads each .md/.txt file and creates a TOC entry and anchor for every H1 header
    inside the file.
    """
    if not folder_path or not os.path.exists(folder_path):
        print(f"Warning: Folder '{folder_path}' not found. Skipping.")
        return

    try:
        files = [f for f in os.listdir(folder_path) if f.lower().endswith((".md", ".txt"))]
    except Exception as e:
        print(f"Error reading folder '{folder_path}': {e}")
        return

    if "database reference (sql)" in section_name.lower():
        files.sort(key=sql_sort_key)
    elif "api reference" in section_name.lower():
        files.sort(key=api_sort_key)
    else:
        files.sort(key=non_sql_sort_key)

    if not files:
        print(f"No files found in '{folder_path}'.")
        return

    if is_module:
        kind_label = section_name if "module" in section_name.lower() else section_name + " (Modules)"
    else:
        kind_label = section_name

    print(f"Processing '{kind_label}' ({len(files)} files) from '{folder_path}'...")

    toc_lines.append(f"\n### {kind_label}")
    body_content.append(f"\n## {kind_label}\n\n")

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

        header_iter = list(re.finditer(r'^\s*#\s+(.+)$', content, flags=re.MULTILINE))
        if not header_iter:
            title = clean_title(base_name) or base_name
            slug_raw = make_slug(kind_label, base_name, 1, title)
            slug = _ensure_unique_slug(slug_raw)
            toc_lines.append(f"- [{title}](#{slug})")
            body_content.append(f"\n<a id='{slug}'></a>\n")
            body_content.append(normalize_whitespace(content.strip()))
            body_content.append("\n\n---\n\n")
            continue

        sections = []
        for i, m in enumerate(header_iter):
            start = m.start()
            end = header_iter[i + 1].start() if i + 1 < len(header_iter) else len(content)
            header_text = m.group(1).strip()
            section_text = content[start:end].rstrip()
            sections.append((header_text, section_text))

        for idx, (header_text, section_text) in enumerate(sections, start=1):
            title = base_name
            slug_raw = make_slug(kind_label, base_name, idx, title)
            slug = _ensure_unique_slug(slug_raw)
            toc_lines.append(f"- [{title}](#{slug})")
            body_content.append(f"\n<a id='{slug}'></a>\n")

            section_text = re.sub(
                r'^\s*#\s+.*$',
                f"# {title}",
                section_text,
                count=1,
                flags=re.MULTILINE
            )

            body_content.append(normalize_whitespace(section_text.strip()))
            body_content.append("\n\n---\n\n")


def find_folder(folder_name):
    """
    Locate folder_name in a set of reasonable places.
    """
    base = os.path.abspath(os.path.dirname(__file__))
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

    for root, dirs, files in os.walk(base):
        if folder_name in dirs:
            found = os.path.join(root, folder_name)
            print(f"Found '{folder_name}' by walking: {found}")
            return found

    print(f"Folder '{folder_name}' not found under '{base}'")
    return None


def _get_zip_basename():
    """
    Try to determine the originating zip filename.
    """
    candidates = ["ANALYZER_ZIP_FILENAME", "ANALYZER_ZIP", "ZIP_FILENAME", "ZIPFILE", "ZIPNAME"]
    for k in candidates:
        v = os.environ.get(k)
        if v:
            return os.path.splitext(os.path.basename(v))[0]

    try:
        uploads = os.path.join(BACKEND_DIR, "uploads")
        if os.path.isdir(uploads):
            zips = [os.path.join(uploads, f) for f in os.listdir(uploads) if f.lower().endswith(".zip")]
            if zips:
                zips.sort(key=lambda p: os.path.getmtime(p), reverse=True)
                return os.path.splitext(os.path.basename(zips[0]))[0]
    except Exception:
        pass

    return None


def main():
    _USED_SLUGS.clear()

    zip_base = _get_zip_basename()
    if zip_base:
        title_line = f"# {zip_base} - Technical Documentation"
    else:
        title_line = "# Technical Documentation"

    toc_lines = [title_line, "", "## Table of Contents"]
    body_content = []

    docs_path = find_folder(DOCS_FOLDER)
    util_path = find_folder(UTIL_FOLDER)
    util_sql_path = find_folder(UTIL_SQL_FOLDER)
    sql_path = find_folder(SQL_FOLDER)
    api_path = find_folder(API_FOLDER)

    if docs_path:
        process_folder(docs_path, "Web Pages", toc_lines, body_content, is_module=False)
    else:
        print(f"No documentation chapters found (expected folder '{DOCS_FOLDER}').")

    if util_path:
        process_folder(util_path, "Modules/Others", toc_lines, body_content, is_module=True)
    else:
        print(f"No utility/module chapters found (expected folder '{UTIL_FOLDER}').")

    if util_sql_path:
        process_folder(util_sql_path, "Modules/Others (SQL-Aware)", toc_lines, body_content, is_module=True)
    else:
        print(f"No SQL-aware utility/module chapters found (expected folder '{UTIL_SQL_FOLDER}').")

    if sql_path:
        process_folder(sql_path, "Database Reference (SQL)", toc_lines, body_content, is_module=False)
    else:
        print(f"No SQL docs found (expected folder '{SQL_FOLDER}').")

    if api_path:
        process_folder(api_path, "API Reference", toc_lines, body_content, is_module=False)
    else:
        print(f"No API docs found (expected folder '{API_FOLDER}').")

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