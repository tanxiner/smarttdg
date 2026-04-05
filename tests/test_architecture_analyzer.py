"""Tests for architecture analysis scripts.

Covers manifest_summarizer, architecture_analyzer_template, and
architecture_analyzer (orchestrator).  The LLM module is tested only for
its prompt-builder and connectivity helpers — no live Ollama call is made.
"""

import json
import os
import pytest

from services.analyzer import manifest_summarizer as ms
from services.analyzer import architecture_analyzer_template as tmpl
from services.analyzer import architecture_analyzer as orch
from services.analyzer import architecture_analyzer_llm as llm_mod


# ---------------------------------------------------------------------------
# manifest_summarizer
# ---------------------------------------------------------------------------

_SAMPLE_DATA = [
    {
        "file": "Global.asax.cs",
        "language": "C#",
        "namespaces": ["MyApp"],
        "imports": ["System.Web.Mvc"],
        "classes": [
            {
                "name": "MvcApplication",
                "modifiers": "public",
                "baseType": None,
                "interfaces": [],
                "Methods": ["protected void Application_Start(): void"],
                "Properties": [],
                "Fields": [],
            }
        ],
        "methods": [],
        "ir": "",
        "api_endpoints": [],
        "sql_usages": [],
    },
    {
        "file": "Controllers/HomeController.cs",
        "language": "C#",
        "namespaces": ["MyApp.Controllers"],
        "imports": ["MyApp.Helpers.MenuHelper", "MyApp.Services.APICommunicate"],
        "classes": [
            {
                "name": "HomeController",
                "modifiers": "public",
                "baseType": "BaseController",
                "interfaces": [],
                "Methods": ["public ActionResult Index(): ActionResult"],
                "Properties": [],
                "Fields": ["private APICommunicate _api"],
            }
        ],
        "methods": [],
        "ir": "",
        "api_endpoints": [],
        "sql_usages": [],
    },
    {
        "file": "Models/Post.cs",
        "language": "C#",
        "namespaces": ["MyApp.Models"],
        "imports": [],
        "classes": [
            {
                "name": "Post",
                "modifiers": "public",
                "baseType": None,
                "interfaces": [],
                "Methods": [],
                "Properties": [],
                "Fields": [],
            }
        ],
        "methods": [],
        "ir": "",
        "api_endpoints": [],
        "sql_usages": [],
    },
    {
        "file": "Helpers/MenuHelper.cs",
        "language": "C#",
        "namespaces": ["MyApp.Helpers"],
        "imports": [],
        "classes": [
            {
                "name": "MenuHelper",
                "modifiers": "public",
                "baseType": None,
                "interfaces": [],
                "Methods": [],
                "Properties": [],
                "Fields": [],
            }
        ],
        "methods": [],
        "ir": "",
        "api_endpoints": [],
        "sql_usages": [],
    },
]


def test_extract_summary_finds_entry_points():
    summary = ms.extract_summary(_SAMPLE_DATA)
    names = [ep["class"] for ep in summary["entry_points"]]
    assert "MvcApplication" in names


def test_extract_summary_finds_controllers():
    summary = ms.extract_summary(_SAMPLE_DATA)
    ctrl_names = [c["class"] for c in summary["controllers"]]
    assert "HomeController" in ctrl_names


def test_extract_summary_finds_models():
    summary = ms.extract_summary(_SAMPLE_DATA)
    model_names = [m["class"] for m in summary["models"]]
    assert "Post" in model_names


def test_extract_summary_finds_helpers():
    summary = ms.extract_summary(_SAMPLE_DATA)
    helper_names = [h["class"] for h in summary["helpers"]]
    assert "MenuHelper" in helper_names


def test_extract_summary_builds_dependency_edges():
    summary = ms.extract_summary(_SAMPLE_DATA)
    edges = summary["dependency_edges"]
    # HomeController uses APICommunicate (from its Fields)
    from_home = [e for e in edges if e["from"] == "HomeController"]
    assert any("APICommunicate" in e["to"] for e in from_home)


