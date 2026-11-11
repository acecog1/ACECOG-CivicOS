"""Durability, atomicity, and tamper evidence of the local store (spec 8.1, 11.5, ASR-04)."""
import sqlite3
import pytest
from acecog.engine import Engine, sha

N = [0]


def cmd(eng, name, actor, payload, cid=None):
    N[0] += 1
    return eng.execute(name, {"command_id": cid or f"t-{N[0]}", "actor_id": actor, "client": "desktop", "payload": payload})


def setup_body(eng):
    r = cmd(eng, "civic-bodies.create", "ana", {"name": "Test Commons", "founding_members": [
        {"actor_id": "ana", "display_name": "Ana"}, {"actor_id": "ben", "display_name": "Ben"}]})
    cb = r["result"]["civic_body"]["id"]
    cmd(eng, "governance-processes.adopt", "ana", {"civic_body_id": cb, "decision_classes": [
        {"name": "budget", "method": "direct_vote", "approval_threshold": 0.5, "min_attestation": "verified"}]})
    return cb


def test_state_survives_restart(tmp_path):
    db = str(tmp_path / "a.sqlite")
    eng = Engine.open(db)
    cb = setup_body(eng)
    r = cmd(eng, "propositions.submit", "ben", {"civic_body_id": cb, "decision_class": "budget", "title": "T", "body": "B",
                                               "requested_action": {"type": "advisory"}}, cid="keep-me")
    snapshot = (len(eng.events), sorted(eng.obj), eng.events[-1]["hash"])
    eng.store.close()
    eng2 = Engine.open(db)
    assert (len(eng2.events), sorted(eng2.obj), eng2.events[-1]["hash"]) == snapshot
    again = cmd(eng2, "propositions.submit", "ben", {"civic_body_id": cb, "decision_class": "budget", "title": "T", "body": "B",
                                                     "requested_action": {"type": "advisory"}}, cid="keep-me")   # a client retry
    assert again["transaction_id"] == r["transaction_id"], "idempotency survives restart"
    assert len(eng2.events) == snapshot[0]


def test_refused_command_changes_nothing_but_is_recorded(tmp_path):
    db = str(tmp_path / "b.sqlite")
    eng = Engine.open(db)
    cb = setup_body(eng)
    before = {k: len(v) for k, v in eng.versions.items()}
    r = cmd(eng, "governance-processes.adopt", "ana", {"civic_body_id": cb, "decision_classes": [
        {"name": "budget", "method": "direct_vote", "approval_threshold": 0.5, "min_attestation": "verified", "participation_fee": 3}]})
    assert r["outcome"] == "refused" and r["refusal"]["invariant_id"] == "TRU-ACCESS-001"
    assert {k: len(v) for k, v in eng.versions.items()} == before
    assert eng.events[-1]["type"] == "command.refused"
    eng.store.close()
    eng2 = Engine.open(db)
    assert {k: len(v) for k, v in eng2.versions.items()} == before
    assert eng2.events[-1]["type"] == "command.refused"


def test_founding_with_unknown_creator_leaves_no_partial_state():
    eng = Engine()
    r = cmd(eng, "civic-bodies.create", "mallory", {"name": "X", "founding_members": [{"actor_id": "ana", "display_name": "Ana"}]})
    assert r["outcome"] == "refused"
    assert eng.obj == {} and eng.actors == {}, "credentials and actors from the refused command were rolled back"


def test_event_log_and_versions_are_append_only(tmp_path):
    db = str(tmp_path / "c.sqlite")
    eng = Engine.open(db)
    setup_body(eng)
    con = sqlite3.connect(db)
    for sql in ("UPDATE events SET json='{}' WHERE seq=1", "DELETE FROM events WHERE seq=1",
                "UPDATE versions SET json='{}'", "DELETE FROM versions"):
        with pytest.raises(sqlite3.DatabaseError):
            con.execute(sql)


def test_tampered_log_refuses_to_start(tmp_path):
    db = str(tmp_path / "d.sqlite")
    eng = Engine.open(db)
    setup_body(eng)
    eng.store.close()
    con = sqlite3.connect(db)
    con.execute("DROP TRIGGER events_no_update")       # an attacker with file access
    con.execute("UPDATE events SET json=replace(json, 'Test Commons', 'Evil Commons') WHERE seq=1")
    con.execute("UPDATE events SET json=replace(json, '\"type\":\"civic_body.versioned\"', '\"type\":\"x\"') WHERE seq=1")
    con.commit(); con.close()
    with pytest.raises(RuntimeError, match="hash chain broken"):
        Engine.open(db)


def test_failed_write_rolls_memory_back_to_the_durable_record(tmp_path, monkeypatch):
    db = str(tmp_path / "e.sqlite")
    eng = Engine.open(db)
    cb = setup_body(eng)
    n_events, objs = len(eng.events), sorted(eng.obj)

    def boom(*a, **k):
        raise sqlite3.OperationalError("disk full")
    monkeypatch.setattr(eng.store, "commit", boom)
    with pytest.raises(sqlite3.OperationalError):
        cmd(eng, "propositions.submit", "ben", {"civic_body_id": cb, "decision_class": "budget", "title": "T", "body": "B",
                                               "requested_action": {"type": "advisory"}})
    assert len(eng.events) == n_events and sorted(eng.obj) == objs
