"""LLM-based architecture document generator using Ollama.

Reads the compact ``architecture_summary.json`` produced by
``manifest_summarizer.py`` and sends it to whichever Ollama model the user
has selected via the ``ANALYSIS_MODEL`` environment variable (identical
pattern to ``ai_analysis.py``).

Output: ``CORE_ARCHITECTURE_LLM.md``

Fails gracefully — if Ollama is unavailable the exception propagates so that
the orchestrator (``architecture_analyzer.py``) can fall back to the template
generator.
"""

import json
import os
import socket
import time
from urllib.parse import urlparse

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

ARCH_OUTPUT_DIR = os.path.join(BACKEND_DIR, "analysis_output", "Architecture_Chapters")
SUMMARY_FILE = os.path.join(ARCH_OUTPUT_DIR, "architecture_summary.json")
OUTPUT_FILE = os.path.join(ARCH_OUTPUT_DIR, "CORE_ARCHITECTURE_LLM.md")

# ---------------------------------------------------------------------------
# Model / Ollama config  (same pattern as ai_analysis.py)
# ---------------------------------------------------------------------------
DEFAULT_MODEL = "gemma3:latest"
MODEL_NAME = os.environ.get("ANALYSIS_MODEL", DEFAULT_MODEL)
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434")


# ---------------------------------------------------------------------------
# Connectivity helpers  (same pattern as ai_analysis.py)
# ---------------------------------------------------------------------------

def _is_port_open(host: str, port: int) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.8)
    try:
        s.connect((host, port))
        s.close()
        return True
    except Exception:
        return False


def _assert_ollama_reachable() -> None:
    """Raise RuntimeError if Ollama is not reachable."""
    parsed = urlparse(OLLAMA_BASE_URL)
    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or 11434
    if not _is_port_open(host, port):
        raise RuntimeError(
            f"Ollama server is not reachable at {OLLAMA_BASE_URL}. "
            "Start Ollama and try again, or the pipeline will fall back to "
            "the template-based generator."
        )


# ---------------------------------------------------------------------------
# Prompt builder
# ---------------------------------------------------------------------------

_PROMPT_TEMPLATE = """\
You are a senior software architect writing technical documentation for a \
legacy ASP.NET MVC web application.

Using ONLY the structured data below (no external knowledge), produce a \
Markdown document titled "# Core Architecture Overview" that contains:

1. **Entry Points** – table with columns: File | Class | Purpose
2. **Controllers** – table: File | Class | Base | Key Dependencies | Role Summary
3. **Models** – table: File | Class | Description
4. **Helpers & Services** – combined table: File | Class | Category | Purpose
5. **Dependency Flow** – a short ASCII or Mermaid diagram showing how a \
request flows through the layers
6. **Architecture Summary** – 3-5 sentences describing the overall design \
pattern and key observations

Rules:
- Use only information from the JSON data below.
- Do NOT invent class names, file names, or behaviours.
- Do NOT output code blocks containing C#, VB.NET, or SQL.
- Keep the document concise (aim for under 600 lines).

## Architectural Data (JSON)

```json
{summary_json}
```
"""


def build_prompt(summary: dict) -> str:
    # Truncate dependency edges to keep the prompt manageable
    compact = dict(summary)
    edges = compact.get("dependency_edges") or []
    if len(edges) > 100:
        compact = dict(compact)
        compact["dependency_edges"] = edges[:100]
        compact["_dependency_edges_truncated"] = True
    return _PROMPT_TEMPLATE.format(
        summary_json=json.dumps(compact, indent=2, ensure_ascii=False)
    )


# ---------------------------------------------------------------------------
# LLM invocation
# ---------------------------------------------------------------------------

def generate_with_llm(
    summary: dict,
    model_name: str = MODEL_NAME,
    ollama_base_url: str = OLLAMA_BASE_URL,
    output_file: str = OUTPUT_FILE,
) -> str:
    """Send the summary to Ollama and write the result.  Returns the text."""
    from langchain_community.llms import Ollama  # lazy import — only needed at call time

    _assert_ollama_reachable()

    llm = Ollama(model=model_name, base_url=ollama_base_url)

    prompt = build_prompt(summary)
    print(
        f"[architecture_analyzer_llm] Using model '{model_name}' "
        f"(from ANALYSIS_MODEL env var). Sending prompt …"
    )

    t0 = time.time()
    response = llm.invoke(prompt)
    elapsed = time.time() - t0

    text = (response or "").strip()
    if not text:
        raise ValueError("LLM returned an empty response.")

    # Add generation metadata as a trailing comment
    text += (
        f"\n\n---\n"
        f"*Generated by `architecture_analyzer_llm.py` "
        f"using model `{model_name}` in {elapsed:.1f}s.*\n"
    )

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(
        f"[architecture_analyzer_llm] Wrote {output_file} "
        f"({len(text):,} chars, {elapsed:.1f}s)"
    )
    return text


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(
    summary_file: str = SUMMARY_FILE,
    output_file: str = OUTPUT_FILE,
) -> str:
    with open(summary_file, "r", encoding="utf-8") as f:
        summary = json.load(f)
    return generate_with_llm(summary, output_file=output_file)


if __name__ == "__main__":
    main()
