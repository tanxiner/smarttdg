"""
comment_stripper.py – Pre-processing step that strips comments from collected
source files before the static analyzer runs.

Supported extensions:
  C#/C-style : .cs .js .jsx .aspx .ascx .master .cshtml
  VB.NET     : .vb
  SQL        : .sql
  HTML       : .html .htm

URLs (http://, https://, ftp://) found inside comments are preserved by
emitting a plain-text line that lists only the URLs that were on the
original comment line.

The script reads from ANALYZER_TEMP_DIR (set by app.py), processes every
supported file in-place, and exits gracefully when no files are present.
"""

import os
import re
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[comment_stripper] %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Supported extensions → language key
# ---------------------------------------------------------------------------
EXT_TO_LANG = {
    ".cs":     "cstyle",
    ".js":     "cstyle",
    ".jsx":    "cstyle",
    ".aspx":   "cstyle",
    ".ascx":   "cstyle",
    ".master": "cstyle",
    ".cshtml": "cstyle",
    ".vb":     "vb",
    ".sql":    "sql",
    ".html":   "html",
    ".htm":    "html",
}

# Pattern that matches URLs we want to keep
_URL_RE = re.compile(r'((?:https?|ftp)://\S+)', re.IGNORECASE)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _extract_urls(text: str) -> list:
    """Return all URLs found in *text*."""
    return _URL_RE.findall(text)


def _urls_line(urls: list) -> str:
    """Return a single-line string containing preserved URLs, or '' if none."""
    if not urls:
        return ""
    return " ".join(urls)


# ---------------------------------------------------------------------------
# C-style stripper  (.cs .js .jsx .aspx .ascx .master .cshtml)
# ---------------------------------------------------------------------------

def strip_cstyle(source: str) -> str:
    """
    Strip // single-line and /* ... */ multi-line comments from C-style source.

    • Respects double-quoted string literals (\"…\") – comment markers inside
      strings are ignored.
    • Preserves URLs that appear inside stripped comments.
    • Blank lines left by stripped comments are kept for structural fidelity.
    """
    result: list[str] = []
    i = 0
    n = len(source)

    # Collect current output line so we can decide whether to emit a URL line
    line_buf: list[str] = []

    def flush_line(extra: str = ""):
        """Flush line_buf + optional extra to result, then start a new line."""
        result.append("".join(line_buf) + extra)
        line_buf.clear()

    while i < n:
        ch = source[i]

        # ---- double-quoted string literal --------------------------------
        if ch == '"':
            line_buf.append(ch)
            i += 1
            while i < n:
                c = source[i]
                line_buf.append(c)
                i += 1
                if c == '\\' and i < n:          # escaped char
                    line_buf.append(source[i])
                    i += 1
                elif c == '"':
                    break
            continue

        # ---- single-quoted string literal (char / VB string) -------------
        if ch == "'":
            line_buf.append(ch)
            i += 1
            while i < n:
                c = source[i]
                line_buf.append(c)
                i += 1
                if c == '\\' and i < n:
                    line_buf.append(source[i])
                    i += 1
                elif c == "'":
                    break
            continue

        # ---- // single-line comment --------------------------------------
        if ch == '/' and i + 1 < n and source[i + 1] == '/':
            # Consume to end of line
            j = i + 2
            while j < n and source[j] != '\n':
                j += 1
            comment_text = source[i:j]
            urls = _extract_urls(comment_text)
            url_str = _urls_line(urls)
            # Replace the comment portion on this line; keep any code before it
            if url_str:
                line_buf.append(url_str)
            # Do NOT append a newline yet – the '\n' (or EOF) is handled below
            i = j
            continue

        # ---- /* ... */ multi-line comment --------------------------------
        if ch == '/' and i + 1 < n and source[i + 1] == '*':
            j = i + 2
            comment_chars: list[str] = []
            while j < n:
                if source[j] == '*' and j + 1 < n and source[j + 1] == '/':
                    j += 2
                    break
                comment_chars.append(source[j])
                j += 1
            comment_text = "".join(comment_chars)
            urls = _extract_urls(comment_text)
            # For each newline inside the block comment we must emit a blank line
            # to preserve line numbering / structure.
            inner_lines = comment_text.split('\n')
            for idx, _ in enumerate(inner_lines):
                if idx == 0:
                    # first segment: inject URLs on the same output line
                    if urls and idx == 0:
                        line_buf.append(_urls_line(urls))
                    # emit everything up to and including this logical line end
                    # (we do NOT know yet whether there's a \n – handled by the
                    #  fact that inner_lines are split on \n)
                else:
                    flush_line()
            i = j
            continue

        # ---- newline -----------------------------------------------------
        if ch == '\n':
            flush_line()
            i += 1
            continue

        # ---- ordinary character ------------------------------------------
        line_buf.append(ch)
        i += 1

    # Flush remaining buffer (file not ending in newline)
    if line_buf:
        result.append("".join(line_buf))

    return "\n".join(result)


