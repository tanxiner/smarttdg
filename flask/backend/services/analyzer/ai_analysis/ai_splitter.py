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
# Fallback: user's My Documents/all_analysis_results.json (matches Roslyn fallback)
STATIC_OUTPUT_DIR = os.path.join(BACKEND_DIR, "static_analysis_output")
STATIC_ANALYSIS_FILE = os.path.join(STATIC_OUTPUT_DIR, "all_analysis_results.json")

PAGE_OUTPUT_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "Page_Documentation_Prompts")
UTIL_OUTPUT_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "Utility_Documentation_Prompts")
# include SQL folder so manifest covers SQL prompts too
SQL_OUTPUT_DIR = os.path.join(PROMPTS_OUTPUT_BASE, "SQL_Documentation_Prompts")
MAX_CHARS = 12000

# --- PER-PAIR TEMPLATES: explicitly label page vs code-behind ---
PAGE_TEMPLATE = """
### SYSTEM ROLE
You are a **Technical Writer** specializing in Legacy Web Applications.
You are NOT a Developer. You DO NOT write code.

### OBJECTIVE
Analyze the combined Web Page and its Code-Behind to create a single Page Functionality Reference.

Web Page File: {page_file}
Code-Behind File: {codebehind_file}

### IMPORTANT: DO NOT INFER DOMAIN
- Do NOT infer business domain, product names, or concrete entities from filenames, base types, or project names.
- Use only explicit evidence present in the provided IR/metadata (method names, control names, SQL table names, linked markup tokens).
- If there is no explicit domain or entity name visible in the input, write the User Purpose exactly as:
  This page's user purpose is Unknown (no explicit domain information in the code).

### 🛑 HARD NEGATIVE CONSTRAINTS
1. NO code blocks (C#, VB.NET, SQL).
2. NO installation / setup sections.
3. NO low-level ASP.NET explanations — explain what *this specific page* does.

### OUTPUT FORMAT (one document per page)
# Page: {page_title}
**Web Page File:** {page_file}
**Code-Behind File:** {codebehind_file}

### 1. User Purpose
{One sentence describing user purpose — if unknown use exact text required.}

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| ... | ... |

### 3. Data Interactions
* **Reads:** ...
* **Writes:** ...

--- 

### ⬇️ RAW INPUT (combined objects) ⬇️
{code_chunk}
### ⬆️ END OF INPUT ⬆️

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

### HARD CONSTRAINTS
1. NO code blocks (C#, VB.NET, SQL).
2. NO speculative domain assertions beyond explicit tokens.
3. If no runtime data access exists, explicitly state "None at runtime".

### OUTPUT FORMAT (one document per module)
# Module: {module_name}
**File:** {module_file}

### 1. Purpose
{One sentence describing user purpose — if unknown use exact text required.}

### 2. Key Declarations
| Symbol | Kind | Description |
| :--- | :--- | :--- |
| ... | ... | ... |

Kinds may include: Method, Function, Class, Attribute, Constant, Event, Table, View, Page Handler, Utility.

### 3. Important Behavior & Side Effects
- ...

### 4. Data Interactions
* **Reads:** ...
* **Writes:** ...

---

### ⬇️ RAW MODULE INPUT ⬇️
{code_chunk}
### ⬆️ END OF INPUT ⬆️
"""

def clean_data(item):
    """Remove noisy keys to keep prompts compact."""
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

def is_markup_item(item: dict) -> bool:
    fname = (item.get("file") or item.get("fileName") or "").lower()
    if item.get("isAspx") is True:
        return True
    # treat Razor views and Blazor components as markup too
    return fname.endswith(".aspx") or fname.endswith(".ascx") or fname.endswith(".master") or fname.endswith(".cshtml") or fname.endswith(".razor")

def is_codebehind_item(item: dict) -> bool:
    fname = (item.get("file") or item.get("fileName") or "").lower()
    # include Razor page-model / Blazor partial class codebehind (.razor.cs)
    return fname.endswith(".aspx.vb") or fname.endswith(".ascx.vb") or fname.endswith(".master.vb") \
        or fname.endswith(".aspx.cs") or fname.endswith(".ascx.cs") or fname.endswith(".master.cs") \
        #or fname.endswith(".cshtml.cs") or fname.endswith(".razor.cs")

def find_codebehind_for_markup(markup_item: dict, all_items: list) -> dict | None:
    """Find a matching code-behind item for the given markup item (best-effort)."""
    markup_path = (markup_item.get("path") or markup_item.get("file") or markup_item.get("fileName") or "")
    if not markup_path:
        return None
    norm = _normalize_path(markup_path)
    # common variants
    candidates = [norm + ".vb", norm + ".cs", norm + ".aspx.vb", norm + ".aspx.cs"]
    for it in all_items:
        cand = _normalize_path((it.get("ir") or {}).get("path") or it.get("path") or it.get("file") or it.get("fileName") or "")
        if not cand:
            continue
        if cand in candidates or (cand.startswith(norm) and (cand.endswith(".vb") or cand.endswith(".cs"))):
            return it
    return None

