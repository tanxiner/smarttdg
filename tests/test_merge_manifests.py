import json
from pathlib import Path

from services.analyzer import merge_manifests as mm


def test_read_manifest_returns_json_for_valid_file(tmp_path):
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps({"files": ["a.txt"]}), encoding="utf-8")

    result = mm.read_manifest(str(path))

    assert result == {"files": ["a.txt"]}


def test_read_manifest_returns_none_for_invalid_json(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("{not valid json", encoding="utf-8")

    result = mm.read_manifest(str(path))

    assert result is None


def test_collect_txt_files_collects_only_txt_files(monkeypatch, tmp_path):
    prompts = tmp_path / "prompts_output"
    page_dir = prompts / "Page_Documentation_Prompts"
    util_dir = prompts / "Utility_Documentation_Prompts"
    sql_dir = prompts / "SQL_Documentation_Prompts"
    api_dir = prompts / "API_Documentation_Prompts"

    for d in (page_dir, util_dir, sql_dir, api_dir):
        d.mkdir(parents=True, exist_ok=True)

    (page_dir / "a.txt").write_text("x", encoding="utf-8")
    (page_dir / "ignore.md").write_text("x", encoding="utf-8")
    (util_dir / "b.txt").write_text("x", encoding="utf-8")
    (sql_dir / "c.txt").write_text("x", encoding="utf-8")
    (api_dir / "d.log").write_text("x", encoding="utf-8")

    monkeypatch.setattr(mm, "PROMPTS_OUTPUT_BASE", str(prompts))
    monkeypatch.setattr(mm, "PAGE_DIR", str(page_dir))
    monkeypatch.setattr(mm, "UTIL_DIR", str(util_dir))
    monkeypatch.setattr(mm, "SQL_DIR", str(sql_dir))
    monkeypatch.setattr(mm, "API_DIR", str(api_dir))

    files = mm.collect_txt_files()

    assert sorted(files) == sorted([
        "Page_Documentation_Prompts/a.txt",
        "Utility_Documentation_Prompts/b.txt",
        "SQL_Documentation_Prompts/c.txt",
    ])


def test_main_merges_all_manifests_without_fallback(monkeypatch, tmp_path):
    prompts = tmp_path / "prompts_output"
    prompts.mkdir(parents=True, exist_ok=True)

    job_id = "job123"

    ai_manifest = {
        "job_id": job_id,
        "expected": 2,
        "files": [
            "Page_Documentation_Prompts/a.txt",
            "Utility_Documentation_Prompts/b.txt",
        ],
    }
    sql_manifest = {
        "job_id": job_id,
        "expected": 1,
        "files": [
            "SQL_Documentation_Prompts/c.txt",
            "Utility_Documentation_Prompts/b.txt",
        ],
    }
    api_manifest = {
        "job_id": job_id,
        "expected": 1,
        "files": [
            "API_Documentation_Prompts/d.txt",
        ],
    }

    (prompts / f"manifest_ai_{job_id}.json").write_text(json.dumps(ai_manifest), encoding="utf-8")
    (prompts / f"manifest_sql_{job_id}.json").write_text(json.dumps(sql_manifest), encoding="utf-8")
    (prompts / f"manifest_api_{job_id}.json").write_text(json.dumps(api_manifest), encoding="utf-8")

    monkeypatch.setenv("ANALYZER_JOB_ID", job_id)
    monkeypatch.setattr(mm, "PROMPTS_OUTPUT_BASE", str(prompts))
    monkeypatch.setattr(mm, "PAGE_DIR", str(prompts / "Page_Documentation_Prompts"))
    monkeypatch.setattr(mm, "UTIL_DIR", str(prompts / "Utility_Documentation_Prompts"))
    monkeypatch.setattr(mm, "SQL_DIR", str(prompts / "SQL_Documentation_Prompts"))
    monkeypatch.setattr(mm, "API_DIR", str(prompts / "API_Documentation_Prompts"))

    mm.main()

    out_path = prompts / f"manifest_{job_id}.json"
    assert out_path.exists()

    merged = json.loads(out_path.read_text(encoding="utf-8"))
    assert merged["job_id"] == job_id
    assert merged["expected"] == 4
    assert merged["files"] == sorted([
        "API_Documentation_Prompts/d.txt",
        "Page_Documentation_Prompts/a.txt",
        "SQL_Documentation_Prompts/c.txt",
        "Utility_Documentation_Prompts/b.txt",
    ])


def test_main_falls_back_to_folder_scan_when_manifest_missing(monkeypatch, tmp_path):
    prompts = tmp_path / "prompts_output"
    page_dir = prompts / "Page_Documentation_Prompts"
    util_dir = prompts / "Utility_Documentation_Prompts"
    sql_dir = prompts / "SQL_Documentation_Prompts"
    api_dir = prompts / "API_Documentation_Prompts"

    for d in (page_dir, util_dir, sql_dir, api_dir):
        d.mkdir(parents=True, exist_ok=True)

    job_id = "job456"

    ai_manifest = {
        "job_id": job_id,
        "expected": 1,
        "files": ["Page_Documentation_Prompts/from_manifest.txt"],
    }
    sql_manifest = {
        "job_id": job_id,
        "expected": 1,
        "files": ["SQL_Documentation_Prompts/from_sql_manifest.txt"],
    }

    (prompts / f"manifest_ai_{job_id}.json").write_text(json.dumps(ai_manifest), encoding="utf-8")
    (prompts / f"manifest_sql_{job_id}.json").write_text(json.dumps(sql_manifest), encoding="utf-8")
    # intentionally do not create manifest_api_job456.json

    (page_dir / "from_scan_page.txt").write_text("x", encoding="utf-8")
    (util_dir / "from_scan_util.txt").write_text("x", encoding="utf-8")
    (sql_dir / "from_sql_manifest.txt").write_text("x", encoding="utf-8")
    (api_dir / "from_scan_api.txt").write_text("x", encoding="utf-8")

    monkeypatch.setenv("ANALYZER_JOB_ID", job_id)
    monkeypatch.setattr(mm, "PROMPTS_OUTPUT_BASE", str(prompts))
    monkeypatch.setattr(mm, "PAGE_DIR", str(page_dir))
    monkeypatch.setattr(mm, "UTIL_DIR", str(util_dir))
    monkeypatch.setattr(mm, "SQL_DIR", str(sql_dir))
    monkeypatch.setattr(mm, "API_DIR", str(api_dir))

    mm.main()

    out_path = prompts / f"manifest_{job_id}.json"
    merged = json.loads(out_path.read_text(encoding="utf-8"))

    assert merged["job_id"] == job_id
    assert merged["expected"] == len(merged["files"])
    assert sorted(merged["files"]) == sorted([
        "API_Documentation_Prompts/from_scan_api.txt",
        "Page_Documentation_Prompts/from_manifest.txt",
        "Page_Documentation_Prompts/from_scan_page.txt",
        "SQL_Documentation_Prompts/from_sql_manifest.txt",
        "Utility_Documentation_Prompts/from_scan_util.txt",
    ])