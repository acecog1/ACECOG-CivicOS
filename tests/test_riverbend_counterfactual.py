"""Local PoC acceptance: genuine governance commands, not simulated page text."""
import importlib.util
from pathlib import Path

import pytest

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "experiment_riverbend.py"
spec = importlib.util.spec_from_file_location("experiment_riverbend", MODULE)
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)


def test_reference_adopts_and_reserves_through_real_engine():
    reference = lab.run_case(lab.parameters())
    assert reference["decision"]["result"] == "approved"
    assert reference["decision"]["legal_status"] == "Advisory"
    assert reference["portfolio_adopted"]
    assert reference["optimization"]["solution"]["feasible"] is True
    assert reference["baseline_created"]
    assert reference["synthetic_commitment_created"]
    assert reference["replay"]["reproduced"]
    assert reference["recusal_refusal"] == "RECUSED"
    assert len(reference["chain_head"]) == 64


def test_two_flipped_votes_reject_and_prevent_downstream_funding():
    before = lab.parameters()
    after = lab.parameters(votes={"cara": "no", "dev": "no"})
    result = lab.compare(after)
    original, alternative = result["reference"], result["alternative"]
    assert original["decision"]["result"] == "approved"
    assert alternative["decision"]["result"] == "rejected"
    assert alternative["decision"]["tally"]["choices"]["yes"] == 2
    assert alternative["decision"]["tally"]["choices"]["no"] == 3
    assert alternative["recusal_refusal"] == "RECUSED"
    assert alternative["portfolio_adopted"] is False
    assert alternative["optimization"] is None
    assert not alternative["baseline_created"]
    assert not alternative["synthetic_commitment_created"]
    assert original["chain_head"] == lab.run_case(before)["chain_head"]
    assert original["chain_head"] != alternative["chain_head"]
    assert any("not adopted" in s for s in result["impact_narrative"]["statements"])
    assert not any("real-world benefit" in s for s in result["impact_narrative"]["statements"])


def test_budget_constraint_change_runs_real_solver_not_display_only():
    baseline = lab.run_case(lab.parameters())
    changed = lab.run_case(lab.parameters(budget=600000, crew=20, water=12))
    assert baseline["decision"]["result"] == changed["decision"]["result"] == "approved"
    assert baseline["optimization"]["solution"]["feasible"]
    assert changed["optimization"]["solution"]["feasible"]
    assert changed["replay"]["reproduced"]
    assert changed["optimization"]["input_hash"] != baseline["optimization"]["input_hash"]
    assert changed["optimization"]["result_hash"] != baseline["optimization"]["result_hash"]
    assert changed["optimization"]["solution"]["allocations"] != baseline["optimization"]["solution"]["allocations"]
    assert changed["synthetic_commitment_created"]


def test_randomizer_determinism_and_versioned_replay():
    a, b = lab.surprise(42), lab.surprise(42)
    assert a == b
    first, second = lab.run_case(a), lab.run_case(b)
    assert first["input_hash"] == second["input_hash"]
    assert first["chain_head"] == second["chain_head"]
    if first["portfolio_adopted"]:
        assert first["replay"]["reproduced"]


@pytest.mark.parametrize("overrides", [
    {"budget": 10},
    {"water": -5},
    {"crew": 1000},
    {"appropriation": 0},
    {"votes": {"eli": "yes"}},
    {"votes": {"fake_member": "yes"}},
    {"votes": {"cara": "approve"}},
    {"budget": True},
])
def test_invalid_or_illegal_inputs_fail_closed(overrides):
    with pytest.raises(ValueError):
        lab.parameters(**overrides)


def test_explanation_is_structured_and_disclaims_unsupported_effects():
    output = lab.compare(lab.parameters(budget=600000, votes={"cara": "no", "dev": "no"}))
    assert output["impact_narrative"]["method"].startswith("deterministic statements")
    assert output["impact_narrative"]["evidence"]["reference_head"] == output["reference"]["chain_head"]
    assert output["impact_narrative"]["evidence"]["alternative_head"] == output["alternative"]["chain_head"]
    assert any("Not established" in statement for statement in output["impact_narrative"]["statements"])
    assert "NOT THE BG-1" in output["warning"]
