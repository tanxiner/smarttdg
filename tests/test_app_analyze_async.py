import io
import app as app_module


class ImmediateThread:
    def __init__(self, target=None, daemon=None):
        self._target = target
        self._alive = False

    def start(self):
        self._alive = True
        if self._target:
            self._target()
        self._alive = False

    def is_alive(self):
        return self._alive


def setup_function():
    app_module.JOB_STATUS.clear()
    app_module.JOB_THREADS.clear()


def test_analyze_async_returns_202_and_updates_job(monkeypatch):
    monkeypatch.setattr(app_module.uuid, "uuid4", lambda: "test-job-123")
    monkeypatch.setattr(app_module, "_find_active_job_id", lambda: None)
    monkeypatch.setattr(app_module.threading, "Thread", ImmediateThread)

    def fake_analyze_zip(filepath, job_id=None, model_choice=None):
        assert job_id == "test-job-123"
        assert model_choice == "gemma3:latest"
        return {
            "status": "ok",
            "message": "Mock analysis complete",
            "computedTotals": {
                "webChapters": 2,
                "sqlChapters": 1,
                "utilityChapters": 1,
                "apiChapters": 0,
            },
        }

    monkeypatch.setattr(app_module, "analyze_zip", fake_analyze_zip)

    client = app_module.app.test_client()

    response = client.post(
        "/analyze_async",
        data={
            "file": (io.BytesIO(b"fake zip content"), "demo.zip"),
            "model": "gemma3:latest",
        },
        content_type="multipart/form-data",
    )

    assert response.status_code == 202
    payload = response.get_json()
    assert payload["jobId"] == "test-job-123"

    status = app_module._get_job("test-job-123")
    assert status["step"] == "done"
    assert status["progress"] == 100
    assert status["zipFilename"] == "demo.zip"
    assert status["model"] == "gemma3:latest"

    result = status["result"]
    assert result["status"] == "ok"
    assert result["message"] == "Mock analysis complete"
    assert result["zipFilename"] == "demo.zip"
    assert result["analysisModel"] == "gemma3:latest"
    assert result["model"] == "gemma3:latest"


def test_analyze_async_rejects_missing_file():
    client = app_module.app.test_client()

    response = client.post(
        "/analyze_async",
        data={},
        content_type="multipart/form-data",
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "No file uploaded"


def test_analyze_async_rejects_non_zip_file():
    client = app_module.app.test_client()

    response = client.post(
        "/analyze_async",
        data={"file": (io.BytesIO(b"not zip"), "demo.txt")},
        content_type="multipart/form-data",
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Only .zip files are supported"


def test_analyze_async_rejects_when_another_job_is_running(monkeypatch):
    monkeypatch.setattr(app_module, "_find_active_job_id", lambda: "existing-job-1")

    client = app_module.app.test_client()

    response = client.post(
        "/analyze_async",
        data={"file": (io.BytesIO(b"fake zip content"), "demo.zip")},
        content_type="multipart/form-data",
    )

    assert response.status_code == 409
    payload = response.get_json()
    assert payload["error"] == "Another analysis job is still running."
    assert payload["activeJobId"] == "existing-job-1"


def test_status_route_returns_404_for_unknown_job():
    client = app_module.app.test_client()

    response = client.get("/status/not-found-job")

    assert response.status_code == 404
    assert response.get_json()["error"] == "job not found"