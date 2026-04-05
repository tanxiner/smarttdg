"""Architecture analysis orchestrator.

Pipeline:
  1. manifest_summarizer  – compress static analysis JSON to compact summary
  2. architecture_analyzer_llm – generate CORE_ARCHITECTURE_LLM.md via Ollama
     (uses model from ANALYSIS_MODEL env var, falls back gracefully)
  3. architecture_analyzer_template – generate CORE_ARCHITECTURE_TEMPLATE.md
     (pure Python, always succeeds)

Both outputs are produced on every run so that a reader can compare them.
This step is **non-blocking**: errors are logged and the pipeline continues.
"""

import json
import os
import time

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

STATIC_ANALYSIS_FILE = os.path.join(
    BACKEND_DIR, "static_analysis_output", "all_analysis_results.json"
)
ARCH_OUTPUT_DIR = os.path.join(BACKEND_DIR, "analysis_output", "Architecture_Chapters")
SUMMARY_FILE = os.path.join(ARCH_OUTPUT_DIR, "architecture_summary.json")
TEMPLATE_OUTPUT = os.path.join(ARCH_OUTPUT_DIR, "CORE_ARCHITECTURE_TEMPLATE.md")
LLM_OUTPUT = os.path.join(ARCH_OUTPUT_DIR, "CORE_ARCHITECTURE_LLM.md")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _import_summarizer():
    from services.analyzer import manifest_summarizer
    return manifest_summarizer


def _import_template():
    from services.analyzer import architecture_analyzer_template
    return architecture_analyzer_template


def _import_llm():
    from services.analyzer import architecture_analyzer_llm
    return architecture_analyzer_llm


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def run(
    static_analysis_file: str = STATIC_ANALYSIS_FILE,
    summary_file: str = SUMMARY_FILE,
    template_output: str = TEMPLATE_OUTPUT,
    llm_output: str = LLM_OUTPUT,
) -> dict:
    """Run the full architecture analysis pipeline.

    Returns a metrics dict with keys:
        original_bytes, summary_bytes, compression_ratio,
        template_generated, llm_generated, llm_model, elapsed_seconds
    """
    metrics: dict = {
        "original_bytes": 0,
        "summary_bytes": 0,
        "compression_ratio": 0.0,
        "template_generated": False,
        "llm_generated": False,
        "llm_model": os.environ.get("ANALYSIS_MODEL", "gemma3:latest"),
        "elapsed_seconds": 0.0,
    }

    t_start = time.time()

    # ------------------------------------------------------------------
    # Step 1: Summarise
    # ------------------------------------------------------------------
    print("[architecture_analyzer] Step 1/3 — manifest summariser …")
    try:
        summarizer = _import_summarizer()
        summary = summarizer.summarize(
            static_analysis_file=static_analysis_file,
            output_file=summary_file,
        )
        metrics["original_bytes"] = os.path.getsize(static_analysis_file)
        metrics["summary_bytes"] = os.path.getsize(summary_file)
        metrics["compression_ratio"] = round(
            metrics["original_bytes"] / max(metrics["summary_bytes"], 1), 1
        )
    except Exception as exc:
        print(f"[architecture_analyzer] WARNING: summariser failed: {exc}")
        # Try to load an existing summary if available
        if os.path.isfile(summary_file):
            with open(summary_file, "r", encoding="utf-8") as f:
                summary = json.load(f)
        else:
            print("[architecture_analyzer] No existing summary — skipping LLM and template steps.")
            metrics["elapsed_seconds"] = round(time.time() - t_start, 2)
            return metrics

    # ------------------------------------------------------------------
    # Step 2: LLM generation
    # ------------------------------------------------------------------
    print("[architecture_analyzer] Step 2/3 — LLM generation …")
    try:
        llm_mod = _import_llm()
        llm_mod.generate_with_llm(
            summary=summary,
            model_name=os.environ.get("ANALYSIS_MODEL", llm_mod.DEFAULT_MODEL),
            ollama_base_url=os.environ.get("OLLAMA_BASE_URL", llm_mod.OLLAMA_BASE_URL),
            output_file=llm_output,
        )
        metrics["llm_generated"] = True
    except Exception as exc:
        print(
            f"[architecture_analyzer] LLM generation unavailable ({exc}). "
            "Falling back to template generator."
        )

    # ------------------------------------------------------------------
    # Step 3: Template generation (always runs)
    # ------------------------------------------------------------------
    print("[architecture_analyzer] Step 3/3 — template generation …")
    try:
        tmpl_mod = _import_template()
        tmpl_mod.generate(summary=summary, output_file=template_output)
        metrics["template_generated"] = True
    except Exception as exc:
        print(f"[architecture_analyzer] WARNING: template generation failed: {exc}")

    metrics["elapsed_seconds"] = round(time.time() - t_start, 2)

    # ------------------------------------------------------------------
    # Summary log
    # ------------------------------------------------------------------
    print(
        f"[architecture_analyzer] Done in {metrics['elapsed_seconds']}s — "
        f"compression {metrics['compression_ratio']}x, "
        f"template={'✓' if metrics['template_generated'] else '✗'}, "
        f"llm={'✓' if metrics['llm_generated'] else '✗'} "
        f"(model={metrics['llm_model']})"
    )
    return metrics


def main():
    run()


if __name__ == "__main__":
    main()
