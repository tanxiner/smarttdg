import os
import re
import zlib
import shutil
import subprocess
import time
import socket
from collections import Counter
from langchain_community.llms import Ollama
from urllib.parse import urlparse

# --- CONFIGURATION ---
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
PROMPTS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "prompts_output")
ANALYSIS_OUTPUT_BASE = os.path.join(BACKEND_DIR, "analysis_output")

INPUT_FOLDER = os.path.join(PROMPTS_OUTPUT_BASE, "SQL_Documentation_Prompts")
OUTPUT_FOLDER = os.path.join(ANALYSIS_OUTPUT_BASE, "Final_SQL_Docs")

DEFAULT_MODEL = "gemma3:latest"
MODEL_NAME = os.environ.get("ANALYSIS_MODEL", DEFAULT_MODEL)
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
MAX_RETRIES = 3

def standardize_sql_headings(text: str) -> str:
    if not text:
        return text

    text = text.replace("\r\n", "\n").replace("\r", "\n")

    text = re.sub(
        r"^\s*(?:\*\*)?(?:#+\s*)?procedure(?:\*\*)?\s*:\s*",
        "# Procedure: ",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    replacements = {
        "purpose": "### Purpose",
        "parameters": "### Parameters",
        "logic flow": "### Logic Flow",
        "data interactions": "### Data Interactions",
    }

    for key, replacement in replacements.items():
        text = re.sub(
            rf"^\s*(?:\*\*)?(?:#+\s*)?{re.escape(key)}(?:\*\*)?\s*:\s*(.*?)\s*$",
            lambda m: replacement if not m.group(1).strip() else f"{replacement}\n{m.group(1).strip()}",
            text,
            flags=re.IGNORECASE | re.MULTILINE,
        )

        text = re.sub(
            rf"^\s*\*\*{re.escape(key)}\*\*\s+(.+?)\s*$",
            lambda m: f"{replacement}\n{m.group(1).strip()}",
            text,
            flags=re.IGNORECASE | re.MULTILINE,
        )

        text = re.sub(
            rf"^\s*{re.escape(key)}\s+(.+?)\s*$",
            lambda m: f"{replacement}\n{m.group(1).strip()}",
            text,
            flags=re.IGNORECASE | re.MULTILINE,
        )

        text = re.sub(
            rf"^\s*(?:\*\*)?(?:#+\s*)?{re.escape(key)}(?:\*\*)?\s*$",
            replacement,
            text,
            flags=re.IGNORECASE | re.MULTILINE,
        )

    text = re.sub(
        r"\n{0,1}(###\s+(?:Purpose|Parameters|Logic Flow|Data Interactions)\b)",
        r"\n\n\1",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(
        r"^(#\s*Procedure:.*)\n*(\*\*File:\*\*.*)?\n*(\*\*Path:\*\*.*)?\n*(###\s+Purpose\b)",
        lambda m: (
            f"{m.group(1)}\n\n"
            f"{m.group(2) + chr(10) if m.group(2) else ''}"
            f"{m.group(3) + chr(10) if m.group(3) else ''}"
            f"\n{m.group(4)}"
        ),
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip()


def normalize_plain_sql_sections(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")

    text = re.sub(r"(?im)^\s*parameters\s*:\s*$", "### Parameters", text)
    text = re.sub(r"(?im)^\s*logic flow\s*:\s*$", "### Logic Flow", text)
    text = re.sub(r"(?im)^\s*data interactions\s*:\s*$", "### Data Interactions", text)

    text = re.sub(r"(?im)^\s*reads\s*:\s*(.*)$", r"* **Reads:** \1", text)
    text = re.sub(r"(?im)^\s*writes\s*:\s*(.*)$", r"* **Writes:** \1", text)
    text = re.sub(r"(?im)^\s*joins\s*:\s*(.*)$", r"* **Joins:** \1", text)
    text = re.sub(r"(?im)^\s*calls\s*:\s*(.*)$", r"* **Calls:** \1", text)

    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def strip_template_placeholders(text: str) -> str:
    if not text:
        return text

    patterns = [
        r"(?i)one clear sentence explaining the business task\.\s*",
        r"(?i)step[- ]by[- ]step plain english explanation\.\s*",
        r"(?i)describe the sequence of operations performed in this part of the procedure\.\s*",
        r"(?i)list tables explicitly selected from\.?\s*",
        r"(?i)list tables inserted/updated/deleted\.?\s*",
        r"(?i)tables joined in select queries\.?\s*",
    ]

    for p in patterns:
        text = re.sub(p, "", text)

    return text.strip()


def normalize_leading_purpose_block(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n").strip()

    text = re.sub(
        r"(?i)^\s*one clear sentence explaining the business task\.\s*",
        "",
        text,
        count=1,
    ).lstrip()

    if re.search(r"^\s*###\s*Purpose\b", text, flags=re.IGNORECASE | re.MULTILINE):
        return text

    m = re.search(
        r"^(.*?)(?=^\s*(?:###\s*Parameters\b|Parameters\s*:|###\s*Logic\s*Flow\b|Logic\s*Flow\s*:|###\s*Data\s*Interactions\b|Data\s*Interactions\s*:)\s*)",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if not m:
        return text

    prefix = m.group(1).rstrip()
    lines = [ln.strip() for ln in prefix.splitlines() if ln.strip()]
    if not lines:
        return text

    keep = []
    purpose_lines = []

    for ln in lines:
        if (
            re.match(r"^\s*#\s*Procedure\s*:", ln, flags=re.IGNORECASE)
            or re.match(r"^\s*\*\*File:\*\*", ln, flags=re.IGNORECASE)
            or re.match(r"^\s*\*\*Path:\*\*", ln, flags=re.IGNORECASE)
        ):
            keep.append(ln)
        else:
            purpose_lines.append(ln)

    if not purpose_lines:
        return text

    purpose_text = " ".join(purpose_lines).strip()
    rest = text[m.end():].lstrip()

    rebuilt = "\n".join(keep)
    if rebuilt:
        rebuilt += "\n\n"
    rebuilt += f"### Purpose\n{purpose_text}"
    if rest:
        rebuilt += "\n\n" + rest

    return rebuilt.strip()


def strip_global_context_and_below(text: str) -> str:
    if not text:
        return text

    text = re.sub(
        r"\n+#+\s*GLOBAL\s+CONTEXT\b.*$",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    return text.rstrip()


def clean_response(text: str) -> str:
    text = text or ""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)

    # remove fenced block markers
    text = re.sub(r"(?im)^\s*```[a-zA-Z0-9_-]*\s*$", "", text)
    text = text.replace("```", "")

    text = re.sub(
        r"^\s*(Okay|Sure|Here is|Let me|I have|Below is).*?\n",
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


def extract_expected_procedure_name(prompt_text: str) -> str:
    m = re.search(r"\*\*ProcedureName:\*\*\s*(.+)", prompt_text, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()

    m = re.search(r"#\s*Procedure\s*:\s*(.+)", prompt_text, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()

    return "Unknown_Procedure"

def extract_source_file(prompt_text: str) -> str:
    m = re.search(r"\*\*File:\*\*\s*(.*)", prompt_text, flags=re.IGNORECASE)
    return (m.group(1).strip() if m else "") or "Unknown"


def extract_source_path(prompt_text: str) -> str:
    m = re.search(r"\*\*Path:\*\*\s*(.*)", prompt_text, flags=re.IGNORECASE)
    return (m.group(1).strip() if m else "") or "Unknown"

def extract_part_number(prompt_text: str) -> int | None:
    m = re.search(r"\*\*PartNumber:\*\*\s*(\d+)", prompt_text, flags=re.IGNORECASE)
    return int(m.group(1)) if m else None


def extract_total_parts(prompt_text: str) -> int | None:
    m = re.search(r"\*\*TotalParts:\*\*\s*(\d+)", prompt_text, flags=re.IGNORECASE)
    return int(m.group(1)) if m else None

def build_expected_procedure_title(prompt_text: str) -> str:
    base = extract_expected_procedure_name(prompt_text)
    part_num = extract_part_number(prompt_text)
    total_parts = extract_total_parts(prompt_text)

    if part_num and total_parts:
        return f"{base} (Part {part_num} of {total_parts})"
    return base

def replace_header_with_source(
    text: str,
    expected_proc_name: str,
    expected_source_file: str,
    expected_source_path: str,
) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n").strip()

    patterns = [
        r"^\s*#\s*Procedure\s*:.*$\n?",
        r"^\s*\*\*File:\*\*.*$\n?",
        r"^\s*\*\*Path:\*\*.*$\n?",
        r"^\s*File:.*Path:.*$\n?",   # File + Path on same line
        r"^\s*File:.*$\n?",          # File alone
        r"^\s*Path:.*$\n?",          # Path alone
    ]

    for pat in patterns:
        text = re.sub(pat, "", text, flags=re.IGNORECASE | re.MULTILINE)

    text = text.strip()

    header = (
        f"# Procedure: {expected_proc_name}\n\n"
        f"**File:** {expected_source_file}  \n"
        f"**Path:** {expected_source_path}"
    )

    if text:
        return f"{header}\n\n{text}".strip()

    return header

def extract_raw_sql_from_prompt(prompt_text: str) -> str:
    m = re.search(
        r"###\s*RAW\s+SQL\s+INPUT\s*(.*?)(?=^\s*###\s*FINAL\s+INSTRUCTION\b|\Z)",
        prompt_text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if m:
        return m.group(1).strip()
    return prompt_text or ""


def extract_proc_header_block(sql_text: str) -> str:
    if not sql_text:
        return ""

    lines = sql_text.replace("\r\n", "\n").replace("\r", "\n").splitlines()
    if not lines:
        return ""

    start_idx = None
    for i, line in enumerate(lines):
        if re.search(r"(?i)\b(?:create|alter)\s+(?:or\s+alter\s+)?(?:proc|procedure)\b", line):
            start_idx = i
            break

    if start_idx is None:
        return ""

    collected = []
    paren_depth = 0

    for i in range(start_idx, len(lines)):
        line = lines[i]
        collected.append(line)
        paren_depth += line.count("(") - line.count(")")

        if paren_depth <= 0 and re.match(r"^\s*AS\b", line, flags=re.IGNORECASE):
            break

    return "\n".join(collected)


def extract_sql_parameters(prompt_text: str) -> list[dict]:
    sql = extract_raw_sql_from_prompt(prompt_text)
    header = extract_proc_header_block(sql)
    if not header:
        return []

    first_param = re.search(r"@\w+", header)
    if not first_param:
        return []

    param_text = header[first_param.start():]
    param_text = re.sub(r"(?is)\n\s*AS\b.*$", "", param_text).strip()

    params = []
    seen = set()

    param_pattern = re.compile(
        r"@(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s+"
        r"(?:AS\s+)?"
        r"(?P<dtype>"
        r"(?:\[[^\]]+\]|\w+)"
        r"(?:\s*\([^)]*\))?"
        r"(?:\s+VARYING)?"
        r")"
        r"(?:\s*=\s*(?P<default>[^,\n]+))?"
        r"(?:\s+(?P<output>OUTPUT|OUT))?",
        flags=re.IGNORECASE,
    )

    for m in param_pattern.finditer(param_text):
        name = "@" + m.group("name")
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)

        dtype = (m.group("dtype") or "").strip()
        params.append({
            "name": name,
            "type": dtype,
            "is_output": bool(m.group("output")),
        })

    return params


def infer_parameter_purpose(name: str, is_output: bool = False) -> str:
    n = (name or "").lower()

    if is_output:
        if n in {"@ret", "@result", "@returnvalue", "@return_value"}:
            return "Output status code returned by the procedure"
        if "id" in n:
            return "Output identifier produced by the procedure"
        if "msg" in n or "message" in n or "error" in n:
            return "Output message returned by the procedure"
        if "status" in n:
            return "Output status returned by the procedure"
        return "Output value returned by the procedure"

    if "id" in n and n not in {"@from"}:
        return "Identifier used by the procedure"
    if "user" in n:
        return "User-related input used by the procedure"
    if "date" in n or "time" in n:
        return "Date or time input used by the procedure"
    if "status" in n:
        return "Status-related input used by the procedure"
    if "msg" in n or "message" in n:
        return "Message content used by the procedure"
    if "subject" in n:
        return "Subject text used by the procedure"
    if "sender" in n:
        return "Sender-related input used by the procedure"
    if n == "@from":
        return "Source or sender address used by the procedure"
    if "to" in n or "cc" in n or "bcc" in n:
        return "Recipient-related input used by the procedure"
    if "separator" in n:
        return "Separator character used to split input values"
    if "attachment" in n:
        return "Attachment-related input used by the procedure"
    if "ref" in n:
        return "Reference-related parameter used by the procedure"

    return "Parameter used by the procedure"


def build_parameters_section_from_source(prompt_text: str) -> str:
    params = extract_sql_parameters(prompt_text)
    if not params:
        return "### Parameters\nNone"

    lines = [
        "### Parameters",
        "| Name | Type | Purpose |",
        "| :--- | :--- | :--- |",
    ]
    for p in params:
        lines.append(
            f"| {p['name']} | {p['type']} | {infer_parameter_purpose(p['name'], p.get('is_output', False))} |"
        )
    return "\n".join(lines)


def replace_parameters_section_with_source(text: str, original_prompt: str) -> str:
    source_section = build_parameters_section_from_source(original_prompt)

    m = re.search(
        r"^\s*###\s*Parameters\b.*?(?=^\s*###\s*Logic\s*Flow\b|\Z)",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if m:
        text = text[:m.start()] + source_section + "\n\n" + text[m.end():]
    else:
        logic_m = re.search(r"^\s*###\s*Logic\s*Flow\b", text, flags=re.IGNORECASE | re.MULTILINE)
        purpose_m = re.search(
            r"^\s*###\s*Purpose\b.*?(?=^\s*###|\Z)",
            text,
            flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
        )

        if logic_m:
            text = text[:logic_m.start()] + source_section + "\n\n" + text[logic_m.start():]
        elif purpose_m:
            text = text[:purpose_m.end()] + "\n\n" + source_section + text[purpose_m.end():]
        else:
            text += "\n\n" + source_section

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def normalize_sql_identifier(identifier: str) -> str:
    identifier = (identifier or "").strip()
    if not identifier:
        return ""

    identifier = re.sub(r"[;,]+$", "", identifier).strip()

    if identifier.startswith("("):
        return ""

    parts = re.findall(r"\[([^\]]+)\]|([@#A-Za-z0-9_]+)", identifier)
    tokens = []
    for a, b in parts:
        tokens.append(a or b)

    if not tokens:
        return identifier.strip("[]")

    if tokens[0].startswith("@"):
        return tokens[0]
    if tokens[0].startswith("##"):
        return tokens[0]
    if tokens[0].startswith("#"):
        return tokens[0]

    return tokens[-1]


def strip_sql_comments_and_literals(sql: str) -> str:
    sql = sql or ""
    sql = re.sub(r"/\*.*?\*/", " ", sql, flags=re.DOTALL)
    sql = re.sub(r"--.*?$", " ", sql, flags=re.MULTILINE)
    sql = re.sub(r"'(?:''|[^'])*'", "''", sql)
    return sql


def split_sql_statements(sql: str) -> list[str]:
    sql = (sql or "").replace("\r\n", "\n").replace("\r", "\n")
    parts = re.split(r"(?im)^\s*GO\s*$", sql)
    parts = [p.strip() for p in parts if p.strip()]
    return parts if parts else [sql]


def extract_table_names_from_sql(prompt_text: str) -> dict:
    sql = extract_raw_sql_from_prompt(prompt_text)
    scrubbed = strip_sql_comments_and_literals(sql)
    statements = split_sql_statements(scrubbed)

    reads = []
    writes = []
    joins = []

    declared_table_vars = set()
    for stmt in statements:
        stmt_norm = re.sub(r"\s+", " ", stmt).strip()
        for m in re.finditer(r"(?i)\bdeclare\s+(@\w+)\s+table\b", stmt_norm):
            declared_table_vars.add(m.group(1).lower())

    def add_unique(target: list[str], raw_name: str):
        name = normalize_sql_identifier(raw_name)
        if not name:
            return

        if name.startswith("@") and name.lower() not in declared_table_vars:
            return

        bad = {
            "select", "insert", "update", "delete", "merge", "into", "from", "join",
            "set", "values", "null", "case", "when", "then", "else", "end",
            "on", "and", "or", "as", "begin", "try", "catch", "distinct",
            "top", "where", "group", "order", "by", "left", "right", "inner",
            "outer", "cross", "full", "openquery", "openrowset", "output",
            "tvf"
        }
        if name.lower() in bad:
            return

        if re.match(r"^\d+$", name):
            return

        if name.lower() not in {x.lower() for x in target}:
            target.append(name)

    def build_alias_map(stmt_norm: str) -> dict[str, str]:
        alias_map = {}

        patterns = [
            r"(?i)\bfrom\s+([@#\[\]\w\.]+)\s+(?:as\s+)?([A-Za-z_][A-Za-z0-9_]*)\b",
            r"(?i)\bjoin\s+([@#\[\]\w\.]+)\s+(?:as\s+)?([A-Za-z_][A-Za-z0-9_]*)\b",
            r"(?i)\bupdate\s+([A-Za-z_][A-Za-z0-9_]*)\b.*?\bfrom\s+([@#\[\]\w\.]+)\s+(?:as\s+)?\1\b",
            r"(?i)\bdelete\s+([A-Za-z_][A-Za-z0-9_]*)\b.*?\bfrom\s+([@#\[\]\w\.]+)\s+(?:as\s+)?\1\b",
        ]

        for pattern in patterns:
            for m in re.finditer(pattern, stmt_norm):
                g1, g2 = m.group(1), m.group(2)

                if pattern.startswith(r"(?i)\bupdate") or pattern.startswith(r"(?i)\bdelete"):
                    alias = g1
                    table = g2
                else:
                    table = g1
                    alias = g2

                table_name = normalize_sql_identifier(table)
                if table_name:
                    alias_map[alias.lower()] = table_name

        return alias_map

    def resolve_name(raw_name: str, alias_map: dict[str, str]) -> str:
        raw_name = (raw_name or "").strip()
        norm = normalize_sql_identifier(raw_name)
        if not norm:
            return ""
        return alias_map.get(norm.lower(), norm)

    def extract_from_comma_sources(stmt_norm: str) -> list[str]:
        results = []
        m = re.search(
            r"(?is)\bfrom\s+(.+?)(?=\bwhere\b|\bgroup\b|\border\b|\bhaving\b|\bunion\b|\boption\b|$)",
            stmt_norm
        )
        if not m:
            return results

        from_body = m.group(1).strip()

        if "(" in from_body and ")" in from_body:
            return results

        parts = [p.strip() for p in from_body.split(",") if p.strip()]
        for part in parts:
            first = part.split()[0]
            results.append(first)

        return results

    for stmt in statements:
        stmt_norm = re.sub(r"\s+", " ", stmt).strip()
        alias_map = build_alias_map(stmt_norm)

        for m in re.finditer(r"(?i)\bcreate\s+table\s+([@#\[\]\w\.]+)", stmt_norm):
            add_unique(writes, m.group(1))

        for m in re.finditer(r"(?i)\bdeclare\s+(@\w+)\s+table\b", stmt_norm):
            add_unique(writes, m.group(1))

        for m in re.finditer(r"(?i)\bselect\b.*?\binto\s+([@#\[\]\w\.]+)", stmt_norm):
            add_unique(writes, m.group(1))

        for m in re.finditer(r"(?i)\binsert\s+into\s+([@#\[\]\w\.]+)", stmt_norm):
            add_unique(writes, m.group(1))

        for m in re.finditer(r"(?i)\bupdate\s+([@#\[\]\w\.]+)", stmt_norm):
            target = resolve_name(m.group(1), alias_map)
            add_unique(writes, target)
            add_unique(reads, target)

        for m in re.finditer(r"(?i)\bdelete\s+from\s+([@#\[\]\w\.]+)", stmt_norm):
            target = resolve_name(m.group(1), alias_map)
            add_unique(writes, target)
            add_unique(reads, target)

        for m in re.finditer(r"(?i)\bdelete\s+([A-Za-z_][A-Za-z0-9_]*)\b", stmt_norm):
            target = resolve_name(m.group(1), alias_map)
            add_unique(writes, target)
            add_unique(reads, target)

        for m in re.finditer(r"(?i)\bmerge\s+into\s+([@#\[\]\w\.]+)", stmt_norm):
            target = resolve_name(m.group(1), alias_map)
            add_unique(writes, target)
            add_unique(reads, target)

        for m in re.finditer(r"(?i)\busing\s+([@#\[\]\w\.]+)", stmt_norm):
            source = resolve_name(m.group(1), alias_map)
            add_unique(reads, source)

        for m in re.finditer(r"(?i)\bfrom\s+([@#\[\]\w\.]+)", stmt_norm):
            source = resolve_name(m.group(1), alias_map)
            add_unique(reads, source)

        for m in re.finditer(r"(?i)\b(?:inner|left|right|full|cross)?\s*join\s+([@#\[\]\w\.]+)", stmt_norm):
            joined = resolve_name(m.group(1), alias_map)
            add_unique(reads, joined)
            add_unique(joins, joined)

        # FROM
        from_sources = []
        for m in re.finditer(r"(?i)\bfrom\s+([@#\[\]\w\.]+)", stmt_norm):
            source = resolve_name(m.group(1), alias_map)
            add_unique(reads, source)
            from_sources.append(source)

        # JOIN
        explicit_join_sources = []
        for m in re.finditer(r"(?i)\b(?:inner|left|right|full|cross)?\s*join\s+([@#\[\]\w\.]+)", stmt_norm):
            joined = resolve_name(m.group(1), alias_map)
            add_unique(reads, joined)
            explicit_join_sources.append(joined)

        if explicit_join_sources:
            for src in from_sources:
                add_unique(joins, src)
            for src in explicit_join_sources:
                add_unique(joins, src)

        # Old-style comma joins: FROM A a, B b, C c
        comma_sources = extract_from_comma_sources(stmt_norm)
        for src in comma_sources:
            resolved = resolve_name(src, alias_map)
            add_unique(reads, resolved)

        if len(comma_sources) > 1:
            for src in comma_sources:
                resolved = resolve_name(src, alias_map)
                add_unique(joins, resolved)

    return {
        "reads": reads,
        "writes": writes,
        "joins": joins,
    }


def extract_called_procedures_from_sql(prompt_text: str) -> list[str]:
    sql = extract_raw_sql_from_prompt(prompt_text)
    scrubbed = strip_sql_comments_and_literals(sql)
    statements = split_sql_statements(scrubbed)

    calls = []

    def add_unique(raw_name: str):
        name = normalize_sql_identifier(raw_name)
        if not name:
            return

        bad = {"exec", "execute", "sp_executesql"}
        if name.lower() in bad:
            return

        if name.lower() not in {x.lower() for x in calls}:
            calls.append(name)

    for stmt in statements:
        stmt_norm = re.sub(r"\s+", " ", stmt).strip()

        for m in re.finditer(r"(?i)\bexec(?:ute)?\s+([#@\[\]\w\.]+)", stmt_norm):
            raw = m.group(1).strip()
            if raw.startswith("@"):
                continue
            add_unique(raw)

    return calls


def build_data_interactions_from_source(prompt_text: str) -> str:
    src = extract_table_names_from_sql(prompt_text)
    reads = src["reads"]
    writes = src["writes"]
    joins = src["joins"]
    calls = extract_called_procedures_from_sql(prompt_text)

    return "\n".join([
        "### Data Interactions",
        f"* **Reads:** {', '.join(reads[:20]) if reads else 'None/Unknown'}",
        f"* **Writes:** {', '.join(writes[:20]) if writes else 'None'}",
        f"* **Joins:** {', '.join(joins[:20]) if joins else 'None'}",
        f"* **Calls:** {', '.join(calls[:20]) if calls else 'None'}",
    ])


def replace_data_interactions_with_source(text: str, original_prompt: str) -> str:
    source_section = build_data_interactions_from_source(original_prompt)

    m = re.search(
        r"^\s*###\s*Data\s*Interactions\b.*$",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if m:
        text = text[:m.start()] + source_section
    else:
        text = text.rstrip() + "\n\n" + source_section

    return re.sub(r"\n{3,}", "\n\n", text).strip()


def enforce_sql_template(
    text: str,
    expected_proc_name: str,
    expected_source_file: str,
    expected_source_path: str,
) -> str:
    text = (text or "").strip()

    if not re.search(r"^\s*#\s*Procedure\s*:", text, flags=re.IGNORECASE | re.MULTILINE):
        text = (
            f"# Procedure: {expected_proc_name}\n\n"
            f"**File:** {expected_source_file}\n"
            f"**Path:** {expected_source_path}\n\n"
            f"{text}"
        )

    if not re.search(r"^\s*\*\*File:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
        text = re.sub(
            r"(^\s*#\s*Procedure:.*$)",
            lambda m: f"{m.group(1)}\n\n**File:** {expected_source_file}\n**Path:** {expected_source_path}",
            text,
            count=1,
            flags=re.IGNORECASE | re.MULTILINE,
        )
    elif not re.search(r"^\s*\*\*Path:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
        text = re.sub(
            r"(^\s*\*\*File:\*\*.*$)",
            lambda m: f"{m.group(1)}\n**Path:** {expected_source_path}",
            text,
            count=1,
            flags=re.IGNORECASE | re.MULTILINE,
        )

    return text


def salvage_sql_output(
    text: str,
    expected_proc_name: str,
    expected_source_file: str,
    expected_source_path: str,
) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n").strip()

    text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
    text = re.sub(r"\n```$", "", text)

    if not re.search(r"^\s*#\s*Procedure\s*:", text, flags=re.IGNORECASE | re.MULTILINE):
        text = f"# Procedure: {expected_proc_name}\n\n{text}"

    if not re.search(r"^\s*\*\*File:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
        text = re.sub(
            r"(^\s*#\s*Procedure:.*$)",
            lambda m: f"{m.group(1)}\n\n**File:** {expected_source_file}\n**Path:** {expected_source_path}",
            text,
            count=1,
            flags=re.IGNORECASE | re.MULTILINE,
        )
    elif not re.search(r"^\s*\*\*Path:\*\*", text, flags=re.IGNORECASE | re.MULTILINE):
        text = re.sub(
            r"(^\s*\*\*File:\*\*.*$)",
            lambda m: f"{m.group(1)}\n**Path:** {expected_source_path}",
            text,
            count=1,
            flags=re.IGNORECASE | re.MULTILINE,
        )

    text = re.sub(
        r"\s*(\*\*(?:Purpose|Parameters|Logic Flow|Data Interactions|Error Handling|Key Declarations and Temp Objects):\*\*)\s*",
        r"\n\n\1\n",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(
        r"^\s*\*\*Purpose:\*\*\s*(.+?)\s*$",
        r"### Purpose\n\1",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    text = re.sub(
        r"^\s*\*\*Logic Flow:\*\*\s*$",
        r"### Logic Flow",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    text = re.sub(
        r"^\s*\*\*Logic Flow:\*\*\s*(.+?)\s*$",
        r"### Logic Flow\n\1",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    text = re.sub(
        r"^\s*\*\*Data Interactions:\*\*\s*$",
        r"### Data Interactions",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    text = re.sub(
        r"^\s*\*\*Data Interactions:\*\*\s*(.+?)\s*$",
        r"### Data Interactions\n\1",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    text = re.sub(
        r"^\s*Purpose\s+so\s+far:\s*$",
        "### Purpose",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    text = re.sub(
        r"^\s*Known\s+data\s+interactions\s+so\s+far:\s*$",
        "### Data Interactions",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    text = re.sub(
        r"^\s*Key\s+logic\s+already\s+established:\s*$",
        "### Logic Flow",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    text = re.sub(
        r"\n{0,1}(###\s+(?:Purpose|Parameters|Logic Flow|Data Interactions)\b)",
        r"\n\n\1",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text

def remove_orphan_markdown_emphasis(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")

    # Remove lines that are only stray emphasis markers
    text = re.sub(r"(?m)^\s*\*{1,3}\s*$\n?", "", text)

    # Fix lines like: "** some text" -> "some text"
    text = re.sub(r"(?m)^\s*\*\*\s+(.+?)\s*$", r"\1", text)

    # Fix lines like: "* some text" only when they are clearly not meant to be bullets
    # Keep this conservative: only remove if not already a list item pattern you want.
    text = re.sub(r"(?m)^\s*\*\s+([A-Z][^\n]*)$", r"\1", text)

    # Remove trailing orphan emphasis at end of line: "text **" -> "text"
    text = re.sub(r"(?m)^(.*\S)\s+\*\*\s*$", r"\1", text)

    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def sanitize_data_interactions_block(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n").strip()

    text = re.sub(
        r"^\s*(?:#+\s*)?(?:\*\*)?Data Interactions(?:\*\*)?\s*:?\s*$",
        "### Data Interactions",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    m = re.search(
        r"^\s*###\s*Data Interactions\b(.*)$",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if not m:
        return text

    body = m.group(1).strip()

    if (
        re.search(r"^\|.*\|$", body, flags=re.MULTILINE)
        or "**Table" in body
        or "Column Name" in body
        or "Data Type" in body
        or "Description" in body
    ):
        new_block = "\n".join([
            "### Data Interactions",
            "* **Reads:** Unknown",
            "* **Writes:** None",
            "* **Joins:** None",
            "* **Calls:** None",
        ])
        text = re.sub(
            r"^\s*###\s*Data Interactions\b.*$",
            new_block,
            text,
            flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
        )
        return text.strip()

    lines = body.splitlines()
    reads = []
    writes = []
    joins = []
    calls = []
    current = None

    for line in lines:
        stripped = line.strip()

        if re.match(r"^\*\s*\*\*Reads:\*\*", stripped, flags=re.IGNORECASE):
            current = "reads"
            value = re.sub(r"^\*\s*\*\*Reads:\*\*\s*", "", stripped, flags=re.IGNORECASE).strip(" `")
            if value:
                reads.extend([v.strip(" `") for v in value.split(",") if v.strip()])
            continue

        if re.match(r"^\*\s*\*\*Writes:\*\*", stripped, flags=re.IGNORECASE):
            current = "writes"
            value = re.sub(r"^\*\s*\*\*Writes:\*\*\s*", "", stripped, flags=re.IGNORECASE).strip(" `")
            if value:
                writes.extend([v.strip(" `") for v in value.split(",") if v.strip()])
            continue

        if re.match(r"^\*\s*\*\*Joins:\*\*", stripped, flags=re.IGNORECASE):
            current = "joins"
            value = re.sub(r"^\*\s*\*\*Joins:\*\*\s*", "", stripped, flags=re.IGNORECASE).strip(" `")
            if value and value.lower() != "none":
                joins.extend([v.strip(" `") for v in value.split(",") if v.strip()])
            continue

        if re.match(r"^\*\s*\*\*Calls:\*\*", stripped, flags=re.IGNORECASE):
            current = "calls"
            value = re.sub(r"^\*\s*\*\*Calls:\*\*\s*", "", stripped, flags=re.IGNORECASE).strip(" `")
            if value and value.lower() != "none":
                calls.extend([v.strip(" `") for v in value.split(",") if v.strip()])
            continue

        nested = re.sub(r"^\*\s*", "", stripped).strip(" `")
        if not nested:
            continue

        if nested.lower() in {"column name", "data type", "description"}:
            continue
        if "|" in nested:
            continue
        if "primary key" in nested.lower():
            continue

        if current == "reads":
            reads.append(nested)
        elif current == "writes":
            writes.append(nested)
        elif current == "joins":
            joins.append(nested)
        elif current == "calls":
            calls.append(nested)

    def uniq(items):
        out = []
        seen = set()
        for item in items:
            key = item.lower()
            if key not in seen:
                seen.add(key)
                out.append(item)
        return out

    reads = uniq(reads)
    writes = uniq(writes)
    joins = uniq(joins)
    calls = uniq(calls)

    new_block = "\n".join([
        "### Data Interactions",
        f"* **Reads:** {', '.join(reads[:20]) if reads else 'Unknown'}",
        f"* **Writes:** {', '.join(writes[:20]) if writes else 'None'}",
        f"* **Joins:** {', '.join(joins[:20]) if joins else 'None'}",
        f"* **Calls:** {', '.join(calls[:20]) if calls else 'None'}",
    ])

    text = re.sub(
        r"^\s*###\s*Data Interactions\b.*$",
        new_block,
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )

    return text.strip()


def repair_sql_structure(
    text: str,
    expected_proc_name: str,
    expected_source_file: str,
    expected_source_path: str,
) -> str:
    text = enforce_sql_template(text, expected_proc_name, expected_source_file, expected_source_path)

    if not re.search(r"^\s*###\s*Purpose\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### Purpose\nNot clearly indicated"

    if not re.search(r"^\s*###\s*Logic Flow\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### Logic Flow\n1. Not clearly indicated"

    if not re.search(r"^\s*###\s*Data Interactions\b", text, flags=re.IGNORECASE | re.MULTILINE):
        text += "\n\n### Data Interactions\n* **Reads:** Unknown\n* **Writes:** None\n* **Joins:** None\n* **Calls:** None"
    else:
        if "**Reads:**" not in text:
            text += "\n* **Reads:** Unknown"
        if "**Writes:**" not in text:
            text += "\n* **Writes:** None"
        if "**Joins:**" not in text:
            text += "\n* **Joins:** None"
        if "**Calls:**" not in text:
            text += "\n* **Calls:** None"

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text

def fix_broken_logic_flow_numbering(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")

    # Collapse empty numbered item followed by bold label into same item
    text = re.sub(
        r"(?m)^(\d+\.)\s*$\n+\s*\*\*([^*]+)\*\*\s*:?\s*\n*",
        lambda m: f"{m.group(1)} {m.group(2).strip()}: ",
        text,
    )

    # Collapse double blank lines inside Logic Flow a bit
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()

def dedupe_data_interactions(text: str) -> str:
    m = re.search(
        r"(###\s*Data Interactions\s*\n)(.*)$",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if not m:
        return text

    header = m.group(1)
    body = m.group(2)

    reads = []
    writes = []
    joins = []
    calls = []

    current = None
    for line in body.splitlines():
        stripped = line.strip()

        if re.match(r"^\*\s*\*\*Reads:\*\*", stripped, flags=re.IGNORECASE):
            current = "reads"
            value = re.sub(r"^\*\s*\*\*Reads:\*\*\s*", "", stripped, flags=re.IGNORECASE).strip()
            if value:
                reads.append(value)
            continue

        if re.match(r"^\*\s*\*\*Writes:\*\*", stripped, flags=re.IGNORECASE):
            current = "writes"
            value = re.sub(r"^\*\s*\*\*Writes:\*\*\s*", "", stripped, flags=re.IGNORECASE).strip()
            if value:
                writes.append(value)
            continue

        if re.match(r"^\*\s*\*\*Joins:\*\*", stripped, flags=re.IGNORECASE):
            current = "joins"
            value = re.sub(r"^\*\s*\*\*Joins:\*\*\s*", "", stripped, flags=re.IGNORECASE).strip()
            if value:
                joins.append(value)
            continue

        if re.match(r"^\*\s*\*\*Calls:\*\*", stripped, flags=re.IGNORECASE):
            current = "calls"
            value = re.sub(r"^\*\s*\*\*Calls:\*\*\s*", "", stripped, flags=re.IGNORECASE).strip()
            if value:
                calls.append(value)
            continue

        bullet = re.sub(r"^\*\s*", "", stripped).strip()
        if not bullet:
            continue

        if current == "reads":
            reads.append(bullet)
        elif current == "writes":
            writes.append(bullet)
        elif current == "joins":
            joins.append(bullet)
        elif current == "calls":
            calls.append(bullet)

    def normalize_items(items):
        out = []
        seen = set()
        for item in items:
            item = re.sub(
                r"\([^)]*(select|insert|update|delete|merge|from|where)[^)]*\)",
                "",
                item,
                flags=re.IGNORECASE,
            ).strip(" `")
            parts = [p.strip(" `") for p in re.split(r",|\n", item) if p.strip()]
            for p in parts:
                key = p.lower()
                if key not in seen:
                    seen.add(key)
                    out.append(p)
        return out

    reads = normalize_items(reads)
    writes = normalize_items(writes)
    joins = normalize_items(joins)
    calls = normalize_items(calls)

    def fmt(label, items, empty_default):
        if not items:
            return f"* **{label}:** {empty_default}"
        return f"* **{label}:** " + ", ".join(items[:20])

    new_block = "\n".join([
        header.rstrip(),
        fmt("Reads", reads, "Unknown"),
        fmt("Writes", writes, "None"),
        fmt("Joins", joins, "None"),
        fmt("Calls", calls, "None"),
    ])

    text = re.sub(
        r"###\s*Data Interactions\s*\n.*$",
        new_block,
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    return text


def detect_excessive_duplicate_lines(text, min_line_len=25, duplicate_threshold=6, dominance_threshold=0.35):
    raw_lines = [ln.strip() for ln in (text or "").splitlines()]
    raw_lines = [ln for ln in raw_lines if ln and len(ln) >= min_line_len]

    if not raw_lines:
        return False, "No meaningful lines"

    normalized = []
    for ln in raw_lines:
        ln2 = re.sub(r"^\s*(?:\d+[\.\)]\s*|[-*]\s+)", "", ln).strip()
        normalized.append(ln2)

    counts = Counter(normalized)
    _, most_common_count = counts.most_common(1)[0]

    if most_common_count >= duplicate_threshold:
        return True, f"Repeated normalized line detected {most_common_count} times"

    duplicated_total = sum(c for _, c in counts.items() if c > 1)
    if duplicated_total / len(normalized) > dominance_threshold:
        return True, f"Too many duplicated normalized lines ({duplicated_total}/{len(normalized)})"

    return False, "OK"


def detect_repeated_line_chunks(text: str, window_size: int = 3, repeat_threshold: int = 3):
    lines = [ln.strip() for ln in (text or "").splitlines()]
    lines = [ln for ln in lines if ln]

    if len(lines) < window_size * 2:
        return False, "Not enough lines for chunk check"

    normalized = []
    for ln in lines:
        ln = re.sub(r"^\s*(?:\d+[\.\)]\s*|[-*]\s+)", "", ln).strip()
        ln = re.sub(r"\s+", " ", ln)
        normalized.append(ln)

    chunks = []
    for i in range(len(normalized) - window_size + 1):
        chunk = "\n".join(normalized[i:i + window_size])
        chunks.append(chunk)

    counts = Counter(chunks)
    most_common_chunk, most_common_count = counts.most_common(1)[0]
    snippet = most_common_chunk[:200]
    if most_common_count >= repeat_threshold:
        return True, f"Repeated line chunk detected {most_common_count} times: {snippet}"

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


def contains_template_placeholders(text: str):
    text_lower = (text or "").lower()
    placeholder_phrases = [
        "one clear sentence explaining the business task.",
        "describe the sequence of operations performed in this part of the procedure.",
        "inferred usage",
        "list tables explicitly selected from",
        "list tables inserted/updated/deleted",
        "@paramname",
        "datatype",
        "step-by-step plain english explanation.",
        "do not leave purpose out.",
        "if none, write none.",
        "tables joined in select queries",
        "if none, write none, but only once you have checked that it is actually none.",
        "start your response with exactly",
    ]
    for phrase in placeholder_phrases:
        if phrase in text_lower:
            return phrase
    return None


def looks_like_raw_sql(text: str) -> bool:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    text_lower = text.lower()

    if "### raw sql input" in text_lower:
        return True

    if "```" in text:
        return True

    if re.search(r"\b(?:create|alter)\s+(?:or\s+alter\s+)?(?:proc|procedure)\b", text, flags=re.IGNORECASE):
        return True

    scan_lines = []
    for line in text.splitlines():
        stripped = line.strip()

        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if re.match(r"^\*\s*\*\*(Reads|Writes|Joins|Calls):\*\*", stripped, flags=re.IGNORECASE):
            continue

        if re.match(r"^\d+[\.\)]\s+", stripped):
            stripped = re.sub(r"^\d+[\.\)]\s+", "", stripped).strip()
        if re.match(r"^\*\s+", stripped):
            stripped = re.sub(r"^\*\s+", "", stripped).strip()

        scan_lines.append(stripped)

    sql_like_lines = 0

    for line in scan_lines:
        low = line.lower()

        if re.match(r"^\s*--", line):
            return True

        # only count lines that look like actual SQL, not prose
        actual_sql = any([
            re.match(r"^select\s+.+\s+from\s+.+\b(where|join|group\s+by|order\s+by|having|union)\b", low),
            re.match(r"^insert\s+into\s+.+\b(values|select)\b", low),
            re.match(r"^update\s+.+\s+set\s+.+", low),
            re.match(r"^delete\s+from\s+.+", low),
            re.match(r"^merge\s+into\s+.+", low),
            re.match(r"^truncate\s+table\s+.+", low),
            re.match(r"^declare\s+@\w+\s+", low),
            re.match(r"^set\s+@\w+\s*=", low),
            re.match(r"^exec(?:ute)?\s+[\[\]\w\.]+", low),
            re.match(r"^begin\s+transaction\b", low),
            re.match(r"^commit\s+transaction\b", low),
            re.match(r"^rollback\s+transaction\b", low),
            re.match(r"^fetch\s+next\s+from\s+\w+", low),
        ])

        # prose guard: skip obvious English explanation lines
        prose_like = any([
            low.startswith("select the "),
            low.startswith("insert the "),
            low.startswith("update the "),
            low.startswith("delete the "),
            low.startswith("declare and "),
            low.startswith("set the "),
            low.startswith("if "),
            low.startswith("return "),
            low.startswith("create a "),
            low.startswith("drop the "),
            low.startswith("construct "),
            low.startswith("retrieve "),
        ])

        if actual_sql and not prose_like:
            sql_like_lines += 1

    return sql_like_lines >= 2


def detect_sql_placeholder_only_sections(text: str):
    errors = []

    purpose_match = re.search(
        r"^\s*###\s*Purpose\b(.*?)(?=^\s*###\s*Parameters\b|^\s*###\s*Logic\s*Flow\b|^\s*###\s*Data\s*Interactions\b|\Z)",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if purpose_match:
        purpose_body = purpose_match.group(1).strip()
        if not purpose_body or purpose_body.lower() in {"not clearly indicated", "none", "unknown"}:
            errors.append("Purpose section is only a placeholder")

    logic_match = re.search(
        r"^\s*###\s*Logic\s*Flow\b(.*?)(?=^\s*###\s*Data\s*Interactions\b|\Z)",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if logic_match:
        logic_body = logic_match.group(1).strip()
        logic_norm = re.sub(r"\s+", " ", logic_body.lower())
        if not logic_body or logic_norm in {
            "1. not clearly indicated",
            "not clearly indicated",
            "none",
            "unknown",
        }:
            errors.append("Logic Flow section is only a placeholder")

    data_match = re.search(
        r"^\s*###\s*Data\s*Interactions\b(.*)$",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if data_match:
        data_body = data_match.group(1).strip().lower()
        reads_unknown = "**reads:** unknown" in data_body
        writes_placeholder = "**writes:** unknown" in data_body
        joins_placeholder = "**joins:** unknown" in data_body or "**joins:** none" in data_body
        calls_placeholder = "**calls:** unknown" in data_body or "**calls:** none" in data_body

        if reads_unknown and writes_placeholder and joins_placeholder and calls_placeholder:
            errors.append("Data Interactions section is only placeholder values")

    return errors


def strip_prompt_leakage(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")

    leakage_patterns = [
        r"(?ims)^##\s*Key Declarations:.*?(?=^\s*###\s|\Z)",
        r"(?ims)^###\s*Key Declarations\b.*?(?=^\s*###\s|\Z)",
        r"(?ims)^Key Declarations:.*?(?=^\s*###\s|\Z)",
        r"(?ims)^Temp/Table Variable Objects:.*?(?=^\s*###\s|\Z)",
        r"(?ims)^Main Table References:.*?(?=^\s*###\s|\Z)",
        r"(?ims)^###\s*FINAL OUTPUT\b.*?(?=^\s*###\s|\Z)",
        r"(?ims)^###\s*SYSTEM ROLE\b.*?(?=^\s*###\s*TASK\b|\Z)",
        r"(?ims)^###\s*TASK\b.*?(?=^\s*###\s*REQUIRED OUTPUT\b|\Z)",
        r"(?ims)^###\s*REQUIRED OUTPUT\b.*?(?=^\s*#\s*Procedure\b|\Z)",
        r"(?ims)^###\s*STRICT RULES\b.*$",
        r"(?ims)^###\s*ORIGINAL SOURCE PROMPT\b.*$",
        r"(?ims)^###\s*CURRENT DRAFT\b.*$",
    ]

    for pattern in leakage_patterns:
        text = re.sub(pattern, "", text)

    text = re.sub(r"(?im)^\s*@Message\s*$", "", text)
    text = re.sub(r"(?im)^\s*Do not add any sections after Logic Flow.*$", "", text)
    text = re.sub(r"(?im)^\s*Do not add the rules given.*$", "", text)

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def keep_only_through_logic_flow(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n").strip()

    proc_match = re.search(r"^\s*#\s*Procedure:.*$", text, flags=re.IGNORECASE | re.MULTILINE)
    file_match = re.search(r"^\s*\*\*File:\*\*.*$", text, flags=re.IGNORECASE | re.MULTILINE)
    path_match = re.search(r"^\s*\*\*Path:\*\*.*$", text, flags=re.IGNORECASE | re.MULTILINE)

    purpose_match = re.search(
        r"^\s*###\s*Purpose\b.*?(?=^\s*###\s*Logic\s*Flow\b|\Z)",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )

    logic_match = re.search(
        r"^\s*###\s*Logic\s*Flow\b.*?(?=^\s*###\s*\S+|\Z)",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )

    parts = []

    if proc_match:
        parts.append(proc_match.group(0).strip())
    if file_match:
        parts.append(file_match.group(0).strip())
    if path_match:
        parts.append(path_match.group(0).strip())
    if purpose_match:
        parts.append(purpose_match.group(0).strip())
    if logic_match:
        logic_block = logic_match.group(0).strip()

        # remove trailing code fences and stray fence lines
        logic_block = re.sub(r"\n?```+\s*$", "", logic_block, flags=re.MULTILINE).rstrip()
        logic_block = re.sub(r"(?im)^\s*```+\s*$", "", logic_block).strip()

        parts.append(logic_block)

    if parts:
        rebuilt = "\n\n".join(parts).strip()
        rebuilt = re.sub(r"(?im)^\s*```+\s*$", "", rebuilt).strip()
        rebuilt = re.sub(r"\n{3,}", "\n\n", rebuilt)
        return rebuilt

    text = re.sub(r"(?im)^\s*```+\s*$", "", text).strip()
    return text


def validate_output_all(text: str, original_prompt: str | None = None):
    errors = []
    text = (text or "").strip()
    text_lower = text.lower()

    if len(text) < 30:
        errors.append("Output empty")

    header_patterns = {
        "procedure": r"^\s*#+\s*procedure\s*:",
        "file": r"^\s*\*\*file:\*\*",
        "path": r"^\s*\*\*path:\*\*",
        "purpose": r"^\s*#+\s*purpose\b",
        "parameters": r"^\s*#+\s*parameters\b",
        "logic flow": r"^\s*#+\s*logic\s*flow\b",
        "data interactions": r"^\s*#+\s*data\s*interactions\b",
    }

    for name, pattern in header_patterns.items():
        if not re.search(pattern, text_lower, flags=re.MULTILINE):
            errors.append(f"Missing required section: {name}")

    if not re.match(r"^\s*#\s*Procedure\s*:\s*\S+", text, flags=re.IGNORECASE):
        errors.append("Missing or invalid procedure title")

    parameters_ok = (
        "| Name | Type | Purpose |" in text
        or re.search(r"^\s*###\s*Parameters\s*\n+\s*None\s*$", text, flags=re.IGNORECASE | re.MULTILINE)
    )
    if not parameters_ok:
        errors.append("Parameters section must contain a table or 'None'")

    if "**Reads:**" not in text:
        errors.append("Data Interactions missing Reads")
    if "**Writes:**" not in text:
        errors.append("Data Interactions missing Writes")
    if "**Joins:**" not in text:
        errors.append("Data Interactions missing Joins")
    if "**Calls:**" not in text:
        errors.append("Data Interactions missing Calls")

    data_block = re.search(
        r"###\s*Data Interactions\s*(.*)$",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if data_block and "|" in data_block.group(1):
        errors.append("Data Interactions contains markdown tables; only bullet summaries are allowed")

    placeholder = contains_template_placeholders(text)
    if placeholder:
        errors.append(f"Output still contains template placeholder text: '{placeholder}'")

    tail = text_lower[-400:]
    for p in ["do you want me to", "would you like me to", "let me know if", "i can also"]:
        if p in tail:
            errors.append("Detected conversational ending")
            break

    if looks_like_raw_sql(text):
        errors.append("Detected raw SQL code")

    if re.search(r"^\s*--", text, flags=re.MULTILINE):
        errors.append("Detected SQL-style comments in output")

    proc_titles = re.findall(r"^\s*#\s*Procedure\s*:", text, flags=re.IGNORECASE | re.MULTILINE)
    if len(proc_titles) != 1:
        errors.append(f"Expected exactly 1 procedure title, found {len(proc_titles)}")

    if re.search(r"(final instruction:|do not write anything before|do not write anything after)", text_lower):
        errors.append("Model copied prompt instructions into output")

    dup_bad, dup_reason = detect_excessive_duplicate_lines(text)
    if dup_bad:
        errors.append(dup_reason)

    chunk_bad, chunk_reason = detect_repeated_line_chunks(text)
    if chunk_bad:
        errors.append(chunk_reason)

    table_bad, table_reason = detect_duplicate_table_rows(text)
    if table_bad:
        errors.append(table_reason)

    if len(text) > 300:
        compressed = zlib.compress(text.encode("utf-8"))
        ratio = len(compressed) / len(text)
        if ratio < 0.15:
            errors.append(f"Gibberish detected (ratio: {ratio:.2f})")

    if original_prompt:
        errors.extend(detect_sql_placeholder_only_sections(text))

    return (len(errors) == 0), errors


def is_minor_only(errors: list[str]) -> bool:
    if not errors:
        return False

    minor_whitelist = {
        "Missing required section: purpose",
        "Missing required section: parameters",
        "Missing required section: logic flow",
        "Missing required section: data interactions",
    }
    return all(e in minor_whitelist for e in errors)


def build_retry_prompt(cleaned: str, original_prompt: str, errors: list[str]) -> str:
    error_text = "\n".join(f"- {e}" for e in errors)

    hide_current_draft_markers = [
        "gibberish detected",
        "repeated normalized line detected",
        "too many duplicated normalized lines",
        "repeated line chunk detected",
        "duplicate table row repeated",
    ]

    should_hide_current_draft = any(
        marker in e.lower()
        for e in errors
        for marker in hide_current_draft_markers
    )

    prompt_parts = [
        "### 🛑 CRITICAL INSTRUCTION",
        "Your previous output failed validation.",
        "",
        "Fix ALL of these issues:",
        error_text,
        "",
        "Return ONLY one corrected document.",
        "",
        "IMPORTANT RULES:",
        "- Preserve any already-correct sections.",
        "- Do NOT remove correct headings.",
        "- Do NOT write SQL.",
        "- Do NOT use SQL comments like --.",
        "- Do NOT include a RAW SQL INPUT section.",
        "- Do NOT include prompt instructions in the answer.",
        "- Do NOT output a Parameters section. Parameters are generated automatically from source SQL.",
        "- Do NOT add introductions or conclusions.",
        "- Do NOT ask follow-up questions.",
        '- Purpose and Logic Flow must be filled with concrete information from the SQL body.',
        '- Do NOT leave Purpose as "Not clearly indicated" if the SQL body reveals intent.',
        '- Do NOT leave Logic Flow as "1. Not clearly indicated" if the SQL body shows processing steps.',
        '- NEVER output schema tables, column lists, or “Table[1] / Table[2]” blocks.',
        '- Do NOT describe columns, datatypes, primary keys, or expanded table structures.',
        '- Stop after Logic Flow. Do not output any extra sections from the model.',
        "- Do NOT output Procedure, File, or Path lines. They are generated automatically.",
        "",
        "SQL-SPECIFIC RULES:",
        "- Do NOT repeat the same table name multiple times.",
        "- Deduplicate all table names before writing them.",
        "- If too many tables are involved, list the main unique tables only.",
        "- Summarize operations in plain language instead.",
    ]

    if not should_hide_current_draft:
        prompt_parts.extend([
            "",
            "### CURRENT DRAFT",
            cleaned,
        ])

    prompt_parts.extend([
        "",
        "### ORIGINAL SOURCE PROMPT",
        original_prompt,
    ])

    return "\n".join(prompt_parts).strip()


def parse_part_info(filename: str):
    m = re.match(r"^(?P<prefix>\d+_[^\.]+?)_part(?P<part>\d+)\.txt$", filename, flags=re.IGNORECASE)
    if not m:
        return None
    base_key = m.group("prefix")
    part_num = int(m.group("part"))
    return base_key, part_num


def summarize_output_for_next_part(text: str, max_logic_steps: int = 4) -> str:
    text = text or ""

    purpose = re.search(r"#+\s*Purpose\s*(.*?)(?=\n#+\s*Parameters)", text, flags=re.IGNORECASE | re.DOTALL)
    params = re.search(r"#+\s*Parameters\s*(.*?)(?=\n#+\s*Logic Flow)", text, flags=re.IGNORECASE | re.DOTALL)
    logic = re.search(r"#+\s*Logic Flow\s*(.*?)(?=\n#+\s*Data Interactions)", text, flags=re.IGNORECASE | re.DOTALL)
    data = re.search(r"#+\s*Data Interactions\s*(.*)$", text, flags=re.IGNORECASE | re.DOTALL)

    logic_lines = []
    if logic:
        for ln in logic.group(1).splitlines():
            cleaned = ln.strip()
            if cleaned:
                logic_lines.append(cleaned)
            if len(logic_lines) >= max_logic_steps:
                break

    parts = ["### PRIOR PART SUMMARY"]
    parts.append("Use this only as earlier context. Do not repeat it unless needed for continuity.")

    if purpose and purpose.group(1).strip():
        parts.append("\nPurpose so far:")
        parts.append(purpose.group(1).strip())

    if params and params.group(1).strip():
        parts.append("\nParameter understanding so far:")
        parts.append(params.group(1).strip())

    if logic_lines:
        parts.append("\nKey logic already established:")
        for ln in logic_lines:
            parts.append(f"- {ln}")

    if data and data.group(1).strip():
        parts.append("\nKnown data interactions so far:")
        parts.append(data.group(1).strip())

    return "\n".join(parts).strip()


def sort_key(filename):
    info = parse_part_info(filename)
    if info:
        base_key, part_num = info
        return (base_key, part_num)
    return (filename, 0)


def inject_prior_summary(prompt_text: str, prior_summary: str) -> str:
    if not prior_summary:
        return prompt_text

    insert_block = (
        f"{prior_summary}\n\n"
        "### PART-SPECIFIC INSTRUCTION\n"
        "Use the prior summary only to understand context from earlier chunks. "
        "Do not re-document the earlier chunk in full. Focus on the current SQL chunk while keeping naming and purpose consistent.\n\n"
    )

    marker = "### RAW SQL INPUT"
    if marker in prompt_text:
        return prompt_text.replace(marker, insert_block + marker, 1)

    return insert_block + prompt_text


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



def main():
    print("Starting sql_analysis...")
    print(f"Using model: {MODEL_NAME}")
    print(f"SQL prompts input folder: {INPUT_FOLDER}")
    print(f"SQL analysis output folder: {OUTPUT_FOLDER}")

    try:
        ensure_ollama_running(MODEL_NAME)
    except Exception as e:
        print(f"  ⚠️ Ollama not available: {e}")
        print("  Aborting sql_analysis. Start Ollama manually or adjust the helper.")
        return

    if os.path.exists(OUTPUT_FOLDER):
        print(f"Wiping existing folder: {OUTPUT_FOLDER}")
        try:
            shutil.rmtree(OUTPUT_FOLDER)
        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}.")
            return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    llm = Ollama(
        model=MODEL_NAME,
        #base_url=OLLAMA_BASE_URL,
        temperature=0.1,
        num_ctx=8192,
        num_predict=4096,
        stop=["<|eot_id|>", "### SYSTEM ROLE", "### RAW SQL INPUT"],
    )

    if not os.path.isdir(INPUT_FOLDER):
        print(f"No SQL prompt folder found at '{INPUT_FOLDER}'. Skipping sql_analysis.")
        return

    files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".txt")]
    files.sort(key=sort_key)

    if not files:
        print(f"No SQL prompt files found in '{INPUT_FOLDER}'. Skipping sql_analysis.")
        return

    prior_part_summaries = {}

    for filename in files:
        output_filename = filename.replace(".txt", ".md")
        out_path = os.path.join(OUTPUT_FOLDER, output_filename)

        if os.path.exists(out_path):
            print(f"Skipping {filename} (Done)")
            continue

        print(f"\nProcessing {filename}...")
        with open(os.path.join(INPUT_FOLDER, filename), "r", encoding="utf-8") as f:
            original_prompt = f.read()

        expected_proc_title = build_expected_procedure_title(original_prompt)
        expected_source_file = extract_source_file(original_prompt)
        expected_source_path = extract_source_path(original_prompt)
        part_info = parse_part_info(filename)
        current_prompt = original_prompt

        if part_info:
            base_key, part_num = part_info
            if part_num > 1 and base_key in prior_part_summaries:
                current_prompt = inject_prior_summary(original_prompt, prior_part_summaries[base_key])
                print(f"  ↪ Injected summary from previous part for {base_key}.")

        final_output = ""
        best_minor_output = ""
        best_minor_error_count = 10**9
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
            cleaned = strip_global_context_and_below(cleaned)
            cleaned = standardize_sql_headings(cleaned)
            cleaned = normalize_plain_sql_sections(cleaned)
            cleaned = strip_template_placeholders(cleaned)
            cleaned = normalize_leading_purpose_block(cleaned)
            cleaned = salvage_sql_output(cleaned, expected_proc_title, expected_source_file, expected_source_path)
            cleaned = strip_prompt_leakage(cleaned)
            cleaned = keep_only_through_logic_flow(cleaned)
            cleaned = fix_broken_logic_flow_numbering(cleaned)

            cleaned = replace_header_with_source(
                cleaned,
                expected_proc_title,
                expected_source_file,
                expected_source_path,
            )
            cleaned = replace_parameters_section_with_source(cleaned, original_prompt)
            cleaned = replace_data_interactions_with_source(cleaned, original_prompt)
            cleaned = sanitize_data_interactions_block(cleaned)
            cleaned = remove_orphan_markdown_emphasis(cleaned)
            cleaned = dedupe_data_interactions(cleaned)

            is_valid, errors = validate_output_all(cleaned, original_prompt=original_prompt)

            repaired_output = repair_sql_structure(
                cleaned,
                expected_proc_title,
                expected_source_file,
                expected_source_path,
            )
            repaired_output = strip_prompt_leakage(repaired_output)
            repaired_output = keep_only_through_logic_flow(repaired_output)
            repaired_output = fix_broken_logic_flow_numbering(repaired_output)
            repaired_output = replace_header_with_source(
                repaired_output,
                expected_proc_title,
                expected_source_file,
                expected_source_path,
            )
            repaired_output = replace_parameters_section_with_source(repaired_output, original_prompt)
            repaired_output = replace_data_interactions_with_source(repaired_output, original_prompt)
            repaired_output = sanitize_data_interactions_block(repaired_output)
            repaired_output = remove_orphan_markdown_emphasis(repaired_output)
            repaired_output = dedupe_data_interactions(repaired_output)

            candidate_output = standardize_sql_headings(repaired_output)
            minor_only = is_minor_only(errors)

            if is_valid:
                print("  ✅ PASS")
                final_output = candidate_output
                success = True
                break

            if minor_only and len(errors) < best_minor_error_count:
                best_minor_error_count = len(errors)
                best_minor_output = candidate_output

            if minor_only:
                print(f"  ⚠️ Minor issues detected, retrying before fallback: {errors}")
            else:
                print(f"  ❌ FAIL: {errors}")

            if attempt == MAX_RETRIES:
                if best_minor_output:
                    print(f"  ↪ Retries exhausted. Saving best minor-issue draft ({best_minor_error_count} issue(s)).")
                    final_output = best_minor_output
                    success = True
                else:
                    print("  ! Retries exhausted with major issues only. Will use fallback.")
                break

            current_prompt = build_retry_prompt(cleaned, original_prompt, errors)

        if not success:
            print(f"  ! ABORTING {filename}")
            source_file = extract_source_file(original_prompt)
            source_path = extract_source_path(original_prompt)
            source_params = build_parameters_section_from_source(original_prompt)
            source_data = build_data_interactions_from_source(original_prompt)

            final_output = f"""# Procedure: {expected_proc_title}

**File:** {source_file}
**Path:** {source_path}

### Purpose
Generation failed after {MAX_RETRIES} attempts.

{source_params}

### Logic Flow
Could not reliably generate a compliant summary for this procedure.

{source_data}
"""

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_output)

        if part_info and success:
            base_key, _ = part_info
            prior_part_summaries[base_key] = summarize_output_for_next_part(final_output)

        print(f"  Saved: {out_path}")

    print("\nsql_analysis: DONE")


if __name__ == "__main__":

    main()