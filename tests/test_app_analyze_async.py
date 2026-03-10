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


def test_analyze_async_returns_202_and_job_id(monkeypatch):
    # Make job ID deterministic
    monkeypatch.setattr(app_module.uuid, "uuid4", lambda: "test-job-123")

    # No active job running
    monkeypatch.setattr(app_module, "_find_active_job_id", lambda: None)

    # Replace real background thread with immediate execution
    monkeypatch.setattr(app_module.threading, "Thread", ImmediateThread)

    # Mock heavy analyzer
    def fake_analyze_zip(filepath, job_id=None, model_choice=None):
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

    data = {
        "file": (io.BytesIO(b"fake zip content"), "demo.zip"),
        "model": "gemma3:latest",
    }

    response = client.post(
        "/analyze_async",
        data=data,
        content_type="multipart/form-data",
    )

    assert response.status_code == 202
    payload = response.get_json()
    assert payload["jobId"] == "test-job-123"

    # Since our fake thread runs immediately, the job should already be updated
    status = app_module._get_job("test-job-123")
    assert status["step"] == "done"
    assert status["result"]["status"] == "ok"
    assert status["result"]["message"] == "Mock analysis complete"
    assert status["result"]["zipFilename"] == "demo.zip"
    assert status["model"] == "gemma3:latest"

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

    data = {
        "file": (io.BytesIO(b"not a zip"), "demo.txt"),
    }

    response = client.post(
        "/analyze_async",
        data=data,
        content_type="multipart/form-data",
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Only .zip files are supported"


def test_analyze_async_rejects_when_another_job_is_running(monkeypatch):
    monkeypatch.setattr(app_module, "_find_active_job_id", lambda: "existing-job-1")

    client = app_module.app.test_client()

    data = {
        "file": (io.BytesIO(b"fake zip content"), "demo.zip"),
    }

    response = client.post(
        "/analyze_async",
        data=data,
        content_type="multipart/form-data",
    )

    assert response.status_code == 409
    payload = response.get_json()
    assert payload["error"] == "Another analysis job is still running."
    assert payload["activeJobId"] == "existing-job-1"