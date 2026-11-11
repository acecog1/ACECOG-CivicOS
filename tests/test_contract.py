"""The Phase 1 contract scenario (Riverbend Commons), in memory and on the durable store."""
import pytest
import scenario
from acecog.engine import Engine


def _run(engine):
    results = list(scenario.run_all(engine))
    assert len(results) >= 48
    failed = [f"{t}: {d} [{x}]" for t, d, ok, x in results if not ok]
    assert not failed, "\n".join(failed)
    return results


def test_contract_scenario_in_memory():
    _run(Engine())


def test_contract_scenario_on_durable_store(tmp_path):
    db = tmp_path / "acecog.sqlite"
    eng = Engine.open(str(db))
    _run(eng)
    n_events, n_objects = len(eng.events), len(eng.obj)
    eng.store.close()
    again = Engine.open(str(db))            # restart: everything comes back, chain verified
    assert len(again.events) == n_events and len(again.obj) == n_objects