# ---------------------------------------------------------------------------
# VB.NET stripper  (.vb)
# ---------------------------------------------------------------------------

def strip_vb(source: str) -> str:
    """
    Strip VB.NET single-line comments (everything from ' to end-of-line).
    Respects double-quoted string literals.
    """
    result_lines: list[str] = []

    for raw_line in source.splitlines(keepends=True):
        line = raw_line.rstrip('\n').rstrip('\r')
        out: list[str] = []
        i = 0
        n = len(line)
        in_string = False

        while i < n:
            ch = line[i]

            if in_string:
                out.append(ch)
                i += 1
                if ch == '"':
                    # VB uses "" for escaped quote inside string
                    if i < n and line[i] == '"':
                        out.append(line[i])
                        i += 1
                    else:
                        in_string = False
                continue

            if ch == '"':
                in_string = True
                out.append(ch)
                i += 1
                continue

            if ch == "'":
                # Rest of line is comment
                comment_text = line[i:]
                urls = _extract_urls(comment_text)
                if urls:
                    out.append(_urls_line(urls))
                break  # skip rest of line

            out.append(ch)
            i += 1

        eol = '\n' if raw_line.endswith('\n') else ''
        result_lines.append("".join(out) + eol)

    return "".join(result_lines)


# ---------------------------------------------------------------------------
# SQL stripper  (.sql)
# ---------------------------------------------------------------------------

def strip_sql(source: str) -> str:
    """
    Strip SQL -- single-line and /* */ multi-line comments.
    Respects single-quoted string literals.
    """
    result: list[str] = []
    i = 0
    n = len(source)
    line_buf: list[str] = []

    def flush_line(extra: str = ""):
        result.append("".join(line_buf) + extra)
        line_buf.clear()

    while i < n:
        ch = source[i]

        # ---- single-quoted string literal --------------------------------
        if ch == "'":
            line_buf.append(ch)
            i += 1
            while i < n:
                c = source[i]
                line_buf.append(c)
                i += 1
                if c == "'" and i < n and source[i] == "'":
                    # escaped quote ''
                    line_buf.append(source[i])
                    i += 1
                elif c == "'":
                    break
            continue

        # ---- -- single-line comment -------------------------------------
        if ch == '-' and i + 1 < n and source[i + 1] == '-':
            j = i + 2
            while j < n and source[j] != '\n':
                j += 1
            comment_text = source[i:j]
            urls = _extract_urls(comment_text)
            if urls:
                line_buf.append(_urls_line(urls))
            i = j
            continue

        # ---- /* ... */ multi-line comment --------------------------------
        if ch == '/' and i + 1 < n and source[i + 1] == '*':
            j = i + 2
            comment_chars: list[str] = []
            while j < n:
                if source[j] == '*' and j + 1 < n and source[j + 1] == '/':
                    j += 2
                    break
                comment_chars.append(source[j])
                j += 1
            comment_text = "".join(comment_chars)
            urls = _extract_urls(comment_text)
            inner_lines = comment_text.split('\n')
            for idx, _ in enumerate(inner_lines):
                if idx == 0:
                    if urls:
                        line_buf.append(_urls_line(urls))
                else:
                    flush_line()
            i = j
            continue

        # ---- newline -----------------------------------------------------
        if ch == '\n':
            flush_line()
            i += 1
            continue

        # ---- ordinary character ------------------------------------------
        line_buf.append(ch)
        i += 1

    if line_buf:
        result.append("".join(line_buf))

    return "\n".join(result)


# ---------------------------------------------------------------------------
# HTML stripper  (.html .htm)
# ---------------------------------------------------------------------------

