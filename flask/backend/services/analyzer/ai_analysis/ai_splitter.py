import json
import os
import copy
import shutil
from collections import defaultdict

# --- OUTPUT BASE: place prompts under flask/backend/prompts_output ---
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))  # flask/backend/services/analyzer/ai_analysis
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))  # flask/backend
PROMPTS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")

# Input: prefer <repo>/flask/backend/static_analysis_output/all_analysis_results.json
STATIC_OUTPUT_DIR = os.path.join(BACKEND_DIR, "static_analysis_output")
STATIC_ANALYSIS_FILE = os.path.join(STATIC_OUTPUT_DIR, "all_analysis_results.json")

PAGE_OUTPUT_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "Page_Documentation_Prompts")
UTIL_OUTPUT_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "Utility_Documentation_Prompts")
UTIL_SQL_OUTPUT_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "Utility_SQL_Documentation_Prompts")
HTML_PROMPTS_OUTPUT_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "HTML_Documentation_Prompts")
JS_PROMPTS_OUTPUT_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "JS_Documentation_Prompts")

MAX_AI_CHARS_PER_PROMPT = 12000
MAX_AI_LINES_PER_PROMPT = 500
AI_CHUNK_OVERLAP_LINES = 0

PAGE_TEMPLATE = """
### SYSTEM ROLE
You are a **Technical Writer** specializing in Legacy Web Applications.
You are NOT a Developer. You DO NOT write code.

### OBJECTIVE
Analyze the combined Web Page and its Code-Behind to create a single Page Functionality Reference.
If linked files (such as JavaScript, helper modules, or markup fragments) appear in the input and clearly influence page behavior, briefly mention them in the relevant logic summary rows. Do NOT create a separate section for linked files.

### SOURCE METADATA
**PageTitle:** {page_title}
**Web Page File:** {page_file}
**Web Page Path:** {page_path}
**Code-Behind File:** {codebehind_file}
**Code-Behind Path:** {codebehind_path}

### IMPORTANT: DO NOT INFER DOMAIN
- Do NOT infer business domain, product names, or concrete entities from filenames, base types, or project names.
- Use only explicit evidence present in the provided IR/metadata.

### HARD NEGATIVE CONSTRAINTS
1. NO code blocks (C#, VB.NET, SQL).
2. NO installation / setup sections.
3. NO low-level ASP.NET explanations — explain what *this specific page* does.
4. Do NOT list simple data-binding expressions such as Eval(...), Bind(...), DataBinder.Eval(...), or repeated markup value expressions as events or methods.
5. Only include meaningful page lifecycle handlers, button handlers, server-side methods, validation logic, or clearly relevant client-side functions.

### OUTPUT FORMAT
### 1. User Purpose
{One sentence describing user purpose — if unknown use exact text required.}

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| ... | ... |

### 3. Data Interactions
* **Reads:**
* **Writes:**

### RAW INPUT
{code_chunk}
### END OF INPUT

Instruction: Document the page above. Focus on user actions, key events/methods and data flow.
"""

UTIL_TEMPLATE = """
### SYSTEM ROLE
You are a **Technical Writer** documenting code modules and utilities.
You are NOT a Developer. You DO NOT write code.

### OBJECTIVE
Produce a concise technical reference for the provided module.
Focus on purpose, externally visible declarations (functions, classes,
attributes), important side effects, and data interactions.

### IMPORTANT: DO NOT INFER DOMAIN
- Do NOT infer business domain, product names, or concrete entities from filenames, base types, or project names.
- Use only explicit evidence present in the provided IR/metadata.

### HARD CONSTRAINTS
1. NO code blocks (C#, VB.NET, SQL).
2. NO speculative domain assertions beyond explicit tokens.
3. If no runtime data access exists, explicitly state "None at runtime".

### SOURCE METADATA
**ModuleTitle:** {module_file}
**File:** {module_file}
**Path:** {module_path}

### OUTPUT FORMAT
### 1. Purpose
{One sentence describing user purpose — if unknown use exact text required.}

### 2. Key Declarations
| Symbol | Kind | Description |
| :--- | :--- | :--- |
| ... | ... | ... |

Kinds may include: Method, Function, Class, Attribute, Constant, Event, Table, View, Page Handler, Utility.

### 3. Important Behavior & Side Effects

### 4. Data Interactions
* **Reads:**
* **Writes:**

If there is no runtime data access, write exactly (you have to check first):
* **Reads:** None at runtime
* **Writes:** None at runtime

### RAW INPUT
{code_chunk}
### END OF INPUT
"""