def find_matching_markup(codebehind_item: dict, all_items: list) -> dict | None:
    """
    Given a code-behind item (e.g. 'Foo.aspx.vb' or 'Foo.aspx.cs'), find the corresponding markup item.
    Returns the matched markup item or None.
    """
    p = (codebehind_item.get("ir") or {}).get("path") or codebehind_item.get("path") or codebehind_item.get("file") or codebehind_item.get("fileName") or ""
    if not p:
        return None
    p_norm = _normalize_path(p)
    # strip .cs / .vb suffix to get markup path candidate
    if p_norm.endswith(".cs"):
        markup_candidate = p_norm[:-3]
    elif p_norm.endswith(".vb"):
        markup_candidate = p_norm[:-3]
    else:
        return None

    # Try exact match against items
    for it in all_items:
        cand = _normalize_path((it.get("ir") or {}).get("path") or it.get("path") or it.get("file") or it.get("fileName") or "")
        if not cand:
            continue
        if cand == markup_candidate:
            return it
    # fallback: try basename match (last segment)
    markup_base = os.path.basename(markup_candidate)
    for it in all_items:
        cand = _normalize_path((it.get("ir") or {}).get("path") or it.get("path") or it.get("file") or it.get("fileName") or "")
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
        cand = (it.get("path") or it.get("file") or (it.get("ir") or {}).get("path") or "")
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

