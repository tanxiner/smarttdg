"""Template-based architecture document generator (pure Python, no LLM).

Reads ``architecture_summary.json`` produced by ``manifest_summarizer.py``
and generates ``CORE_ARCHITECTURE_TEMPLATE.md`` using markdown tables and a
simple ASCII dependency diagram.  No network or model is required, so this
always works as a fallback.
"""

import json
import os
import time

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

ARCH_OUTPUT_DIR = os.path.join(BACKEND_DIR, "analysis_output", "Architecture_Chapters")
SUMMARY_FILE = os.path.join(ARCH_OUTPUT_DIR, "architecture_summary.json")
OUTPUT_FILE = os.path.join(ARCH_OUTPUT_DIR, "CORE_ARCHITECTURE_TEMPLATE.md")


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------

def _md_table(headers: list, rows: list) -> str:
    """Render a markdown table. rows is a list of lists."""
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    header_row = "| " + " | ".join(str(h) for h in headers) + " |"
    body = "\n".join(
        "| " + " | ".join(str(c) for c in row) + " |"
        for row in rows
    )
    return f"{header_row}\n{sep}\n{body}"


def _ascii_dependency_tree(controllers: list) -> str:
    """Build a simple ASCII tree for a handful of top controllers."""
    lines = ["Request", "  └── Route Dispatch"]
    shown = controllers[:8]  # keep diagram compact
    for i, ctrl in enumerate(shown):
        connector = "       ├──" if i < len(shown) - 1 else "       └──"
        deps = ctrl.get("dependencies") or []
        dep_str = ", ".join(deps[:3]) if deps else "(no detected deps)"
        lines.append(f"{connector} {ctrl['class']} [{ctrl.get('base', '')}]")
        lines.append(f"              └── uses: {dep_str}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Document generation
# ---------------------------------------------------------------------------

def generate(summary: dict, output_file: str = OUTPUT_FILE) -> str:
    """Generate the markdown document from a summary dict.  Returns the text."""

    entry_points = summary.get("entry_points") or []
    controllers = summary.get("controllers") or []
    models = summary.get("models") or []
    helpers = summary.get("helpers") or []
    services = summary.get("services") or []
    stats = summary.get("stats") or {}

    lines = [
        "# Core Architecture Overview",
        "",
        f"> Generated: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}  ",
        f"> Method: template (no LLM)  ",
        f"> Components detected: {stats.get('controllers', 0)} controllers, "
        f"{stats.get('models', 0)} models, "
        f"{stats.get('helpers', 0)} helpers, "
        f"{stats.get('services', 0)} services",
        "",
    ]

    # ------------------------------------------------------------------
    # 1. Entry Points
    # ------------------------------------------------------------------
    lines += [
        "## 1. Entry Points",
        "",
    ]
    if entry_points:
        rows = [
            [ep["file"], ep["class"], ep.get("base") or "—"]
            for ep in entry_points
        ]
        lines.append(_md_table(["File", "Class", "Base Type"], rows))
    else:
        lines.append("*No entry points detected.*")
    lines.append("")

    # ------------------------------------------------------------------
    # 2. Controllers
    # ------------------------------------------------------------------
    lines += [
        "## 2. Controllers",
        "",
    ]
    if controllers:
        rows = [
            [
                ctrl["file"],
                ctrl["class"],
                ctrl.get("base") or "—",
                ctrl.get("method_count", 0),
                ", ".join((ctrl.get("dependencies") or [])[:5]) or "—",
            ]
            for ctrl in controllers
        ]
        lines.append(_md_table(
            ["File", "Class", "Base", "Methods", "Key Dependencies"],
            rows,
        ))
    else:
        lines.append("*No controllers detected.*")
    lines.append("")

    # ------------------------------------------------------------------
    # 3. Models
    # ------------------------------------------------------------------
    lines += [
        "## 3. Models",
        "",
    ]
    if models:
        rows = [[m["file"], m["class"]] for m in models]
        lines.append(_md_table(["File", "Class"], rows))
    else:
        lines.append("*No models detected.*")
    lines.append("")

    # ------------------------------------------------------------------
    # 4. Helpers
    # ------------------------------------------------------------------
    lines += [
        "## 4. Helpers",
        "",
    ]
    if helpers:
        rows = [[h["file"], h["class"]] for h in helpers]
        lines.append(_md_table(["File", "Class"], rows))
    else:
        lines.append("*No helpers detected.*")
    lines.append("")

    # ------------------------------------------------------------------
    # 5. Services / Factories
    # ------------------------------------------------------------------
    lines += [
        "## 5. Services / Factories",
        "",
    ]
    if services:
        rows = [[s["file"], s["class"]] for s in services]
        lines.append(_md_table(["File", "Class"], rows))
    else:
        lines.append("*No services detected.*")
    lines.append("")

    # ------------------------------------------------------------------
    # 6. Dependency Flow Diagram
    # ------------------------------------------------------------------
    lines += [
        "## 6. Dependency Flow (top controllers)",
        "",
        "```",
        _ascii_dependency_tree(controllers),
        "```",
        "",
    ]

    text = "\n".join(lines)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"[architecture_analyzer_template] Wrote {output_file}")
    return text


def main(
    summary_file: str = SUMMARY_FILE,
    output_file: str = OUTPUT_FILE,
) -> str:
    with open(summary_file, "r", encoding="utf-8") as f:
        summary = json.load(f)
    return generate(summary, output_file)


if __name__ == "__main__":
    main()
