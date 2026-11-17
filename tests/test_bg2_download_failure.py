"""Transport failure cannot use uninitialized bytes or create partial output."""
from urllib.error import URLError
import pytest
from scripts import vendor_browser_pyodide as vendor


def test_all_transport_retries_fail_without_writing(tmp_path, monkeypatch):
    calls = []
    def unavailable(*args, **kwargs):
        calls.append(1)
        raise URLError("synthetic transport failure")
    monkeypatch.setattr(vendor.urllib.request, "urlopen", unavailable)
    monkeypatch.setattr(vendor.time, "sleep", lambda _: None)
    output = tmp_path / "pyodide.mjs"
    with pytest.raises(RuntimeError, match="unavailable after bounded retries"):
        vendor.download("pyodide.mjs", output)
    assert len(calls) == 3
    assert not output.exists()
