import os
import re
import json
import shutil
import textwrap
import socket
import subprocess
import time
from collections import Counter
from langchain_community.llms import Ollama
from urllib.parse import urlparse

# --- CONFIGURATION ---
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
PROMPTS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")
ANALYSIS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "analysis_output")

INPUT_OUTPUT_PAIRS = [
    ("Page_Documentation_Prompts", "Final_Documentation_Chapters"),
    ("Utility_Documentation_Prompts", "Final_Utility_Chapters"),
    ("Utility_SQL_Documentation_Prompts", "Final_Utility_SQL_Chapters"),
    ("HTML_Documentation_Prompts", "Final_HTML_Docs"),
    ("JS_Documentation_Prompts", "Final_JS_Docs"),
]

DEFAULT_MODEL = "gemma3:latest"
MODEL_NAME = os.environ.get("ANALYSIS_MODEL", DEFAULT_MODEL)
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
MAX_RETRIES = 3


# ---------------------------
# General helpers
# ---------------------------
def _is_port_open(host: str, port: int) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.8)
    try:
        s.connect((host, port))
        s.close()
        return True
    except Exception:
        return False


def ensure_ollama_running(model: str) -> None:
    base_url = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
    parsed = urlparse(base_url)

    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or 11434

    if _is_port_open(host, port):
        return

    ollama_path = shutil.which("ollama")
    if not ollama_path:
        raise RuntimeError(
            "`ollama` CLI not found on PATH. Install Ollama and ensure `ollama` is available."
        )

    try:
        subprocess.run(
            [ollama_path, "pull", model],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False
        )
    except Exception:
        pass

    server_cmds = [["serve"], ["daemon"], ["run", "serve"]]

    for cmd in server_cmds:
        try:
            proc = subprocess.Popen(
                [ollama_path] + cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except FileNotFoundError:
            continue

        deadline = time.time() + 30

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


def clean_response(text: str) -> str:
    text = text or ""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    text = re.sub(r"```[a-zA-Z]*\n?", "", text)
    text = re.sub(r"\n```", "", text)
    text = re.sub(
        r"^\s*(Okay|Sure|Here is|Here’s|Below is|Let me|I have)\b.*?\n",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\n*(Do you want me to .*|Would you like me to .*|Let me know if .*|I can also .*?)\s*$",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return text.strip()


def normalize_unicode_bullets(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")

    replacements = {
        "•": "*",
        "◦": "*",
        "▪": "*",
        "‣": "*",
        "–": "-",
        "—": "-",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)

    text = re.sub(r"(?im)^\s*[*-]?\s*Reads\s*:\s*(.*)$", r"* **Reads:** \1", text)
    text = re.sub(r"(?im)^\s*[*-]?\s*Writes\s*:\s*(.*)$", r"* **Writes:** \1", text)

    text = re.sub(r"(?im)^\s*[*-]?\s*Exports\s*:\s*(.*)$", r"* **Exports:** \1", text)
    text = re.sub(r"(?im)^\s*[*-]?\s*External Dependencies\s*:\s*(.*)$", r"* **External Dependencies:** \1", text)
    text = re.sub(r"(?im)^\s*[*-]?\s*Side Effects\s*:\s*(.*)$", r"* **Side Effects:** \1", text)

    return text


def strip_js_prompt_leakage(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")

    leakage_patterns = [
        r"(?im)^\s*[*•-]?\s*Summarize selectors, DOM queries, and visible DOM update behavior if present\.\s*$",
        r"(?im)^\s*[*•-]?\s*Summarize fetch / axios / jQuery AJAX calls and likely targets if present\.\s*$",
        r"(?im)^\s*[*•-]?\s*If none, write exactly: Not clearly indicated\.\s*$",
        r"(?im)^\s*[*•-]?\s*Only include meaningful page lifecycle handlers.*$",
    ]

    for pat in leakage_patterns:
        text = re.sub(pat, "", text)

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def detect_prompt_type(prompt_text: str) -> str:
    t = (prompt_text or "").lower()

    if "**jstitle:**" in t:
        return "javascript"
    if "**htmltitle:**" in t:
        return "html"
    if "**pagetitle:**" in t:
        return "page"
    if "**moduletitle:**" in t:
        return "module"

    if "output format" in t and "# javascript file:" in t:
        return "javascript"
    if "output format" in t and "# html page:" in t:
        return "html"
    if "output format" in t and "# page:" in t:
        return "page"
    if "output format" in t and "# module:" in t:
        return "module"

    return "unknown"


def extract_expected_title(prompt_text: str, prompt_type: str) -> str:
    metadata_map = {
        "page": "PageTitle",
        "module": "ModuleTitle",
        "html": "HtmlTitle",
        "javascript": "JsTitle",
    }

    field = metadata_map.get(prompt_type)
    if field:
        m = re.search(
            rf"(?im)^\*\*{re.escape(field)}:\*\*[ \t]*([^\n]+)$",
            prompt_text,
        )
        if m:
            return m.group(1).strip()

    fallback_patterns = {
        "page": r"(?im)^#\s*Page\s*:[ \t]*([^\n]+)$",
        "module": r"(?im)^#\s*Module\s*:[ \t]*([^\n]+)$",
        "html": r"(?im)^#\s*HTML Page\s*:[ \t]*([^\n]+)$",
        "javascript": r"(?im)^#\s*JavaScript File\s*:[ \t]*([^\n]+)$",
    }

    pat = fallback_patterns.get(prompt_type)
    if pat:
        m = re.search(pat, prompt_text)
        if m:
            return m.group(1).strip()

    return "Unknown"


def _strip_existing_header_lines(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")

    patterns = [
        r"^\s*#\s*Page\s*:.*$\n?",
        r"^\s*#\s*Module\s*:.*$\n?",
        r"^\s*#\s*HTML Page\s*:.*$\n?",
        r"^\s*#\s*JavaScript File\s*:.*$\n?",
        r"^\s*\*\*Web Page File:\*\*.*$\n?",
        r"^\s*\*\*Web Page Path:\*\*.*$\n?",
        r"^\s*\*\*Code-Behind File:\*\*.*$\n?",
        r"^\s*\*\*Code-Behind Path:\*\*.*$\n?",
        r"^\s*\*\*File:\*\*.*$\n?",
        r"^\s*\*\*Path:\*\*.*$\n?",
        r"^\s*File:.*$\n?",
        r"^\s*Path:.*$\n?",
    ]

    for pat in patterns:
        text = re.sub(pat, "", text, flags=re.IGNORECASE | re.MULTILINE)

    return text.strip()


def extract_expected_field(prompt_text: str, field_name: str) -> str:
    m = re.search(
        rf"(?im)^\*\*{re.escape(field_name)}:\*\*[ \t]*([^\n]*)$",
        prompt_text,
    )
    if not m:
        return ""

    value = m.group(1).strip()
    if value.startswith("**") or value.startswith("###"):
        return ""
    return value


def replace_page_header_with_source(text: str, fields: dict) -> str:
    body = _strip_existing_header_lines(text)

    cb_file = (fields.get("codebehind_file") or "").strip()
    cb_path = (fields.get("codebehind_path") or "").strip()

    header = (
        f"# Page: {fields['expected_title']}\n"
        f"**Web Page File:** {fields['page_file']}  \n"
        f"**Web Page Path:** {fields['page_path']}  \n"
        f"**Code-Behind File:** {cb_file}  \n"
        f"**Code-Behind Path:** {cb_path}"
    )

    return f"{header}\n\n{body}".strip() if body else header


def replace_module_header_with_source(text: str, fields: dict) -> str:
    body = _strip_existing_header_lines(text)

    header = (
        f"# Module: {fields['expected_title']}\n"
        f"**File:** {fields['file']}  \n"
        f"**Path:** {fields['path']}"
    )

    return f"{header}\n\n{body}".strip() if body else header


def replace_html_header_with_source(text: str, fields: dict) -> str:
    body = _strip_existing_header_lines(text)

    header = (
        f"# HTML Page: {fields['expected_title']}\n"
        f"**File:** {fields['file']}  \n"
        f"**Path:** {fields['path']}"
    )

    return f"{header}\n\n{body}".strip() if body else header


def replace_js_header_with_source(text: str, fields: dict) -> str:
    body = _strip_existing_header_lines(text)

    header = (
        f"# JavaScript File: {fields['expected_title']}\n"
        f"**File:** {fields['file']}  \n"
        f"**Path:** {fields['path']}"
    )

    return f"{header}\n\n{body}".strip() if body else header


def replace_header_with_source(text: str, prompt_type: str, fields: dict) -> str:
    if prompt_type == "page":
        return replace_page_header_with_source(text, fields)
    if prompt_type == "module":
        return replace_module_header_with_source(text, fields)
    if prompt_type == "html":
        return replace_html_header_with_source(text, fields)
    if prompt_type == "javascript":
        return replace_js_header_with_source(text, fields)

    body = _strip_existing_header_lines(text)
    title = fields.get("expected_title", "Unknown")
    file_val = fields.get("file", fields.get("page_file", "Unknown"))
    path_val = fields.get("path", fields.get("page_path", "Unknown"))

    header = (
        f"# {title}\n"
        f"**File:** {file_val}  \n"
        f"**Path:** {path_val}"
    )

    return f"{header}\n\n{body}".strip() if body else header


def enforce_output_template(text: str, prompt_type: str, expected_title: str) -> str:
    text = (text or "").strip()

    if prompt_type == "page":
        if re.search(r"^\s*#+\s*Page\s*:", text, flags=re.IGNORECASE | re.MULTILINE):
            text = re.sub(
                r"^\s*#+\s*Page\s*:.*$",
                f"# Page: {expected_title}",
                text,
                count=1,
                flags=re.IGNORECASE | re.MULTILINE,
            )
        else:
            text = f"# Page: {expected_title}\n\n{text}"

    elif prompt_type == "module":
        if re.search(r"^\s*#+\s*Module\s*:", text, flags=re.IGNORECASE | re.MULTILINE):
            text = re.sub(
                r"^\s*#+\s*Module\s*:.*$",
                f"# Module: {expected_title}",
                text,
                count=1,
                flags=re.IGNORECASE | re.MULTILINE,
            )
        else:
            text = f"# Module: {expected_title}\n\n{text}"

    elif prompt_type == "html":
        if re.search(r"^\s*#+\s*HTML\s*Page\s*:", text, flags=re.IGNORECASE | re.MULTILINE):
            text = re.sub(
                r"^\s*#+\s*HTML\s*Page\s*:.*$",
                f"# HTML Page: {expected_title}",
                text,
                count=1,
                flags=re.IGNORECASE | re.MULTILINE,
            )
        else:
            text = f"# HTML Page: {expected_title}\n\n{text}"

    elif prompt_type == "javascript":
        if re.search(r"^\s*#+\s*JavaScript\s*File\s*:", text, flags=re.IGNORECASE | re.MULTILINE):
            text = re.sub(
                r"^\s*#+\s*JavaScript\s*File\s*:.*$",
                f"# JavaScript File: {expected_title}",
                text,
                count=1,
                flags=re.IGNORECASE | re.MULTILINE,
            )
        else:
            text = f"# JavaScript File: {expected_title}\n\n{text}"

    return text.strip()


def count_expected_items_in_prompt(prompt_text: str) -> int:
    return 1


def count_sections_in_output(text: str):
    if not text:
        return 0
    return (
        len(re.findall(r"^\s*#+\s*Page\s*:", text, flags=re.MULTILINE))
        + len(re.findall(r"^\s*#+\s*Module\s*:", text, flags=re.MULTILINE))
        + len(re.findall(r"^\s*#+\s*HTML\s*Page\s*:", text, flags=re.MULTILINE))
        + len(re.findall(r"^\s*#+\s*JavaScript\s*File\s*:", text, flags=re.MULTILINE))
    )


# ---------------------------
# Duplicate / junk detection
# ---------------------------
def detect_excessive_duplicate_lines(text, min_line_len=25, duplicate_threshold=6, dominance_threshold=0.35):
    raw_lines = [ln.strip() for ln in (text or "").splitlines()]
    raw_lines = [ln for ln in raw_lines if ln and len(ln) >= min_line_len]

    if not raw_lines:
        return False, "No meaningful lines"

    normalized = []
    for ln in raw_lines:
        ln2 = re.sub(r'^\s*(?:\d+[\.\)]\s*|[-*]\s+)', '', ln).strip()
        normalized.append(ln2)

    counts = Counter(normalized)
    _, most_common_count = counts.most_common(1)[0]

    if most_common_count >= duplicate_threshold:
        return True, f"Too many duplicated lines ({most_common_count}/{len(normalized)})"

    duplicated_total = sum(c for _, c in counts.items() if c > 1)
    if duplicated_total / len(normalized) > dominance_threshold:
        return True, f"Too many duplicated lines ({duplicated_total}/{len(normalized)})"

    return False, "OK"


def detect_repeated_line_chunks(text: str, window_size: int = 3, repeat_threshold: int = 3):
    lines = [ln.strip() for ln in (text or "").splitlines()]
    lines = [ln for ln in lines if ln]

    if len(lines) < window_size * 2:
        return False, "Not enough lines for chunk check"

    normalized = []
    for ln in lines:
        ln = re.sub(r'^\s*(?:\d+[\.\)]\s*|[-*]\s+)', '', ln).strip()
        ln = re.sub(r'\s+', ' ', ln)
        normalized.append(ln)

    chunks = []
    for i in range(len(normalized) - window_size + 1):
        chunk = "\n".join(normalized[i:i + window_size])
        chunks.append(chunk)

    counts = Counter(chunks)
    _, most_common_count = counts.most_common(1)[0]

    if most_common_count >= repeat_threshold:
        return True, f"Repeated line chunk detected {most_common_count} times"

    return False, "OK"


def detect_duplicate_table_rows(text, threshold=6):
    rows = re.findall(r"^\|.*\|$", text or "", flags=re.MULTILINE)
    rows = [r.strip() for r in rows if ":---" not in r]

    if not rows:
        return False, "No table rows"

    counts = Counter(rows)
    _, worst_count = counts.most_common(1)[0]
    if worst_count >= threshold:
        return True, f"Duplicate table row repeated {worst_count} times"

    return False, "OK"


def _normalize_markdown_table_row(row: str) -> str:
    row = (row or "").strip()
    row = re.sub(r"\s+", " ", row)
    parts = [p.strip() for p in row.strip("|").split("|")]
    return " | ".join(parts)


def _extract_section_body(text: str, section_title_regex: str, next_section_regex: str | None = None) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")

    if next_section_regex:
        pat = rf"(?is)^\s*(?:#+\s*)?{section_title_regex}\b(.*?)(?=^\s*(?:#+\s*)?{next_section_regex}\b|\Z)"
    else:
        pat = rf"(?is)^\s*(?:#+\s*)?{section_title_regex}\b(.*)$"

    m = re.search(pat, text, flags=re.MULTILINE)
    return m.group(1).strip() if m else ""


def detect_duplicate_rows_in_section(
    text: str,
    section_title_regex: str,
    next_section_regex: str | None = None,
    min_repeat: int = 2,
):
    body = _extract_section_body(text, section_title_regex, next_section_regex)
    if not body:
        return False, "No section body", []

    rows = re.findall(r"^\|.*\|$", body, flags=re.MULTILINE)
    normalized_rows = []
    for row in rows:
        row_norm = _normalize_markdown_table_row(row)
        if not row_norm:
            continue
        if re.fullmatch(r":?-{3,}:?( \| :?-{3,}:?)+", row_norm):
            continue
        normalized_rows.append(row_norm)

    if not normalized_rows:
        return False, "No table rows", []

    counts = Counter(normalized_rows)
    duplicates = [(row, count) for row, count in counts.items() if count >= min_repeat]
    if duplicates:
        duplicates.sort(key=lambda x: (-x[1], x[0]))
        return True, "Duplicate rows detected", duplicates

    return False, "OK", []


def detect_duplicate_js_key_functions(text: str):
    bad, _, duplicates = detect_duplicate_rows_in_section(
        text,
        r"2\.\s*Key\s*Functions",
        r"3\.\s*Event\s*Bindings",
        min_repeat=2,
    )
    if not bad:
        return False, "OK"

    labels = []
    for row, count in duplicates[:5]:
        parts = [p.strip() for p in row.split(" | ")]
        if len(parts) >= 2:
            labels.append(f"{parts[0]} ({parts[1]}) x{count}")
        else:
            labels.append(f"{row} x{count}")

    return True, "Duplicate key function rows detected: " + ", ".join(labels)


def detect_duplicate_js_event_bindings(text: str):
    bad, _, duplicates = detect_duplicate_rows_in_section(
        text,
        r"3\.\s*Event\s*Bindings",
        r"4\.\s*DOM\s*Interaction",
        min_repeat=2,
    )
    if not bad:
        return False, "OK"

    labels = []
    for row, count in duplicates[:5]:
        parts = [p.strip() for p in row.split(" | ")]
        if len(parts) >= 2:
            labels.append(f"{parts[0]} -> {parts[1]} x{count}")
        else:
            labels.append(f"{row} x{count}")

    return True, "Duplicate event binding rows detected: " + ", ".join(labels)


def contains_template_placeholders(text: str):
    text_lower = (text or "").lower()
    placeholder_phrases = [
        "one sentence describing user purpose",
        "one short paragraph describing",
        "| ... | ... |",
        "not specified | not specified",
        "if no functions are identified, write exactly",
        "if there are no forms or inputs, write exactly",
        "summarize fetch / axios / jquery ajax calls and likely targets if present.",
        "summarize selectors, dom queries, and visible dom update behavior if present.",
        "if no event bindings are identified, write exactly",
        "one short paragraph describing what this script appears to do based only on the extracted metadata.",
        "summarize important links, buttons, and inline-triggered actions.",
        "if forms or inputs exist, provide this table",
        "one short paragraph describing what the page appears to be for based only on visible structure and extracted metadata",
        "summarize the main query or stored procedure usage for each relevant method.",
        "kinds may include: method, function, class, attribute, constant, event, table, view, page handler, utility.",
        "one sentence describing user purpose — if unknown use exact text required.",
        "you have to check first",
        "document the page above. focus on user actions, key events/methods and data flow.",
        "do not list simple data-binding expressions",
        "only include meaningful page lifecycle handlers",
        "if there is no explicit domain or entity name visible in the input",
        "if unknown use exact text required."
    ]
    for phrase in placeholder_phrases:
        if phrase in text_lower:
            return phrase
    return None


def is_empty_semantic_value(value: str) -> bool:
    v = (value or "").strip().lower()
    if not v:
        return True

    empties = {
        "...",
        "…",
        "none",
        "not clearly indicated",
        "not specified",
        "unknown",
        "n/a",
        "na",
        "-",
    }
    return v in empties


def extract_labeled_value(text: str, label: str) -> str:
    m = re.search(
        rf"(?im)^\s*[*-]?\s*\*?\*?{re.escape(label)}\*?\*?\s*:\s*(.*?)\s*$",
        text,
    )
    return m.group(1).strip() if m else ""

def remove_standalone_horizontal_rules(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")

    # Replace --- style separators with a blank line
    text = re.sub(
        r"(?m)^\s*(?:-{3,}|\*{3,}|_{3,})\s*$",
        "",
        text,
    )

    # Ensure there is always a blank line before section headings
    text = re.sub(
        r"(?m)([^\n])\n(###\s*\d+\.)",
        r"\1\n\n\2",
        text,
    )

    # Normalize spacing
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def section_body_is_empty(text: str, section_title_regex: str, next_section_regex: str | None = None) -> bool:
    body = _extract_section_body(text, section_title_regex, next_section_regex)
    body = strip_js_prompt_leakage(body).strip()

    if not body:
        return True

    normalized = re.sub(r"\s+", " ", body.lower()).strip()

    valid_placeholder_outputs = {
        "not clearly indicated",
        "- not clearly indicated",
        "* not clearly indicated",
    }
    if normalized in valid_placeholder_outputs:
        return False

    # Remove markdown table separator rows and blank lines
    meaningful_lines = []
    for line in body.splitlines():
        s = line.strip()
        if not s:
            continue
        if re.fullmatch(r"\|?\s*:?-{3,}:?(?:\s*\|\s*:?-{3,}:?)*\s*\|?", s):
            continue
        meaningful_lines.append(s)

    if not meaningful_lines:
        return True

    # Consider sections empty if they only contain placeholder punctuation
    non_placeholder = [
        ln for ln in meaningful_lines
        if re.sub(r"[\|\-\*\:\.\s]", "", ln).strip()
    ]

    return len(non_placeholder) == 0


# ---------------------------
# Validators (ALL errors)
# ---------------------------
def validate_required_structure(text: str, prompt_type: str):
    errors = []
    text = (text or "").strip()
    text_lower = text.lower()

    if len(text) < 40:
        errors.append("Output empty or too short")

    if prompt_type == "page":
        checks = {
            "page header": r"^\s*#+\s*page\s*:",
            "web page file": r"^\s*\*\*web page file:\*\*",
            "web page path": r"^\s*\*\*web page path:\*\*",
            "code-behind file": r"^\s*\*\*code-behind file:\*\*",
            "code-behind path": r"^\s*\*\*code-behind path:\*\*",
            "user purpose": r"^\s*#+\s*1\.\s*user\s*purpose\b",
            "key events & logic": r"^\s*#+\s*2\.\s*key\s*events\s*&\s*logic\b",
            "data interactions": r"^\s*#+\s*3\.\s*data\s*interactions\b",
        }
        for name, pattern in checks.items():
            if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                errors.append(f"Missing required section: {name}")

        if "| Event / Method | Business Logic Summary |" not in text:
            errors.append("Missing events table")

        reads_val = extract_labeled_value(text, "Reads")
        writes_val = extract_labeled_value(text, "Writes")

        if not reads_val:
            errors.append("Data interactions missing Reads")
        elif is_empty_semantic_value(reads_val):
            errors.append("Data interactions Reads is empty")

        if not writes_val:
            errors.append("Data interactions missing Writes")
        elif is_empty_semantic_value(writes_val):
            errors.append("Data interactions Writes is empty")

    elif prompt_type == "module":
        checks = {
            "module header": r"^\s*#+\s*module\s*:",
            "file": r"^\s*\*\*file:\*\*",
            "path": r"^\s*\*\*path:\*\*",
            "purpose": r"^\s*#+\s*1\.\s*purpose\b",
            "key declarations": r"^\s*#+\s*2\.\s*key\s*declarations\b",
            "important behavior & side effects": r"^\s*#+\s*3\.\s*important\s*behavior\s*&\s*side\s*effects\b",
            "data interactions": r"^\s*#+\s*4\.\s*data\s*interactions\b",
        }
        for name, pattern in checks.items():
            if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                errors.append(f"Missing required section: {name}")

        if "| Symbol | Kind | Description |" not in text:
            errors.append("Missing declarations table")

        reads_val = extract_labeled_value(text, "Reads")
        writes_val = extract_labeled_value(text, "Writes")

        if not reads_val:
            errors.append("Data interactions missing Reads")
        elif is_empty_semantic_value(reads_val):
            errors.append("Data interactions Reads is empty")

        if not writes_val:
            errors.append("Data interactions missing Writes")
        elif is_empty_semantic_value(writes_val):
            errors.append("Data interactions Writes is empty")

    elif prompt_type == "html":
        checks = {
            "html page header": r"^\s*#+\s*html\s*page\s*:",
            "file": r"^\s*\*\*file:\*\*",
            "path": r"^\s*\*\*path:\*\*",
            "user purpose": r"^\s*#+\s*1\.\s*user\s*purpose\b",
            "main ui sections": r"^\s*#+\s*2\.\s*main\s*ui\s*sections\b",
            "forms and user inputs": r"^\s*#+\s*3\.\s*forms\s*and\s*user\s*inputs\b",
            "navigation and actions": r"^\s*#+\s*4\.\s*navigation\s*and\s*actions\b",
            "data display and visual regions": r"^\s*#+\s*5\.\s*data\s*display\s*and\s*visual\s*regions\b",
            "linked assets": r"^\s*#+\s*6\.\s*linked\s*assets\b",
        }
        for name, pattern in checks.items():
            if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                errors.append(f"Missing required section: {name}")

        if "| Section | Description |" not in text:
            errors.append("Missing main UI sections table")

    elif prompt_type == "javascript":
        checks = {
            "javascript file header": r"^\s*#+\s*javascript\s*file\s*:",
            "file": r"^\s*\*\*file:\*\*",
            "path": r"^\s*\*\*path:\*\*",
            "purpose": r"^\s*(?:#+\s*)?1\.\s*purpose\b",
            "key functions": r"^\s*(?:#+\s*)?2\.\s*key\s*functions\b",
            "event bindings": r"^\s*(?:#+\s*)?3\.\s*event\s*bindings\b",
            "dom interaction": r"^\s*(?:#+\s*)?4\.\s*dom\s*interaction\b",
            "api / network usage": r"^\s*(?:#+\s*)?5\.\s*api\s*/\s*network\s*usage\b",
            "side effects and dependencies": r"^\s*(?:#+\s*)?6\.\s*side\s*effects\s*and\s*dependencies\b",
        }
        for name, pattern in checks.items():
            if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                errors.append(f"Missing required section: {name}")

        functions_ok = "| Function | Type | Description |" in text or "Not clearly indicated" in text
        if not functions_ok:
            errors.append("Missing functions table")

        events_ok = "| Event / Trigger | Handler / Behavior |" in text or "Not clearly indicated" in text
        if not events_ok:
            errors.append("Missing event bindings table")

        if section_body_is_empty(text, r"3\.\s*Event Bindings", r"4\.\s*DOM Interaction"):
            errors.append("Event Bindings section is empty")

        if section_body_is_empty(text, r"4\.\s*DOM Interaction", r"5\.\s*API\s*/\s*Network Usage"):
            errors.append("DOM Interaction section is empty")

        if section_body_is_empty(text, r"5\.\s*API\s*/\s*Network Usage", r"6\.\s*Side Effects and Dependencies"):
            errors.append("API / Network Usage section is empty")

        exports_val = extract_labeled_value(text, "Exports")
        deps_val = extract_labeled_value(text, "External Dependencies")
        side_val = extract_labeled_value(text, "Side Effects")

        if not exports_val:
            errors.append("Side effects and dependencies missing Exports")
        elif is_empty_semantic_value(exports_val):
            errors.append("Exports is empty")

        if not deps_val:
            errors.append("Side effects and dependencies missing External Dependencies")
        elif is_empty_semantic_value(deps_val):
            errors.append("External Dependencies is empty")

        if not side_val:
            errors.append("Side effects and dependencies missing Side Effects")
        elif is_empty_semantic_value(side_val):
            errors.append("Side Effects is empty")

    placeholder = contains_template_placeholders(text)
    if placeholder:
        errors.append(f"Output still contains template placeholder text: '{placeholder}'")

    tail = text_lower[-400:]
    for p in ["do you want me to", "would you like me to", "let me know if", "i can also"]:
        if p in tail:
            errors.append("Detected conversational ending")
            break

    dup_bad, dup_reason = detect_excessive_duplicate_lines(text)
    if dup_bad:
        errors.append(dup_reason)

    chunk_bad, chunk_reason = detect_repeated_line_chunks(text)
    if chunk_bad:
        errors.append(chunk_reason)

    table_bad, table_reason = detect_duplicate_table_rows(text)
    if table_bad:
        errors.append(table_reason)

    return (len(errors) == 0), errors


# ---------------------------
# Auto-repair helpers
# ---------------------------
def repair_page_structure(text: str, expected_title: str, page_file: str, page_path: str, cb_file: str, cb_path: str) -> str:
    text = enforce_output_template(text, "page", expected_title)

    if not re.search(r"^\s*\*\*Web Page File:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
        text = re.sub(
            r"(^\s*#\s*Page:.*$)",
            lambda m: (
                f"{m.group(1)}\n"
                f"**Web Page File:** {page_file}\n"
                f"**Web Page Path:** {page_path}\n"
                f"**Code-Behind File:** {cb_file}\n"
                f"**Code-Behind Path:** {cb_path}"
            ),
            text,
            count=1,
            flags=re.IGNORECASE | re.MULTILINE,
        )
    else:
        if not re.search(r"^\s*\*\*Web Page Path:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
            text = re.sub(r"(^\s*\*\*Web Page File:\*\*.*$)", rf"\1\n**Web Page Path:** {page_path}", text, count=1, flags=re.MULTILINE)
        if not re.search(r"^\s*\*\*Code-Behind File:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
            text = re.sub(r"(^\s*\*\*Web Page Path:\*\*.*$)", rf"\1\n**Code-Behind File:** {cb_file}", text, count=1, flags=re.MULTILINE)
        if not re.search(r"^\s*\*\*Code-Behind Path:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
            text = re.sub(
                r"(^\s*\*\*Code-Behind File:\*\*.*$)",
                lambda m: f"{m.group(1)}\n**Code-Behind Path:** {cb_path}",
                text,
                count=1,
                flags=re.MULTILINE,
            )
    if not re.search(r"^\s*#+\s*1\.\s*User Purpose\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 1. User Purpose\nThis page's user purpose is Unknown (no explicit domain information in the code)."

    if not re.search(r"^\s*#+\s*2\.\s*Key Events\s*&\s*Logic\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 2. Key Events & Logic\n| Event / Method | Business Logic Summary |\n| :--- | :--- |\n| Not clearly indicated | Not clearly indicated |"

    if not re.search(r"^\s*#+\s*3\.\s*Data Interactions\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 3. Data Interactions\n* **Reads:** Not clearly indicated\n* **Writes:** Not clearly indicated"
    else:
        if "**Reads:**" not in text:
            text += "\n* **Reads:** Not clearly indicated"
        if "**Writes:**" not in text:
            text += "\n* **Writes:** Not clearly indicated"

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def repair_module_structure(text: str, expected_title: str, file_value: str, path_value: str) -> str:
    text = enforce_output_template(text, "module", expected_title)

    if not re.search(r"^\s*\*\*File:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
        text = re.sub(
            r"(^\s*#\s*Module:.*$)",
            lambda m: f"{m.group(1)}\n**File:** {file_value}\n**Path:** {path_value}",
            text,
            count=1,
            flags=re.IGNORECASE | re.MULTILINE,
        )
    elif not re.search(r"^\s*\*\*Path:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
        text = re.sub(
            r"(^\s*\*\*File:\*\*.*$)",
            lambda m: f"{m.group(1)}\n**Path:** {path_value}",
            text,
            count=1,
            flags=re.MULTILINE,
        )

    if not re.search(r"^\s*#+\s*1\.\s*Purpose\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 1. Purpose\nNot clearly indicated"
    if not re.search(r"^\s*#+\s*2\.\s*Key Declarations\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 2. Key Declarations\n| Symbol | Kind | Description |\n| :--- | :--- | :--- |\n| Not clearly indicated | Not clearly indicated | Not clearly indicated |"
    if not re.search(r"^\s*#+\s*3\.\s*Important Behavior\s*&\s*Side Effects\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 3. Important Behavior & Side Effects\n- Not clearly indicated"
    if not re.search(r"^\s*#+\s*4\.\s*Data Interactions\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 4. Data Interactions\n* **Reads:** None at runtime\n* **Writes:** None at runtime"
    else:
        if "**Reads:**" not in text:
            text += "\n* **Reads:** None at runtime"
        if "**Writes:**" not in text:
            text += "\n* **Writes:** None at runtime"

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def repair_html_structure(text: str, expected_title: str, file_value: str, path_value: str) -> str:
    text = enforce_output_template(text, "html", expected_title)

    if not re.search(r"^\s*\*\*File:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
        text = re.sub(
            r"(^\s*#\s*HTML Page:.*$)",
            lambda m: f"{m.group(1)}\n**File:** {file_value}\n**Path:** {path_value}",
            text,
            count=1,
            flags=re.IGNORECASE | re.MULTILINE,
        )
    elif not re.search(r"^\s*\*\*Path:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
        text = re.sub(
            r"(^\s*\*\*File:\*\*.*$)",
            lambda m: f"{m.group(1)}\n**Path:** {path_value}",
            text,
            count=1,
            flags=re.MULTILINE,
        )

    if not re.search(r"^\s*#+\s*1\.\s*User Purpose\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 1. User Purpose\nNot clearly indicated"
    if not re.search(r"^\s*#+\s*2\.\s*Main UI Sections\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 2. Main UI Sections\n| Section | Description |\n| :--- | :--- |\n| Not clearly indicated | Not clearly indicated |"
    if not re.search(r"^\s*#+\s*3\.\s*Forms and User Inputs\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 3. Forms and User Inputs\nNot clearly indicated"
    if not re.search(r"^\s*#+\s*4\.\s*Navigation and Actions\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 4. Navigation and Actions\n- Not clearly indicated"
    if not re.search(r"^\s*#+\s*5\.\s*Data Display and Visual Regions\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 5. Data Display and Visual Regions\n- Not clearly indicated"
    if not re.search(r"^\s*#+\s*6\.\s*Linked Assets\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 6. Linked Assets\n* **Scripts:** Not clearly indicated\n* **Styles / Links:** Not clearly indicated\n* **Images / Other Assets:** Not clearly indicated"

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def repair_js_structure(text: str, expected_title: str, file_value: str, path_value: str) -> str:
    text = enforce_output_template(text, "javascript", expected_title)

    if not re.search(r"^\s*\*\*File:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
        text = re.sub(
            r"(^\s*#\s*JavaScript File:.*$)",
            lambda m: f"{m.group(1)}\n**File:** {file_value}\n**Path:** {path_value}",
            text,
            count=1,
            flags=re.IGNORECASE | re.MULTILINE,
        )
    elif not re.search(r"^\s*\*\*Path:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
        text = re.sub(
            r"(^\s*\*\*File:\*\*.*$)",
            lambda m: f"{m.group(1)}\n**Path:** {path_value}",
            text,
            count=1,
            flags=re.MULTILINE,
        )

    if not re.search(r"^\s*(?:#+\s*)?1\.\s*Purpose\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 1. Purpose\nNot clearly indicated"
    if not re.search(r"^\s*(?:#+\s*)?2\.\s*Key Functions\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 2. Key Functions\nNot clearly indicated"
    if not re.search(r"^\s*(?:#+\s*)?3\.\s*Event Bindings\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 3. Event Bindings\nNot clearly indicated"
    if not re.search(r"^\s*(?:#+\s*)?4\.\s*DOM Interaction\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 4. DOM Interaction\n- Not clearly indicated"
    if not re.search(r"^\s*(?:#+\s*)?5\.\s*API / Network Usage\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 5. API / Network Usage\n- Not clearly indicated"
    if not re.search(r"^\s*(?:#+\s*)?6\.\s*Side Effects and Dependencies\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### 6. Side Effects and Dependencies\n* **Exports:** Not clearly indicated\n* **External Dependencies:** Not clearly indicated\n* **Side Effects:** Not clearly indicated"

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def auto_repair_structure(text: str, prompt_type: str, fields: dict) -> str:
    if prompt_type == "page":
        return repair_page_structure(
            text,
            fields["expected_title"],
            fields["page_file"],
            fields["page_path"],
            fields["codebehind_file"],
            fields["codebehind_path"],
        )
    if prompt_type == "module":
        return repair_module_structure(text, fields["expected_title"], fields["file"], fields["path"])
    if prompt_type == "html":
        return repair_html_structure(text, fields["expected_title"], fields["file"], fields["path"])
    if prompt_type == "javascript":
        return repair_js_structure(text, fields["expected_title"], fields["file"], fields["path"])
    return text

def normalize_html_linked_assets_section(text: str) -> str:
    """
    Preserve multiline Linked Assets bullets.
    Only inject 'Not clearly indicated' when a label truly has no inline value
    and no child bullet/indented content.
    """
    if not text:
        return text

    pattern = re.compile(
        r"(###\s*6\.\s*Linked\s*Assets\s*\n)(.*?)(?=\n###\s*\d+\.|\Z)",
        re.IGNORECASE | re.DOTALL,
    )

    labels = [
        "Scripts",
        "Styles / Links",
        "Images / Other Assets",
    ]

    def is_label_line(s: str) -> bool:
        s = s.strip()
        for label in labels:
            if re.match(rf"^\*\s*\*\*{re.escape(label)}:\*\*", s, flags=re.IGNORECASE):
                return True
        return False

    def repl(match: re.Match) -> str:
        header = match.group(1)
        body = match.group(2).replace("\r\n", "\n").replace("\r", "\n")
        lines = body.splitlines()

        output = []
        seen = set()
        i = 0

        while i < len(lines):
            line = lines[i]
            stripped = line.strip()

            matched_label = None
            inline_value = None

            for label in labels:
                m = re.match(
                    rf"^\*\s*\*\*{re.escape(label)}:\*\*\s*(.*)$",
                    stripped,
                    flags=re.IGNORECASE,
                )
                if m:
                    matched_label = label
                    inline_value = (m.group(1) or "").strip()
                    break

            if not matched_label:
                if stripped.lower() == "not clearly indicated":
                    i += 1
                    continue
                output.append(line)
                i += 1
                continue

            seen.add(matched_label)

            # gather child lines until next label or next section
            child_lines = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                nxt_stripped = nxt.strip()

                if re.match(r"^###\s*\d+\.", nxt_stripped):
                    break
                if is_label_line(nxt):
                    break

                child_lines.append(nxt)
                j += 1

            meaningful_child_lines = [ln for ln in child_lines if ln.strip()]

            if inline_value:
                output.append(f"* **{matched_label}:** {inline_value}")
                output.extend(meaningful_child_lines)
            else:
                if meaningful_child_lines:
                    # Preserve multiline content exactly
                    output.append(f"* **{matched_label}:**")
                    output.extend(meaningful_child_lines)
                else:
                    output.append(f"* **{matched_label}:** Not clearly indicated")

            i = j

        for label in labels:
            if label not in seen:
                output.append(f"* **{label}:** Not clearly indicated")

        return header + "\n".join(output).rstrip() + "\n"

    return pattern.sub(repl, text)

def is_minor_only(errors: list[str]) -> bool:
    if not errors:
        return False

    major_markers = [
        "Output empty or too short",
        "Detected conversational ending",
        "Too many duplicated lines",
        "Repeated line chunk detected",
        "Duplicate table row repeated",
        "Duplicate key function rows detected",
        "Duplicate event binding rows detected",
        "Missing events table",
        "Missing declarations table",
        "Missing main UI sections table",
        "Missing functions table",
        "Missing event bindings table",
        "Output still contains template placeholder text",
        "Event Bindings section is empty",
        "DOM Interaction section is empty",
        "API / Network Usage section is empty",
        "Exports is empty",
        "External Dependencies is empty",
        "Side Effects is empty",
        "Data interactions Reads is empty",
        "Data interactions Writes is empty",
        "Data interactions missing Reads",
        "Data interactions missing Writes"
    ]
    for e in errors:
        if any(marker in e for marker in major_markers):
            return False
    return True


# ---------------------------
# Retry prompt
# ---------------------------
def build_retry_prompt(cleaned: str, original_prompt: str, prompt_type: str, errors: list[str]) -> str:
    error_text = "\n".join(f"- {e}" for e in errors)

    type_hint = {
        "page": "Preserve correct page fields and table structure.",
        "module": "Preserve correct module fields and declaration table structure.",
        "html": "Preserve correct HTML page fields and section structure.",
        "javascript": "Preserve correct JavaScript file fields and section structure.",
    }.get(prompt_type, "")

    return textwrap.dedent(f"""
    Your previous output failed validation.

    Fix ALL of these issues:
    {error_text}

    IMPORTANT RULES:
    - Preserve any already-correct sections.
    - Do NOT remove existing correct tables.
    - Only add or correct what is necessary.
    - Return ONE complete corrected document only.
    - Do NOT include explanations.
    - Do NOT include code blocks.
    - Do NOT include prompt instructions in the answer.
    - Do NOT output title, file, or path lines. They are generated automatically.
    - {type_hint}

    ### CURRENT DRAFT
    {cleaned}

    ### ORIGINAL INPUT
    {original_prompt}
    """).strip()


# ---------------------------
# Fallback templates
# ---------------------------
def build_fallback(prompt_type: str, fields: dict) -> str:
    if prompt_type == "page":
        return """### 1. User Purpose
Generation failed after 3 attempts.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Unknown | Generation failed |

### 3. Data Interactions
* **Reads:** Not clearly indicated
* **Writes:** Not clearly indicated
"""

    if prompt_type == "module":
        return """### 1. Purpose
Generation failed after 3 attempts.

### 2. Key Declarations
| Symbol | Kind | Description |
| :--- | :--- | :--- |
| Unknown | Unknown | Generation failed |

### 3. Important Behavior & Side Effects
- Unable to determine behavior due to repeated validation failure.

### 4. Data Interactions
* **Reads:** None at runtime
* **Writes:** None at runtime
"""

    if prompt_type == "html":
        return """### 1. User Purpose
Generation failed after 3 attempts.

### 2. Main UI Sections
| Section | Description |
| :--- | :--- |
| Unknown | Generation failed |

### 3. Forms and User Inputs
Not clearly indicated

### 4. Navigation and Actions
- Not clearly indicated

### 5. Data Display and Visual Regions
- Not clearly indicated

### 6. Linked Assets
* **Scripts:** Not clearly indicated
* **Styles / Links:** Not clearly indicated
* **Images / Other Assets:** Not clearly indicated
"""

    if prompt_type == "javascript":
        return """### 1. Purpose
Generation failed after 3 attempts.

### 2. Key Functions
Not clearly indicated

### 3. Event Bindings
Not clearly indicated

### 4. DOM Interaction
- Not clearly indicated

### 5. API / Network Usage
- Not clearly indicated

### 6. Side Effects and Dependencies
* **Exports:** Not clearly indicated
* **External Dependencies:** Not clearly indicated
* **Side Effects:** Not clearly indicated
"""
    return "Generation failed."


# ---------------------------
# Main
# ---------------------------
def main():
    print(f"Using model: {MODEL_NAME}")

    try:
        ensure_ollama_running(MODEL_NAME)
    except Exception as e:
        print(f"⚠️ Ollama not available: {e}")
        return

    llm = Ollama(
        model=MODEL_NAME,
        base_url=OLLAMA_BASE_URL,
        temperature=0.1,
        num_ctx=8192,
        num_predict=4096,
        stop=["<|eot_id|>", "### SYSTEM ROLE"],
    )

    for input_dir_name, output_dir_name in INPUT_OUTPUT_PAIRS:
        input_folder = os.path.join(PROMPTS_OUTPUT_BASE, input_dir_name)
        output_folder = os.path.join(ANALYSIS_OUTPUT_BASE, output_dir_name)

        print(f"\n=== Processing {input_dir_name} -> {output_dir_name} ===")

        if not os.path.isdir(input_folder):
            print(f"Skipping missing folder: {input_folder}")
            continue

        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)
        os.makedirs(output_folder, exist_ok=True)

        files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]
        files.sort()

        if not files:
            print(f"No prompt files found in '{input_folder}'.")
            continue

        for filename in files:
            out_path = os.path.join(output_folder, filename.replace(".txt", ".md"))

            print(f"\nProcessing {filename}...")
            with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
                original_prompt = f.read()

            prompt_type = detect_prompt_type(original_prompt)
            expected_title = extract_expected_title(original_prompt, prompt_type)

            fields = {"expected_title": expected_title}

            if prompt_type == "page":
                fields.update({
                    "page_file": extract_expected_field(original_prompt, "Web Page File"),
                    "page_path": extract_expected_field(original_prompt, "Web Page Path"),
                    "codebehind_file": extract_expected_field(original_prompt, "Code-Behind File"),
                    "codebehind_path": extract_expected_field(original_prompt, "Code-Behind Path"),
                })
            elif prompt_type in ("module", "html", "javascript"):
                fields.update({
                    "file": extract_expected_field(original_prompt, "File"),
                    "path": extract_expected_field(original_prompt, "Path"),
                })

            current_prompt = original_prompt
            final_output = ""
            success = False
            last_minor_output = ""
            last_minor_errors = []

            for attempt in range(1, MAX_RETRIES + 1):
                print(f"  > Attempt {attempt}/{MAX_RETRIES}...")
                raw_buffer = ""

                try:
                    for chunk in llm.stream(current_prompt):
                        print(chunk, end="", flush=True)
                        raw_buffer += chunk
                    print("\n")
                except Exception as e:
                    print(f"  💥 Error: {e}")
                    raw_buffer = ""

                cleaned = clean_response(raw_buffer)
                cleaned = remove_standalone_horizontal_rules(cleaned)
                cleaned = normalize_html_linked_assets_section(cleaned)
                cleaned = normalize_unicode_bullets(cleaned)
                cleaned = strip_js_prompt_leakage(cleaned)
                cleaned = replace_header_with_source(cleaned, prompt_type, fields)

                pre_repair_valid, pre_repair_errors = validate_required_structure(cleaned, prompt_type)

                repaired = auto_repair_structure(cleaned, prompt_type, fields)
                repaired = remove_standalone_horizontal_rules(repaired)
                repaired = normalize_unicode_bullets(repaired)
                repaired = strip_js_prompt_leakage(repaired)
                repaired = replace_header_with_source(repaired, prompt_type, fields)
                repaired_valid, repaired_errors = validate_required_structure(repaired, prompt_type)

                if pre_repair_valid:
                    print("  ✅ VALIDATION PASSED (raw output)")
                    final_output = repaired
                    success = True
                    break

                if repaired_valid:
                    print("  ✅ VALIDATION PASSED (after auto-repair)")
                    final_output = repaired
                    success = True
                    break

                if is_minor_only(repaired_errors):
                    print(f"  ⚠️ Minor issues detected, retrying with targeted feedback: {repaired_errors}")
                    last_minor_output = repaired
                    last_minor_errors = repaired_errors[:]
                    current_prompt = build_retry_prompt(repaired, original_prompt, prompt_type, repaired_errors)
                    continue

                print(f"  ❌ FATAL ERROR(S): {repaired_errors}")
                current_prompt = build_retry_prompt(repaired, original_prompt, prompt_type, repaired_errors)

            if not success and last_minor_output:
                print(f"  ⚠️ Accepting last minor-output version after retries: {last_minor_errors}")
                final_output = last_minor_output
                success = True

            if not success:
                print(f"  ! ABORTING {filename} - Using fallback template.")
                final_output = build_fallback(prompt_type, fields)
                final_output = replace_header_with_source(final_output, prompt_type, fields)

            expected = count_expected_items_in_prompt(original_prompt)
            produced = count_sections_in_output(final_output)

            if success and expected > produced:
                print(f"  ⚠️ Output contains {produced}/{expected} sections, but saving repaired output.")

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(final_output)

            print(f"  Saved: {out_path}")

    print("\nai_analysis: DONE")


if __name__ == "__main__":
    main()