UTIL_SQL_TEMPLATE = """
### SYSTEM ROLE
You are a **Technical Writer** documenting code modules and utilities.
You are NOT a Developer. You DO NOT write code.

### OBJECTIVE
Produce a concise technical reference for the provided module.
This module includes SQL/database access metadata. You MUST describe the database-related behavior clearly.

### IMPORTANT: DO NOT INFER DOMAIN
- Do NOT infer business domain, product names, or concrete entities from filenames, base types, or project names.
- Use only explicit evidence present in the provided IR/metadata.

### SQL-SPECIFIC INSTRUCTIONS
- Inspect the field `sql_usages` in the RAW INPUT.
- Summarize database access at method level when possible.
- Mention tables or views read or written when they can be identified from the SQL text.
- Mention stored procedures if present.
- Do NOT reproduce full SQL statements.
- Do NOT invent tables, business purpose, or schema details that are not explicitly present.
- If SQL usage exists, do NOT say "None at runtime".

### HARD CONSTRAINTS
1. NO code blocks (C#, VB.NET, SQL).
2. NO speculative domain assertions beyond explicit tokens.
3. Base all database statements only on explicit SQL metadata in the input.

### SOURCE METADATA
**ModuleTitle:** {module_file}
**File:** {module_file}
**Path:** {module_path}

### OUTPUT FORMAT
### 1. Purpose
{One sentence describing user purpose — if unknown use exact text required.}

### 2. Key Declarations
| Symbol | Kind | Description |
| :--- | :--- | :--- |
| ... | ... | ... |

Kinds may include: Method, Function, Class, Attribute, Constant, Event, Table, View, Page Handler, Utility.

### 3. Important Behavior & Side Effects

### 4. Data Interactions
* **Reads:** ...
* **Writes:** ...

### 5. Database Access Summary
| Method | Operation | Target |
| :--- | :--- | :--- |
| ... | ... | ... |

### 6. SQL Operations
- Summarize the main query or stored procedure usage for each relevant method.

### RAW INPUT
{code_chunk}
### END OF INPUT
"""

HTML_TEMPLATE = """
### SYSTEM ROLE
You are a Technical Writer documenting static and client-rendered web pages.
You are NOT a Developer. You DO NOT write code.

### OBJECTIVE
Document the HTML page below using only the extracted HTML metadata.
Focus on visible structure, likely user purpose, important UI regions, forms, actions, navigation, and linked assets.

### IMPORTANT: DO NOT INFER DOMAIN
- Do NOT infer business domain, product names, or concrete entities from filenames, base types, or project names.
- Use only explicit evidence present in the provided IR/metadata.

### IMPORTANT RULES
1. Do NOT write code.
2. Do NOT explain HTML syntax.
3. Do NOT invent business context that is not supported by the metadata.
4. If information is not visible from the metadata, write: Not clearly indicated
5. Use the extracted fields such as headings, forms, links, buttons, tables, displayRegions, inlineEventAttrs, assets, scripts, ids, classes, and summaryHints.

### SOURCE METADATA
**HtmlTitle:** {html_file}
**File:** {html_file}
**Path:** {html_path}

### OUTPUT FORMAT
### 1. User Purpose
One short paragraph describing what the page appears to be for based only on visible structure and extracted metadata. If unknown use exact text required.

### 2. Main UI Sections
| Section | Description |
| :--- | :--- |
| ... | ... |

### 3. Forms and User Inputs
If forms or inputs exist, provide this table:

| Element | Type | Purpose |
| :--- | :--- | :--- |
| ... | ... | ... |

If there are no forms or inputs, write exactly:
Not clearly indicated

### 4. Navigation and Actions
- Summarize important links, buttons, and inline-triggered actions.

### 5. Data Display and Visual Regions
- Summarize tables, display regions, charts, modals, lists, grids, summaries, detail areas, or other visible content regions if present.

### 6. Linked Assets
* **Scripts:** 
* **Styles / Links:** 
* **Images / Other Assets:** 

### RAW INPUT
{code_chunk}
### END OF INPUT
"""