def strip_html(source: str) -> str:
    """
    Strip HTML <!-- ... --> comments.
    Preserves URLs found inside stripped comments.
    """
    result: list[str] = []
    i = 0
    n = len(source)
    line_buf: list[str] = []

    def flush_line(extra: str = ""):
        result.append("".join(line_buf) + extra)
        line_buf.clear()

    while i < n:
        # ---- <!-- comment ------------------------------------------------
        if source[i:i + 4] == '<!--':
            j = i + 4
            comment_chars: list[str] = []
            while j < n:
                if source[j:j + 3] == '-->':
                    j += 3
                    break
                comment_chars.append(source[j])
                j += 1
            comment_text = "".join(comment_chars)
            urls = _extract_urls(comment_text)
            inner_lines = comment_text.split('\n')
            for idx, _ in enumerate(inner_lines):
                if idx == 0:
                    if urls:
                        line_buf.append(_urls_line(urls))
                else:
                    flush_line()
            i = j
            continue

        # ---- newline -----------------------------------------------------
        if source[i] == '\n':
            flush_line()
            i += 1
            continue

        # ---- ordinary character ------------------------------------------
        line_buf.append(source[i])
        i += 1

    if line_buf:
        result.append("".join(line_buf))

    return "\n".join(result)


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------

_STRIPPERS = {
    "cstyle": strip_cstyle,
    "vb":     strip_vb,
    "sql":    strip_sql,
    "html":   strip_html,
}


def strip_comments(source: str, lang: str) -> str:
    """Strip comments from *source* according to *lang*.  Returns cleaned text."""
    fn = _STRIPPERS.get(lang)
    if fn is None:
        raise ValueError(f"Unknown language key: {lang!r}")
    return fn(source)


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------

def _collect_files(root: str) -> list[tuple[str, str]]:
    """Return a list of (filepath, lang) for all supported files under *root*."""
    found = []
    for dirpath, _dirs, filenames in os.walk(root):
        for fname in filenames:
            ext = os.path.splitext(fname)[1].lower()
            lang = EXT_TO_LANG.get(ext)
            if lang:
                found.append((os.path.join(dirpath, fname), lang))
    return found


def process_file(filepath: str, lang: str) -> dict:
    """
    Strip comments from one file in-place.

    Returns a stats dict:
        {"file": ..., "original_lines": int, "stripped_lines": int,
         "urls_preserved": int, "error": str|None}
    """
    stats = {"file": filepath, "original_lines": 0, "stripped_lines": 0,
             "urls_preserved": 0, "error": None}
    try:
        try:
            with open(filepath, "r", encoding="utf-8") as fh:
                content = fh.read()
        except UnicodeDecodeError:
            with open(filepath, "r", encoding="latin-1") as fh:
                content = fh.read()

        original_lines = content.count('\n') + (1 if content else 0)
        stats["original_lines"] = original_lines

        cleaned = strip_comments(content, lang)

        stripped_lines = cleaned.count('\n') + (1 if cleaned else 0)
        stats["stripped_lines"] = stripped_lines
        stats["urls_preserved"] = len(_URL_RE.findall(cleaned))

        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(cleaned)

    except Exception as exc:  # noqa: BLE001
        stats["error"] = str(exc)
        log.error("Failed to process %s: %s", filepath, exc)

    return stats


# ---------------------------------------------------------------------------
# Entry-point
# ---------------------------------------------------------------------------

def main() -> None:
    temp_dir = os.environ.get("ANALYZER_TEMP_DIR", "")
    if not temp_dir or not os.path.isdir(temp_dir):
        log.warning(
            "ANALYZER_TEMP_DIR not set or not a directory (%r). "
            "No files to strip – exiting.",
            temp_dir,
        )
        sys.exit(0)

    files = _collect_files(temp_dir)
    if not files:
        log.info("No supported source files found in %s. Exiting.", temp_dir)
        sys.exit(0)

    total_original = 0
    total_stripped = 0
    total_urls = 0
    errors = 0

    for filepath, lang in files:
        log.info("Processing [%s] %s", lang, filepath)
        stats = process_file(filepath, lang)
        if stats["error"]:
            errors += 1
        else:
            total_original += stats["original_lines"]
            total_stripped += stats["stripped_lines"]
            total_urls += stats["urls_preserved"]

    log.info(
        "Done. Files: %d  |  Lines before: %d  |  Lines after: %d  |  "
        "URLs preserved: %d  |  Errors: %d",
        len(files), total_original, total_stripped, total_urls, errors,
    )


if __name__ == "__main__":
    main()
