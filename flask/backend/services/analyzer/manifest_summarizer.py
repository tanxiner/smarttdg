"""Compress the static analysis JSON into a compact architectural summary.

Reads ``all_analysis_results.json`` (which can be tens of MB) and writes a
much smaller ``architecture_summary.json`` containing only the signals needed
to produce a high-level architecture document:

* Entry points (Global.asax, Startup, Program, RouteConfig, …)
* Controllers with their base class, method count, and detected dependencies
* Models (classes inside a ``Models/`` folder)
* Helpers and services
* Cross-component dependency edges
"""

import json
import os

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))       # services/analyzer
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))  # flask/backend

STATIC_ANALYSIS_FILE = os.path.join(
    BACKEND_DIR, "static_analysis_output", "all_analysis_results.json"
)
OUTPUT_DIR = os.path.join(BACKEND_DIR, "analysis_output", "Architecture_Chapters")
SUMMARY_FILE = os.path.join(OUTPUT_DIR, "architecture_summary.json")

# ---------------------------------------------------------------------------
# Classification helpers
# ---------------------------------------------------------------------------

_ENTRY_POINT_NAMES = {
    "global", "startup", "program", "owinmvcapp", "mvcapplication",
    "routeconfig", "bundleconfig", "filterconfig",
}

_CONTROLLER_KEYWORDS = ("controller",)
_MODEL_PATH_KEYWORDS = ("/models/", "\\models\\", "/model/", "\\model\\", "models/", "model/")
_HELPER_PATH_KEYWORDS = ("/helpers/", "\\helpers\\", "/helper/", "\\helper\\", "helpers/", "helper/")
_SERVICE_PATH_KEYWORDS = (
    "/services/", "\\services\\", "/service/", "\\service\\",
    "/factories/", "\\factories\\",
    "services/", "service/", "factories/",
)


def _normalise_path(path: str) -> str:
    return (path or "").replace("\\", "/").lower()


def _is_entry_point(file_name: str, class_name: str) -> bool:
    base = os.path.splitext(file_name)[0].lower().replace(".", "")
    return base in _ENTRY_POINT_NAMES or class_name.lower() in _ENTRY_POINT_NAMES


def _is_controller(base_type: str) -> bool:
    return any(kw in (base_type or "").lower() for kw in _CONTROLLER_KEYWORDS)


def _classify_by_path(norm_path: str) -> str:
    """Return 'model' | 'helper' | 'service' | '' based on folder name."""
    if any(kw in norm_path for kw in _MODEL_PATH_KEYWORDS):
        return "model"
    if any(kw in norm_path for kw in _HELPER_PATH_KEYWORDS):
        return "helper"
    if any(kw in norm_path for kw in _SERVICE_PATH_KEYWORDS):
        return "service"
    return ""


# ---------------------------------------------------------------------------
# Core extraction
# ---------------------------------------------------------------------------

def extract_summary(data: list) -> dict:
    """Return a compact summary dict from the full static-analysis list."""
    entry_points = []
    controllers = []
    models = []
    helpers = []
    services = []
    dependency_edges = []

    for item in data:
        file_name = item.get("file", "")
        norm_path = _normalise_path(file_name)
        item_classes = item.get("classes") or []

        for cls in item_classes:
            if not isinstance(cls, dict):
                continue

            class_name = cls.get("name") or ""
            base_type = cls.get("baseType") or ""
            interfaces = cls.get("interfaces") or []
            methods = cls.get("Methods") or []
            method_count = len(methods)

            # --- entry points ---
            if _is_entry_point(file_name, class_name):
                entry_points.append({
                    "file": file_name,
                    "class": class_name,
                    "base": base_type or None,
                })
                continue

            # --- controllers ---
            if _is_controller(base_type):
                # Collect dependency names from imports / usages
                deps = _extract_deps(item, cls)
                controllers.append({
                    "file": file_name,
                    "class": class_name,
                    "base": base_type,
                    "interfaces": interfaces,
                    "method_count": method_count,
                    "dependencies": deps,
                })
                for dep in deps:
                    dependency_edges.append({
                        "from": class_name,
                        "to": dep,
                        "kind": "uses",
                    })
                continue

            # --- classify by folder ---
            kind = _classify_by_path(norm_path)
            if kind == "model":
                models.append({
                    "file": file_name,
                    "class": class_name,
                    "kind": kind,
                })
            elif kind == "helper":
                helpers.append({
                    "file": file_name,
                    "class": class_name,
                })
            elif kind == "service":
                services.append({
                    "file": file_name,
                    "class": class_name,
                })

    return {
        "entry_points": entry_points,
        "controllers": controllers,
        "models": models,
        "helpers": helpers,
        "services": services,
        "dependency_edges": dependency_edges,
        "stats": {
            "entry_points": len(entry_points),
            "controllers": len(controllers),
            "models": len(models),
            "helpers": len(helpers),
            "services": len(services),
            "dependency_edges": len(dependency_edges),
        },
    }


def _extract_deps(item: dict, cls: dict) -> list:
    """Heuristically extract dependency class names for a controller."""
    deps = set()

    # From top-level imports
    for imp in item.get("imports") or []:
        if isinstance(imp, str):
            # Take the last segment only
            segment = imp.split(".")[-1]
            if segment and not segment[0].islower():
                deps.add(segment)

    # From field types mentioned in class Properties / Fields
    for field in (cls.get("Fields") or []) + (cls.get("Properties") or []):
        if isinstance(field, str):
            # e.g. "private APICommunicate _api" → take the type token
            parts = field.split()
            if len(parts) >= 2:
                candidate = parts[1] if parts[0] in ("private", "public", "protected", "readonly") else parts[0]
                if candidate and candidate[0].isupper():
                    deps.add(candidate)
        elif isinstance(field, dict):
            t = field.get("type") or field.get("Type") or ""
            if t and t[0].isupper():
                deps.add(t.split("<")[0])  # strip generics

    # Remove the class itself and trivial base types
    deps.discard(cls.get("name") or "")
    for trivial in ("Controller", "BaseController", "Object", "string", "int"):
        deps.discard(trivial)

    return sorted(deps)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def summarize(static_analysis_file: str = STATIC_ANALYSIS_FILE,
              output_file: str = SUMMARY_FILE) -> dict:
    """Load the static analysis file, extract summary, write JSON, and return it."""
    with open(static_analysis_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    summary = extract_summary(data)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    original_size = os.path.getsize(static_analysis_file)
    summary_size = os.path.getsize(output_file)
    ratio = original_size / max(summary_size, 1)
    print(
        f"[manifest_summarizer] {original_size:,} bytes → {summary_size:,} bytes "
        f"(compression ratio {ratio:.1f}x)"
    )
    return summary


def main():
    summarize()


if __name__ == "__main__":
    main()