JS_TEMPLATE = """
### SYSTEM ROLE
You are a Technical Writer documenting JavaScript client-side files.
You are NOT a Developer. You DO NOT write code.

### OBJECTIVE
Document the JavaScript file below using only the extracted metadata.
Focus on purpose, key functions, event bindings, selectors / DOM interaction, API usage, and side effects.

### IMPORTANT: DO NOT INFER DOMAIN
- Do NOT infer business domain, product names, or concrete entities from filenames, base types, or project names.
- Use only explicit evidence present in the provided IR/metadata.

### IMPORTANT RULES
1. Do NOT write code.
2. Do NOT explain JavaScript syntax.
3. Do NOT invent business context that is not supported by the metadata.
4. If information is not visible from the metadata, write: Not clearly indicated
5. Use the extracted fields such as exports, funcs, apiCalls, eventBindings, selectors, client_js_summary, parseWarning, and error.

### SOURCE METADATA
**JsTitle:** {js_file}
**File:** {js_file}
**Path:** {js_path}

### OUTPUT FORMAT
### 1. Purpose
One short paragraph describing what this script appears to do based only on the extracted metadata.

### 2. Key Functions
| Function | Type | Description |
| :--- | :--- | :--- |
| ... | ... | ... |

If no functions are identified, write exactly:
Not clearly indicated

### 3. Event Bindings
| Event / Trigger | Handler / Behavior |
| :--- | :--- |
| ... | ... |

If no event bindings are identified, write exactly:
Not clearly indicated

### 4. DOM Interaction
- Summarize selectors, DOM queries, and visible DOM update behavior if present.

### 5. API / Network Usage
- Summarize fetch / axios / jQuery AJAX calls and likely targets if present.

### 6. Side Effects and Dependencies
* **Exports:** 
* **External Dependencies:** 
* **Side Effects:** 

### RAW INPUT
{code_chunk}
### END OF INPUT
"""

def clean_data(item):
    clean_item = copy.deepcopy(item)
    for k in ("dependencies", "usings", "assemblies", "imports", "file_level_sql"):
        if k in clean_item:
            del clean_item[k]
        if "ir" in clean_item and k in clean_item["ir"]:
            del clean_item["ir"][k]
    return clean_item

def _normalize_path(p: str) -> str:
    if not p:
        return ""
    p = p.split("<%")[0].split("?", 1)[0].strip().strip('"').strip("'")
    return p.replace("\\", "/").lstrip("/").lower()

def _get_item_file(item: dict) -> str:
    return item.get("file") or item.get("fileName") or (item.get("ir") or {}).get("file") or ""

def _get_item_path(item: dict) -> str:
    return item.get("path") or (item.get("ir") or {}).get("path") or ""

def is_markup_item(item: dict) -> bool:
    fname = _get_item_file(item).lower()
    if item.get("isAspx") is True:
        return True
    return (
        fname.endswith(".aspx")
        or fname.endswith(".ascx")
        or fname.endswith(".master")
        or fname.endswith(".cshtml")
        or fname.endswith(".razor")
    )

def is_codebehind_item(item: dict) -> bool:
    fname = _get_item_file(item).lower()
    return (
        fname.endswith(".aspx.vb")
        or fname.endswith(".ascx.vb")
        or fname.endswith(".master.vb")
        or fname.endswith(".aspx.cs")
        or fname.endswith(".ascx.cs")
        or fname.endswith(".master.cs")
        or fname.endswith(".cshtml.cs")
        or fname.endswith(".razor.cs")
    )

def is_html_item(item: dict) -> bool:
    fname = _get_item_file(item).lower()
    return fname.endswith(".html") or fname.endswith(".htm")

def is_js_item(item: dict) -> bool:
    fname = _get_item_file(item).lower()
    return fname.endswith(".js") or fname.endswith(".jsx")