def test_extract_summary_stats_counts_correctly():
    summary = ms.extract_summary(_SAMPLE_DATA)
    stats = summary["stats"]
    assert stats["entry_points"] == len(summary["entry_points"])
    assert stats["controllers"] == len(summary["controllers"])
    assert stats["models"] == len(summary["models"])
    assert stats["helpers"] == len(summary["helpers"])


def test_summarize_writes_json_file(tmp_path):
    src = tmp_path / "all_analysis_results.json"
    src.write_text(json.dumps(_SAMPLE_DATA), encoding="utf-8")

    out_dir = tmp_path / "arch_out"
    out_dir.mkdir()
    out_file = out_dir / "architecture_summary.json"

    result = ms.summarize(
        static_analysis_file=str(src),
        output_file=str(out_file),
    )

    assert out_file.exists()
    on_disk = json.loads(out_file.read_text(encoding="utf-8"))
    assert on_disk["stats"]["controllers"] == result["stats"]["controllers"]


def test_extract_summary_empty_input():
    summary = ms.extract_summary([])
    assert summary["entry_points"] == []
    assert summary["controllers"] == []
    assert summary["models"] == []
    assert summary["helpers"] == []
    assert summary["services"] == []
    assert summary["dependency_edges"] == []


def test_extract_summary_skips_non_dict_classes():
    data = [
        {
            "file": "SomeFile.cs",
            "language": "C#",
            "namespaces": [],
            "imports": [],
            "classes": ["not-a-dict"],
            "methods": [],
            "ir": "",
            "api_endpoints": [],
            "sql_usages": [],
        }
    ]
    # Should not raise
    summary = ms.extract_summary(data)
    assert isinstance(summary, dict)


# ---------------------------------------------------------------------------
# architecture_analyzer_template
# ---------------------------------------------------------------------------

def _make_summary(controllers=None, models=None, helpers=None, services=None, entry_points=None):
    controllers = controllers or []
    models = models or []
    helpers = helpers or []
    services = services or []
    entry_points = entry_points or []
    return {
        "entry_points": entry_points,
        "controllers": controllers,
        "models": models,
        "helpers": helpers,
        "services": services,
        "dependency_edges": [],
        "stats": {
            "entry_points": len(entry_points),
            "controllers": len(controllers),
            "models": len(models),
            "helpers": len(helpers),
            "services": len(services),
            "dependency_edges": 0,
        },
    }


def test_template_generates_markdown_file(tmp_path):
    summary = _make_summary(
        entry_points=[{"file": "Global.asax.cs", "class": "MvcApplication", "base": None}],
        controllers=[{
            "file": "Controllers/HomeController.cs",
            "class": "HomeController",
            "base": "BaseController",
            "method_count": 3,
            "dependencies": ["APICommunicate"],
        }],
        models=[{"file": "Models/Post.cs", "class": "Post"}],
    )
    out = tmp_path / "CORE_ARCHITECTURE_TEMPLATE.md"
    text = tmpl.generate(summary, output_file=str(out))

    assert out.exists()
    assert "# Core Architecture Overview" in text
    assert "MvcApplication" in text
    assert "HomeController" in text
    assert "Post" in text


def test_template_contains_all_sections(tmp_path):
    summary = _make_summary()
    out = tmp_path / "arch.md"
    text = tmpl.generate(summary, output_file=str(out))

    for section in ["Entry Points", "Controllers", "Models", "Helpers", "Services", "Dependency Flow"]:
        assert section in text


def test_template_handles_empty_summary(tmp_path):
    summary = _make_summary()
    out = tmp_path / "arch_empty.md"
    text = tmpl.generate(summary, output_file=str(out))

    assert "No controllers detected" in text
    assert "No models detected" in text


def test_template_dependency_tree_limits_to_eight(tmp_path):
    controllers = [
        {"file": f"C{i}.cs", "class": f"Ctrl{i}", "base": "BaseController",
         "method_count": 1, "dependencies": []}
        for i in range(12)
    ]
    summary = _make_summary(controllers=controllers)
    out = tmp_path / "arch_many.md"
    text = tmpl.generate(summary, output_file=str(out))

    # Only 8 should appear in the ASCII tree section
    tree_section = text.split("## 6. Dependency Flow")[1]
    shown = sum(1 for i in range(12) if f"Ctrl{i}" in tree_section)
    assert shown <= 8