def main():
    print(f"Reading {STATIC_ANALYSIS_FILE}...")
    try:
        with open(STATIC_ANALYSIS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading input: {e}")
        return

    # Ensure base output folders
    # Do NOT remove the entire PROMPTS_OUTPUT_BASE since other splitters (SQL) write into it.
    os.makedirs(PROMPTS_OUTPUT_BASE, exist_ok=True)
    # remove only the folders this splitter manages so we don't wipe SQL prompts
    if os.path.exists(PAGE_OUTPUT_DIR):
        shutil.rmtree(PAGE_OUTPUT_DIR)
    if os.path.exists(UTIL_OUTPUT_DIR):
        shutil.rmtree(UTIL_OUTPUT_DIR)
    os.makedirs(PAGE_OUTPUT_DIR, exist_ok=True)
    os.makedirs(UTIL_OUTPUT_DIR, exist_ok=True)

    page_groups = defaultdict(list)   # namespace -> list of combined {markup, codeBehind, ...}
    util_groups = defaultdict(list)   # namespace -> list of module items

    processed = set()
    found_pages = 0
    found_utils = 0

    # Build index by normalized path
    path_index = {}
    for itm in data:
        cand = (itm.get("ir") or {}).get("path") or itm.get("path") or itm.get("file") or itm.get("fileName") or ""
        if cand:
            path_index[_normalize_path(cand)] = itm

    # Pair markup <-> codebehind and collect utilities
    for itm in data:
        raw = (itm.get("ir") or {}).get("path") or itm.get("path") or itm.get("file") or itm.get("fileName") or ""
        norm = _normalize_path(raw)
        if not raw or norm in processed:
            continue

        # If markup, pair with code-behind
        if is_markup_item(itm):
            cleaned_markup = clean_data(itm)
            cb = find_codebehind_for_markup(itm, data)
            cleaned_cb = clean_data(cb) if cb else None

            combined = {
                "pageFile": cleaned_markup.get("file") or cleaned_markup.get("fileName") or "",
                "pagePath": cleaned_markup.get("path") or "",
                "codeBehindFile": cleaned_cb.get("file") if cleaned_cb else None,
                "codeBehindPath": cleaned_cb.get("path") if cleaned_cb else None,
                "markup": cleaned_markup,
                "codeBehind": cleaned_cb,
            }

            # linked client files reasoning
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
                            "file": m.get("file") or m.get("fileName") or "",
                            "path": (m.get("path") or (m.get("ir") or {}).get("path") or ""),
                            "language": m.get("language") or m.get("lang") or "",
                            "client_js_summary": m.get("client_js_summary") if "client_js_summary" in m else None
                        })
            combined["linkedFilesDetailed"] = linked_detailed

            # namespace grouping preference: code-behind namespaces, then markup IR
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

            processed.add(_normalize_path(cleaned_markup.get("path") or ""))
            if cleaned_cb:
                processed.add(_normalize_path(cleaned_cb.get("path") or ""))
            continue

        # If codebehind not paired previously, treat as page with only codebehind
        if is_codebehind_item(itm):
            # try to find markup — if found it will be handled when markup encountered, so skip if paired
            matched_markup = find_matching_markup(itm, data)
            if matched_markup:
                # matched markup exists elsewhere in the data; skip here and let the markup entry create the combined prompt
                continue

            # if no matched markup, emit a page-like prompt containing only the code-behind
            cleaned_cb = clean_data(itm)
            combined = {
                "pageFile": None,
                "pagePath": None,
                "codeBehindFile": cleaned_cb.get("file") or cleaned_cb.get("fileName") or "",
                "codeBehindPath": cleaned_cb.get("path") or "",
                "markup": None,
                "codeBehind": cleaned_cb,
                "linkedFilesDetailed": []
            }
            ns = "Unknown"
            ns_list = cleaned_cb.get("namespaces")
            if not ns_list and itm.get("ir"):
                ns_list = itm["ir"].get("namespaces")
            if ns_list and len(ns_list) > 0:
                ns = ns_list[0]
            page_groups[ns].append(combined)
            found_pages += 1
            processed.add(norm)
            continue

        # Otherwise treat as utility/module if .cs/.vb
        if norm.endswith(".cs") or norm.endswith(".vb"):
            cleaned = clean_data(itm)
            ns = "Unknown"
            ns_list = cleaned.get("namespaces")
            if not ns_list and itm.get("ir"):
                ns_list = itm["ir"].get("namespaces")
            if ns_list and len(ns_list) > 0:
                ns = ns_list[0]
            util_groups[ns].append(cleaned)
            found_utils += 1
            processed.add(norm)
            continue

        # ignore others

    print(f"Found {found_pages} pages (combined) and {found_utils} utility modules across {len(page_groups) + len(util_groups)} namespaces. Generating prompts...")

    # Save one prompt file per page pair and one per utility module
    def _save_page_pair(out_dir: str, ns: str, idx: int, pair_obj: dict):
        os.makedirs(out_dir, exist_ok=True)
        primary = (pair_obj.get("pageFile") or pair_obj.get("codeBehindFile") or "unknown")
        safe = _safe_filename(primary)
        filename = f"Page_{ns.replace('.', '_')}_{idx}_{safe}.txt"
        content = PAGE_TEMPLATE
        content = content.replace("{page_file}", pair_obj.get("pageFile") or "")
        content = content.replace("{codebehind_file}", pair_obj.get("codeBehindFile") or "")
        content = content.replace("{code_chunk}", json.dumps(pair_obj, indent=2))
        content = content.replace("{page_title}", (pair_obj.get("pageFile") or pair_obj.get("codeBehindFile") or safe))
        out_path = os.path.join(out_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved page prompt: {out_path}")

    def _save_module(out_dir: str, ns: str, idx: int, module_obj: dict):
        os.makedirs(out_dir, exist_ok=True)
        primary = (module_obj.get("file") or module_obj.get("fileName") or "module")
        safe = _safe_filename(primary)
        filename = f"Module_{ns.replace('.', '_')}_{idx}_{safe}.txt"
        content = UTIL_TEMPLATE
        content = content.replace("{module_name}", primary)
        content = content.replace("{module_file}", primary)
        content = content.replace("{code_chunk}", json.dumps(module_obj, indent=2))
        out_path = os.path.join(out_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved module prompt: {out_path}")

    # Emit page prompts
    for ns, items in page_groups.items():
        out_dir = PAGE_OUTPUT_DIR
        for i, obj in enumerate(items, start=1):
            _save_page_pair(out_dir, ns, i, obj)

    # Emit utility prompts
    for ns, items in util_groups.items():
        out_dir = UTIL_OUTPUT_DIR
        for i, obj in enumerate(items, start=1):
            _save_module(out_dir, ns, i, obj)

    # Write a manifest so callers can know exactly what was produced (per-job if job id provided)
    try:
        job_id = os.environ.get("ANALYZER_JOB_ID") or os.environ.get("JOB_ID") or "global"
        manifest_files = []
        for d in (PAGE_OUTPUT_DIR, UTIL_OUTPUT_DIR):
            if os.path.isdir(d):
                for f in sorted(os.listdir(d)):
                    if f.endswith(".txt"):
                        manifest_files.append(os.path.join(os.path.relpath(d, PROMPTS_OUTPUT_BASE), f).replace("\\", "/"))
        manifest = {
            "job_id": job_id,
            "expected": len(manifest_files),
            "files": manifest_files
        }
        # write AI-specific manifest so we don't overwrite the final manifest prematurely
        manifest_path = os.path.join(PROMPTS_OUTPUT_BASE, f"manifest_ai_{job_id}.json")
        with open(manifest_path, "w", encoding="utf-8") as mf:
            json.dump(manifest, mf, indent=2)
        print(f"Wrote AI manifest: {manifest_path} (expected={manifest['expected']})")
    except Exception as e:
        print(f"Error writing manifest: {e}")

    print(f"DONE! Page prompts saved in '{PAGE_OUTPUT_DIR}', module prompts saved in '{UTIL_OUTPUT_DIR}'.")
if __name__ == "__main__":
    main()