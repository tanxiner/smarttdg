import json
import pytest

from services.analyzer import analyzer_runner as ar


class FakeProcWindowsSignalOk:
    def __init__(self):
        self.pid = 123
        self.sent = False
        self.terminated = False
        self.killed = False

    def send_signal(self, sig):
        self.sent = True

    def terminate(self):
        self.terminated = True

    def kill(self):
        self.killed = True


class FakeProcWindowsTerminateFallback:
    def __init__(self):
        self.pid = 456
        self.sent = False
        self.terminated = False
        self.killed = False

    def send_signal(self, sig):
        self.sent = True
        raise RuntimeError("CTRL_BREAK failed")

    def terminate(self):
        self.terminated = True

    def kill(self):
        self.killed = True


class FakeProcPosixKillOk:
    def __init__(self):
        self.pid = 789
        self.killed = False

    def kill(self):
        self.killed = True


class FakeProcPosixKillFallback:
    def __init__(self):
        self.pid = 999
        self.killed = False

    def kill(self):
        self.killed = True


def setup_function():
    ar._PROCS.clear()


def test_register_and_unregister_proc():
    proc = FakeProcWindowsSignalOk()

    ar._register_proc("job1", proc)
    assert ar._PROCS["job1"] is proc

    ar._unregister_proc("job1")
    assert "job1" not in ar._PROCS


def test_cancel_analyzer_returns_false_when_missing():
    assert ar.cancel_analyzer("missing-job") is False


def test_cancel_analyzer_windows_uses_send_signal(monkeypatch):
    proc = FakeProcWindowsSignalOk()
    ar._register_proc("job2", proc)

    monkeypatch.setattr(ar.os, "name", "nt")

    result = ar.cancel_analyzer("job2")

    assert result is True
    assert proc.sent is True
    assert proc.terminated is False
    assert "job2" not in ar._PROCS


def test_cancel_analyzer_windows_falls_back_to_terminate(monkeypatch):
    proc = FakeProcWindowsTerminateFallback()
    ar._register_proc("job3", proc)

    monkeypatch.setattr(ar.os, "name", "nt")

    result = ar.cancel_analyzer("job3")

    assert result is True
    assert proc.sent is True
    assert proc.terminated is True
    assert "job3" not in ar._PROCS


def test_cancel_analyzer_posix_uses_killpg(monkeypatch):
    proc = FakeProcPosixKillOk()
    ar._register_proc("job4", proc)

    monkeypatch.setattr(ar.os, "name", "posix")
    monkeypatch.setattr(ar.os, "getpgid", lambda pid: 4242, raising=False)

    called = {}

    def fake_killpg(pgid, sig):
        called["pgid"] = pgid
        called["sig"] = sig

    monkeypatch.setattr(ar.os, "killpg", fake_killpg, raising=False)

    result = ar.cancel_analyzer("job4")

    assert result is True
    assert called["pgid"] == 4242
    assert "job4" not in ar._PROCS
    assert proc.killed is False


def test_cancel_analyzer_posix_falls_back_to_proc_kill(monkeypatch):
    proc = FakeProcPosixKillFallback()
    ar._register_proc("job5", proc)

    monkeypatch.setattr(ar.os, "name", "posix")
    monkeypatch.setattr(ar.os, "getpgid", lambda pid: 1111, raising=False)

    def fake_killpg(pgid, sig):
        raise RuntimeError("killpg failed")

    monkeypatch.setattr(ar.os, "killpg", fake_killpg, raising=False)

    result = ar.cancel_analyzer("job5")

    assert result is True
    assert proc.killed is True
    assert "job5" not in ar._PROCS


def test_clean_and_parse_json_parses_plain_object():
    data = {"status": "ok", "count": 2}
    stdout = json.dumps(data)

    result = ar._clean_and_parse_json(stdout)

    assert result == data


def test_clean_and_parse_json_parses_plain_array():
    data = [{"file": "a.cs"}, {"file": "b.cs"}]
    stdout = json.dumps(data)

    result = ar._clean_and_parse_json(stdout)

    assert result == data


def test_clean_and_parse_json_recovers_json_after_leading_noise():
    stdout = """
Build started...
warning NETSDK1234: something noisy
{"status": "ok", "message": "done"}
"""

    result = ar._clean_and_parse_json(stdout)

    assert result == {"status": "ok", "message": "done"}


def test_clean_and_parse_json_recovers_json_array_after_leading_noise():
    stdout = """
Some startup log
Another line
[{"file": "a.cs"}, {"file": "b.cs"}]
"""

    result = ar._clean_and_parse_json(stdout)

    assert result == [{"file": "a.cs"}, {"file": "b.cs"}]


def test_clean_and_parse_json_filters_interleaved_netsdk_warning():
    stdout = """[
{"file": "a.cs"},
warning NETSDK9999: noisy line
{"file": "b.cs"}
]"""

    result = ar._clean_and_parse_json(stdout)

    assert result == [{"file": "a.cs"}, {"file": "b.cs"}]


def test_clean_and_parse_json_raises_for_empty_output():
    with pytest.raises(json.JSONDecodeError):
        ar._clean_and_parse_json("")


def test_clean_and_parse_json_raises_when_no_json_found():
    with pytest.raises(json.JSONDecodeError):
        ar._clean_and_parse_json("just logs and no json anywhere")