# ---------------------------------------------------------------------------
# architecture_analyzer_llm – unit tests (no live Ollama)
# ---------------------------------------------------------------------------

def test_llm_build_prompt_contains_summary_json():
    summary = ms.extract_summary(_SAMPLE_DATA)
    prompt = llm_mod.build_prompt(summary)

    assert "HomeController" in prompt
    assert "architectural data" in prompt.lower() or "json" in prompt.lower()


def test_llm_build_prompt_truncates_large_edge_list():
    summary = ms.extract_summary(_SAMPLE_DATA)
    summary = dict(summary)
    summary["dependency_edges"] = [
        {"from": f"A{i}", "to": f"B{i}", "kind": "uses"} for i in range(200)
    ]
    prompt = llm_mod.build_prompt(summary)
    # Truncation flag must appear in the serialised JSON block
    assert "_dependency_edges_truncated" in prompt


def test_llm_reads_model_from_env(monkeypatch):
    monkeypatch.setenv("ANALYSIS_MODEL", "neural-chat:latest")
    # Re-import to pick up new env value via direct attribute read
    model = os.environ.get("ANALYSIS_MODEL", llm_mod.DEFAULT_MODEL)
    assert model == "neural-chat:latest"


def test_llm_assert_reachable_raises_when_port_closed(monkeypatch):
    monkeypatch.setattr(llm_mod, "OLLAMA_BASE_URL", "http://127.0.0.1:19999")

    with pytest.raises(RuntimeError, match="not reachable"):
        llm_mod._assert_ollama_reachable()


# ---------------------------------------------------------------------------
# architecture_analyzer (orchestrator)
# ---------------------------------------------------------------------------

def test_orchestrator_template_only_when_llm_unavailable(tmp_path, monkeypatch):
    """When Ollama is unreachable the template output should still be produced."""
    src = tmp_path / "all_analysis_results.json"
    src.write_text(json.dumps(_SAMPLE_DATA), encoding="utf-8")

    summary_file = tmp_path / "arch_out" / "architecture_summary.json"
    template_out = tmp_path / "arch_out" / "CORE_ARCHITECTURE_TEMPLATE.md"
    llm_out = tmp_path / "arch_out" / "CORE_ARCHITECTURE_LLM.md"

    # Make LLM always fail
    def _fail(*args, **kwargs):
        raise RuntimeError("Ollama not available")

    monkeypatch.setattr(
        "services.analyzer.architecture_analyzer_llm.generate_with_llm", _fail
    )

    metrics = orch.run(
        static_analysis_file=str(src),
        summary_file=str(summary_file),
        template_output=str(template_out),
        llm_output=str(llm_out),
    )

    assert metrics["template_generated"] is True
    assert metrics["llm_generated"] is False
    assert template_out.exists()
    assert not llm_out.exists()


def test_orchestrator_returns_compression_metrics(tmp_path, monkeypatch):
    src = tmp_path / "all_analysis_results.json"
    src.write_text(json.dumps(_SAMPLE_DATA), encoding="utf-8")

    summary_file = tmp_path / "arch_out" / "architecture_summary.json"
    template_out = tmp_path / "arch_out" / "CORE_ARCHITECTURE_TEMPLATE.md"
    llm_out = tmp_path / "arch_out" / "CORE_ARCHITECTURE_LLM.md"

    def _fail_llm(*args, **kwargs):
        raise RuntimeError("no ollama")

    monkeypatch.setattr(
        "services.analyzer.architecture_analyzer_llm.generate_with_llm",
        _fail_llm,
    )

    metrics = orch.run(
        static_analysis_file=str(src),
        summary_file=str(summary_file),
        template_output=str(template_out),
        llm_output=str(llm_out),
    )

    assert metrics["original_bytes"] > 0
    assert metrics["summary_bytes"] > 0
    assert metrics["compression_ratio"] > 0