def has_sql_usage(item: dict) -> bool:
    sql_usages = item.get("sql_usages")
    return isinstance(sql_usages, list) and len(sql_usages) > 0

def find_codebehind_for_markup(markup_item: dict, all_items: list) -> dict | None:
    markup_path = _get_item_path(markup_item) or _get_item_file(markup_item)
    if not markup_path:
        return None

    norm = _normalize_path(markup_path)
    candidates = [
        norm + ".vb",
        norm + ".cs",
        norm + ".aspx.vb",
        norm + ".aspx.cs",
        norm + ".ascx.vb",
        norm + ".ascx.cs",
        norm + ".master.vb",
        norm + ".master.cs",
        norm + ".cshtml.cs",
        norm + ".razor.cs",
    ]

    for it in all_items:
        cand = _normalize_path(_get_item_path(it) or _get_item_file(it))
        if not cand:
            continue
        if cand in candidates or (cand.startswith(norm) and (cand.endswith(".vb") or cand.endswith(".cs"))):
            return it
    return None

def find_matching_markup(codebehind_item: dict, all_items: list) -> dict | None:
    p = _get_item_path(codebehind_item) or _get_item_file(codebehind_item)
    if not p:
        return None

    p_norm = _normalize_path(p)
    if p_norm.endswith(".cs"):
        markup_candidate = p_norm[:-3]
    elif p_norm.endswith(".vb"):
        markup_candidate = p_norm[:-3]
    else:
        return None

    for it in all_items:
        cand = _normalize_path(_get_item_path(it) or _get_item_file(it))
        if not cand:
            continue
        if cand == markup_candidate:
            return it

    markup_base = os.path.basename(markup_candidate)
    for it in all_items:
        cand = _normalize_path(_get_item_path(it) or _get_item_file(it))
        if not cand:
            continue
        if cand.endswith("/" + markup_base) or cand.endswith(markup_base):
            return it

    return None

def find_linked_matches(all_items: list, linked_path: str) -> list:
    linked_norm = _normalize_path(linked_path)
    if not linked_norm:
        return []

    linked_base = os.path.basename(linked_norm)
    exact = []
    base_matches = []

    for it in all_items:
        cand = _get_item_path(it) or _get_item_file(it)
        if not cand:
            continue

        cand_norm = _normalize_path(cand)
        if cand_norm.endswith(linked_norm):
            exact.append(it)
            continue

        if cand_norm.endswith("/" + linked_base) or cand_norm.endswith(linked_base):
            base_matches.append(it)

    return exact if exact else base_matches

def _safe_filename(s: str) -> str:
    if not s:
        return "unknown"
    return "".join(c if c.isalnum() or c in "-._" else "_" for c in s)[:200]

def _extract_namespace(item: dict) -> str:
    ns = "Unknown"
    ns_list = item.get("namespaces")
    if not ns_list and item.get("ir"):
        ns_list = item["ir"].get("namespaces")
    if ns_list and len(ns_list) > 0:
        ns = ns_list[0]
    return ns

def split_text_if_too_long(text: str):
    line_count = text.count("\n") + 1
    if len(text) <= MAX_AI_CHARS_PER_PROMPT and line_count <= MAX_AI_LINES_PER_PROMPT:
        return [text]

    lines = text.splitlines(keepends=True)
    chunks = []
    start = 0

    while start < len(lines):
        current_lines = []
        current_len = 0
        end = start

        while end < len(lines):
            next_line = lines[end]
            if current_lines and (
                current_len + len(next_line) > MAX_AI_CHARS_PER_PROMPT
                or len(current_lines) >= MAX_AI_LINES_PER_PROMPT
            ):
                break
            current_lines.append(next_line)
            current_len += len(next_line)
            end += 1

        chunk = "".join(current_lines).strip()
        if chunk:
            chunks.append(chunk)

        if end >= len(lines):
            break

        start = end if AI_CHUNK_OVERLAP_LINES <= 0 else max(end - AI_CHUNK_OVERLAP_LINES, start + 1)

    return chunks



