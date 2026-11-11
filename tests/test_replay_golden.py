"""A dependency update must not silently change optimization results.

Strict replay (spec 9.1, OPT-REPRO-001, MVP-109) re-solves a past decision and compares result hashes. If an
update to numpy or scipy changes the numbers, every earlier decision would report "not reproduced". This test pins
the reference scenario's result hashes, so such an update fails CI and gets a deliberate decision: either hold the
update, or record a new solver ID and re-baseline these hashes in the same commit, with a change-log note.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "src"), str(ROOT / "tests")]
from acecog.engine import Engine  # noqa: E402


def test_reference_results_unchanged():
    import numpy, scipy, scenario
    golden = json.loads((ROOT / "tests" / "golden" / "replay_hashes.json").read_text())
    engine = Engine()
    scenario.run_all(engine)
    got = {v["version_id"]: v["result_hash"] for vs in engine.versions.values() for v in vs
           if v["object_type"] == "optimization_run" and v.get("result_hash")}
    changed = {k: (h, got.get(k)) for k, h in golden["runs"].items() if got.get(k) != h}
    assert not changed, (
        f"Optimization results changed (numpy {numpy.__version__}, scipy {scipy.__version__}; recorded with "
        f"{golden['recorded_with']}). Past decisions would no longer replay exactly. Hold this update, or re-baseline "
        f"deliberately with a new solver ID. Changed: {changed}")