def test_orchestrator_records_model_name(tmp_path, monkeypatch):
    monkeypatch.setenv("ANALYSIS_MODEL", "mistral:latest")
    src = tmp_path / "all_analysis_results.json"
    src.write_text(json.dumps(_SAMPLE_DATA), encoding="utf-8")

    summary_file = tmp_path / "arch_out2" / "architecture_summary.json"
    template_out = tmp_path / "arch_out2" / "CORE_ARCHITECTURE_TEMPLATE.md"
    llm_out = tmp_path / "arch_out2" / "CORE_ARCHITECTURE_LLM.md"

    def _fail_llm(*args, **kwargs):
        raise RuntimeError("no ollama")

    monkeypatch.setattr(
        "services.analyzer.architecture_analyzer_llm.generate_with_llm",
        _fail_llm,
    )

    metrics = orch.run(
        static_analysis_file=str(src),
        summary_file=str(summary_file),
        template_output=str(template_out),
        llm_output=str(llm_out),
    )

    assert metrics["llm_model"] == "mistral:latest"


def test_orchestrator_continues_when_summariser_fails(tmp_path, monkeypatch):
    """If summariser raises but a pre-existing summary exists, keep going."""
    out_dir = tmp_path / "arch_out3"
    out_dir.mkdir()
    summary_file = out_dir / "architecture_summary.json"
    template_out = out_dir / "CORE_ARCHITECTURE_TEMPLATE.md"
    llm_out = out_dir / "CORE_ARCHITECTURE_LLM.md"

    # Write a valid pre-existing summary
    summary_data = ms.extract_summary(_SAMPLE_DATA)
    summary_file.write_text(json.dumps(summary_data), encoding="utf-8")

    def _bad_summarize(*a, **kw):
        raise IOError("source file missing")

    def _fail_llm(*args, **kwargs):
        raise RuntimeError("source file missing")

    monkeypatch.setattr(
        "services.analyzer.manifest_summarizer.summarize", _bad_summarize
    )
    monkeypatch.setattr(
        "services.analyzer.architecture_analyzer_llm.generate_with_llm",
        _fail_llm,
    )

    metrics = orch.run(
        static_analysis_file=str(tmp_path / "missing.json"),
        summary_file=str(summary_file),
        template_output=str(template_out),
        llm_output=str(llm_out),
    )

    assert metrics["template_generated"] is True


# ---------------------------------------------------------------------------
# pipeline.json integration
# ---------------------------------------------------------------------------

def test_pipeline_json_contains_architecture_analyzer():
    pipeline_path = os.path.join(
        os.path.dirname(__file__), "..", "flask", "backend", "pipeline.json"
    )
    with open(pipeline_path, "r", encoding="utf-8") as f:
        pipeline = json.load(f)

    step_names = [s["name"] for s in pipeline["steps"]]
    assert "architecture_analyzer" in step_names


def test_pipeline_architecture_analyzer_is_non_blocking():
    pipeline_path = os.path.join(
        os.path.dirname(__file__), "..", "flask", "backend", "pipeline.json"
    )
    with open(pipeline_path, "r", encoding="utf-8") as f:
        pipeline = json.load(f)

    step = next(s for s in pipeline["steps"] if s["name"] == "architecture_analyzer")
    assert step.get("non_blocking") is True


def test_pipeline_architecture_analyzer_in_analysis_phase():
    pipeline_path = os.path.join(
        os.path.dirname(__file__), "..", "flask", "backend", "pipeline.json"
    )
    with open(pipeline_path, "r", encoding="utf-8") as f:
        pipeline = json.load(f)

    step = next(s for s in pipeline["steps"] if s["name"] == "architecture_analyzer")
    assert step["phase"] == "analysis"


def test_pipeline_architecture_analyzer_after_splitters_before_compile():
    pipeline_path = os.path.join(
        os.path.dirname(__file__), "..", "flask", "backend", "pipeline.json"
    )
    with open(pipeline_path, "r", encoding="utf-8") as f:
        pipeline = json.load(f)

    names = [s["name"] for s in pipeline["steps"]]
    arch_idx = names.index("architecture_analyzer")
    compile_idx = names.index("compile")
    merge_idx = names.index("merge_manifests")

    assert merge_idx < arch_idx < compile_idx