def _build_part_suffix(part_idx: int, total_parts: int) -> str:
    return f" (Part {part_idx} of {total_parts})"


def _title_with_part_suffix(title: str, part_idx: int, total_parts: int) -> str:
    base = (title or "").strip()
    suffix = _build_part_suffix(part_idx, total_parts)
    if not base:
        return suffix.strip()
    if base.endswith(suffix):
        return base
    return f"{base}{suffix}"

def _save_module(out_dir: str, ns: str, idx: int, module_obj: dict, template: str):
    os.makedirs(out_dir, exist_ok=True)
    primary = _get_item_file(module_obj) or "module"
    safe = _safe_filename(primary)
    module_path = _get_item_path(module_obj)

    code_chunk = json.dumps(module_obj, indent=2)
    parts = split_text_if_too_long(code_chunk)

    if len(parts) == 1:
        filename = f"Module_{ns.replace('.', '_')}_{idx}_{safe}.txt"
        content = template.replace("{module_file}", primary).replace("{module_path}", module_path).replace("{code_chunk}", parts[0])

        out_path = os.path.join(out_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Saved module prompt: {out_path}")
    else:
        print(f"Module '{primary}' is large; splitting into {len(parts)} parts...")
        for part_idx, part_chunk in enumerate(parts, start=1):
            filename = f"Module_{ns.replace('.', '_')}_{idx}_{safe}_part{part_idx}.txt"
            part_note = (
                f"This file contains only one chunk of the full module metadata. "
                f"Document this chunk as Part {part_idx} of {len(parts)} while keeping terminology consistent."
            )

            content = template.replace("{module_file}", _title_with_part_suffix(primary, part_idx, len(parts))).replace("{module_path}", module_path)
            content = content.replace("### RAW INPUT", f"### PART INSTRUCTION\n{part_note}\n\n### RAW INPUT")
            content = content.replace("{code_chunk}", part_chunk)

            out_path = os.path.join(out_dir, filename)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Saved module prompt: {out_path}")

def _save_page_pair(out_dir: str, ns: str, idx: int, pair_obj: dict):
    os.makedirs(out_dir, exist_ok=True)
    primary = pair_obj.get("pageFile") or pair_obj.get("codeBehindFile") or "unknown"
    safe = _safe_filename(primary)

    page_file = (
        pair_obj.get("pageFile")
        or _get_item_file(pair_obj.get("markup") or {})
        or ""
    )
    page_path = (
        pair_obj.get("pagePath")
        or _get_item_path(pair_obj.get("markup") or {})
        or ""
    )
    codebehind_file = (
        pair_obj.get("codeBehindFile")
        or _get_item_file(pair_obj.get("codeBehind") or {})
        or ""
    )
    codebehind_path = (
        pair_obj.get("codeBehindPath")
        or _get_item_path(pair_obj.get("codeBehind") or {})
        or ""
    )

    code_chunk = json.dumps(pair_obj, indent=2)
    parts = split_text_if_too_long(code_chunk)

    if len(parts) == 1:
        filename = f"Page_{ns.replace('.', '_')}_{idx}_{safe}.txt"

        content = PAGE_TEMPLATE
        content = content.replace("{page_file}", page_file)
        content = content.replace("{page_path}", page_path)
        content = content.replace("{codebehind_file}", codebehind_file)
        content = content.replace("{codebehind_path}", codebehind_path)
        content = content.replace("{code_chunk}", parts[0])
        content = content.replace("{page_title}", page_file or codebehind_file or safe)

        out_path = os.path.join(out_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Saved page prompt: {out_path}")
    else:
        print(f"Page '{primary}' is large; splitting into {len(parts)} parts...")
        for part_idx, part_chunk in enumerate(parts, start=1):
            filename = f"Page_{ns.replace('.', '_')}_{idx}_{safe}_part{part_idx}.txt"

            part_note = (
                f"This file contains only one chunk of the full page metadata. "
                f"Document this chunk as Part {part_idx} of {len(parts)} while keeping terminology consistent."
            )

            content = PAGE_TEMPLATE
            content = content.replace("{page_file}", page_file)
            content = content.replace("{page_path}", page_path)
            content = content.replace("{codebehind_file}", codebehind_file)
            content = content.replace("{codebehind_path}", codebehind_path)
            content = content.replace(
                "### RAW INPUT",
                f"### PART INSTRUCTION\n{part_note}\n\n### RAW INPUT"
            )
            content = content.replace("{code_chunk}", part_chunk)
            content = content.replace("{page_title}", _title_with_part_suffix(page_file or codebehind_file or safe, part_idx, len(parts)))

            out_path = os.path.join(out_dir, filename)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Saved page prompt: {out_path}")

def _save_html_page(out_dir: str, idx: int, html_obj: dict):
    os.makedirs(out_dir, exist_ok=True)
    primary = _get_item_file(html_obj) or "unknown.html"
    safe = _safe_filename(primary)
    html_path = _get_item_path(html_obj)

    code_chunk = json.dumps(html_obj, indent=2)
    parts = split_text_if_too_long(code_chunk)

    if len(parts) == 1:
        filename = f"HTML_{idx}_{safe}.txt"
        content = HTML_TEMPLATE.replace("{html_file}", primary).replace("{html_path}", html_path).replace("{code_chunk}", parts[0])

        out_path = os.path.join(out_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Saved HTML prompt: {out_path}")
    else:
        print(f"HTML page '{primary}' is large; splitting into {len(parts)} parts...")
        for part_idx, part_chunk in enumerate(parts, start=1):
            filename = f"HTML_{idx}_{safe}_part{part_idx}.txt"
            part_note = (
                f"This file contains only one chunk of the full HTML page metadata. "
                f"Document this chunk as Part {part_idx} of {len(parts)} while keeping terminology consistent."
            )

            content = HTML_TEMPLATE.replace("{html_file}", _title_with_part_suffix(primary, part_idx, len(parts))).replace("{html_path}", html_path)
            content = content.replace("### RAW INPUT", f"### PART INSTRUCTION\n{part_note}\n\n### RAW INPUT")
            content = content.replace("{code_chunk}", part_chunk)

            out_path = os.path.join(out_dir, filename)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Saved HTML prompt: {out_path}")

def _save_js_file(out_dir: str, idx: int, js_obj: dict):
    os.makedirs(out_dir, exist_ok=True)
    primary = _get_item_file(js_obj) or "unknown.js"
    safe = _safe_filename(primary)
    js_path = _get_item_path(js_obj)

    code_chunk = json.dumps(js_obj, indent=2)
    parts = split_text_if_too_long(code_chunk)

    if len(parts) == 1:
        filename = f"JS_{idx}_{safe}.txt"
        content = JS_TEMPLATE.replace("{js_file}", primary).replace("{js_path}", js_path).replace("{code_chunk}", parts[0])

        out_path = os.path.join(out_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Saved JS prompt: {out_path}")
    else:
        print(f"JS file '{primary}' is large; splitting into {len(parts)} parts...")
        for part_idx, part_chunk in enumerate(parts, start=1):
            filename = f"JS_{idx}_{safe}_part{part_idx}.txt"
            part_note = (
                f"This file contains only one chunk of the full JavaScript metadata. "
                f"Document this chunk as Part {part_idx} of {len(parts)} while keeping terminology consistent."
            )

            content = JS_TEMPLATE.replace("{js_file}", _title_with_part_suffix(primary, part_idx, len(parts))).replace("{js_path}", js_path)
            content = content.replace("### RAW INPUT", f"### PART INSTRUCTION\n{part_note}\n\n### RAW INPUT")
            content = content.replace("{code_chunk}", part_chunk)

            out_path = os.path.join(out_dir, filename)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Saved JS prompt: {out_path}")

def main():
    print(f"Reading {STATIC_ANALYSIS_FILE}...")
    try:
        with open(STATIC_ANALYSIS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading input: {e}")
        return

    os.makedirs(PROMPTS_OUTPUT_BASE, exist_ok=True)

    for folder in (PAGE_OUTPUT_DIR, UTIL_OUTPUT_DIR, UTIL_SQL_OUTPUT_DIR, HTML_PROMPTS_OUTPUT_DIR, JS_PROMPTS_OUTPUT_DIR):
        if os.path.exists(folder):
            shutil.rmtree(folder)

    os.makedirs(PAGE_OUTPUT_DIR, exist_ok=True)
    os.makedirs(UTIL_OUTPUT_DIR, exist_ok=True)
    os.makedirs(UTIL_SQL_OUTPUT_DIR, exist_ok=True)
    os.makedirs(HTML_PROMPTS_OUTPUT_DIR, exist_ok=True)
    os.makedirs(JS_PROMPTS_OUTPUT_DIR, exist_ok=True)

    page_groups = defaultdict(list)
    util_groups = defaultdict(list)
    util_sql_groups = defaultdict(list)
    html_items = []
    js_items = []

    processed = set()
    found_pages = 0
    found_utils = 0
    found_sql_utils = 0
    found_html = 0
    found_js = 0

    path_index = {}
    for itm in data:
        cand = _get_item_path(itm) or _get_item_file(itm)
        if cand:
            path_index[_normalize_path(cand)] = itm

    for itm in data:
        raw = _get_item_path(itm) or _get_item_file(itm)
        norm = _normalize_path(raw)

        if not raw or norm in processed:
            continue

        if is_html_item(itm):
            cleaned_html = clean_data(itm)

            linked_from_html = itm.get("linkedClientFiles") or itm.get("linkedFiles") or []
            if linked_from_html is None:
                linked_from_html = []

            linked_detailed = []
            for lf in linked_from_html:
                matches = find_linked_matches(data, lf)
                if not matches:
                    linked_detailed.append({"candidate": lf})
                else:
                    for m in matches:
                        linked_detailed.append({
                            "file": _get_item_file(m),
                            "path": _get_item_path(m),
                            "language": m.get("language") or m.get("lang") or "",
                            "client_js_summary": m.get("client_js_summary") if "client_js_summary" in m else None,
                            "exports": m.get("exports") if "exports" in m else None,
                            "funcs": m.get("funcs") if "funcs" in m else None,
                            "apiCalls": m.get("apiCalls") if "apiCalls" in m else None,
                            "eventBindings": m.get("eventBindings") if "eventBindings" in m else None,
                            "selectors": m.get("selectors") if "selectors" in m else None,
                        })

            cleaned_html["linkedFilesDetailed"] = linked_detailed

            html_items.append(cleaned_html)
            found_html += 1
            processed.add(norm)
            continue

        if is_js_item(itm):
            cleaned_js = clean_data(itm)
            js_items.append(cleaned_js)
            found_js += 1
            processed.add(norm)
            continue

        if is_markup_item(itm):
            cleaned_markup = clean_data(itm)
            cb = find_codebehind_for_markup(itm, data)
            cleaned_cb = clean_data(cb) if cb else None

            combined = {
                "pageFile": _get_item_file(cleaned_markup),
                "pagePath": _get_item_path(cleaned_markup),
                "codeBehindFile": _get_item_file(cleaned_cb) if cleaned_cb else None,
                "codeBehindPath": _get_item_path(cleaned_cb) if cleaned_cb else None,
                "markup": cleaned_markup,
                "codeBehind": cleaned_cb,
            }

            linked_from_markup = itm.get("linkedClientFiles") or itm.get("linkedFiles") or []
            if linked_from_markup is None:
                linked_from_markup = []

            linked_detailed = []
            for lf in linked_from_markup:
                matches = find_linked_matches(data, lf)
                if not matches:
                    linked_detailed.append({"candidate": lf})
                else:
                    for m in matches:
                        linked_detailed.append({
                            "file": _get_item_file(m),
                            "path": _get_item_path(m),
                            "language": m.get("language") or m.get("lang") or "",
                            "client_js_summary": m.get("client_js_summary") if "client_js_summary" in m else None,
                        })

            combined["linkedFilesDetailed"] = linked_detailed

            ns = "Unknown"
            ns_list = None
            if cleaned_cb and cleaned_cb.get("namespaces"):
                ns_list = cleaned_cb.get("namespaces")
            if not ns_list and itm.get("ir"):
                ns_list = itm["ir"].get("namespaces")
            if ns_list and len(ns_list) > 0:
                ns = ns_list[0]

            page_groups[ns].append(combined)
            found_pages += 1

            processed.add(_normalize_path(_get_item_path(cleaned_markup)))
            if cleaned_cb:
                processed.add(_normalize_path(_get_item_path(cleaned_cb)))
            continue

        if is_codebehind_item(itm):
            matched_markup = find_matching_markup(itm, data)
            if matched_markup:
                continue

            cleaned_cb = clean_data(itm)
            combined = {
                "pageFile": None,
                "pagePath": None,
                "codeBehindFile": _get_item_file(cleaned_cb),
                "codeBehindPath": _get_item_path(cleaned_cb),
                "markup": None,
                "codeBehind": cleaned_cb,
                "linkedFilesDetailed": [],
            }

            ns = _extract_namespace(cleaned_cb)
            page_groups[ns].append(combined)
            found_pages += 1
            processed.add(norm)
            continue

        if norm.endswith(".cs") or norm.endswith(".vb"):
            cleaned = clean_data(itm)
            ns = _extract_namespace(cleaned)

            if has_sql_usage(itm):
                util_sql_groups[ns].append(cleaned)
                found_sql_utils += 1
            else:
                util_groups[ns].append(cleaned)
                found_utils += 1

            processed.add(norm)
            continue

    print(
        f"Found {found_pages} pages, {found_utils} utility modules without SQL, "
        f"{found_sql_utils} utility modules with SQL, {found_html} HTML pages, "
        f"and {found_js} JS files. Generating prompts..."
    )

    for ns, items in page_groups.items():
        for i, obj in enumerate(items, start=1):
            _save_page_pair(PAGE_OUTPUT_DIR, ns, i, obj)

    for ns, items in util_groups.items():
        for i, obj in enumerate(items, start=1):
            _save_module(UTIL_OUTPUT_DIR, ns, i, obj, UTIL_TEMPLATE)

    for ns, items in util_sql_groups.items():
        for i, obj in enumerate(items, start=1):
            _save_module(UTIL_SQL_OUTPUT_DIR, ns, i, obj, UTIL_SQL_TEMPLATE)

    for i, obj in enumerate(html_items, start=1):
        _save_html_page(HTML_PROMPTS_OUTPUT_DIR, i, obj)

    for i, obj in enumerate(js_items, start=1):
        _save_js_file(JS_PROMPTS_OUTPUT_DIR, i, obj)

    try:
        job_id = os.environ.get("ANALYZER_JOB_ID") or os.environ.get("JOB_ID") or "global"
        manifest_files = []

        for d in (PAGE_OUTPUT_DIR, UTIL_OUTPUT_DIR, UTIL_SQL_OUTPUT_DIR, HTML_PROMPTS_OUTPUT_DIR, JS_PROMPTS_OUTPUT_DIR):
            if os.path.isdir(d):
                for f in sorted(os.listdir(d)):
                    if f.endswith(".txt"):
                        manifest_files.append(
                            os.path.join(os.path.relpath(d, PROMPTS_OUTPUT_BASE), f).replace("\\", "/")
                        )

        manifest = {
            "job_id": job_id,
            "expected": len(manifest_files),
            "files": manifest_files,
        }

        manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_ai_{job_id}.json")
        with open(manifest_path, "w", encoding="utf-8") as mf:
            json.dump(manifest, mf, indent=2)

        print(f"Wrote AI manifest: {manifest_path} (expected={manifest['expected']})")
    except Exception as e:
        print(f"Error writing manifest: {e}")

    print(
        f"DONE! Page prompts saved in '{PAGE_OUTPUT_DIR}', "
        f"Module prompts saved in '{UTIL_OUTPUT_DIR}', "
        f"SQL-aware Module prompts saved in '{UTIL_SQL_OUTPUT_DIR}', "
        f"HTML prompts saved in '{HTML_PROMPTS_OUTPUT_DIR}', "
        f"JS prompts saved in '{JS_PROMPTS_OUTPUT_DIR}'."
    )

if __name__ == "__main__":
    main()