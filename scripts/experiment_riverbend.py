"""OFFLINE Riverbend counterfactual PoC; not a public API or a beta release.

Usage:
    python scripts/experiment_riverbend.py --flip cara --flip dev
    python scripts/experiment_riverbend.py --budget 750000 --water 12
    python scripts/experiment_riverbend.py --surprise --seed 42

Runs the ACTUAL CivicOS governance, vote and optimization commands in fresh,
isolated, in-memory engines. No original Riverbend records are changed.
"""
from __future__ import annotations
import argparse
import copy
import json
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tests"))
from acecog.engine import Engine, sha, verify_chain  # noqa: E402
import scenario as riverbend  # noqa: E402

DEFAULT_VOTES = {"ana": "yes", "ben": "yes", "cara": "yes", "dev": "yes", "fay": "no"}
VOTERS = tuple(DEFAULT_VOTES)
RECUSAL = "eli"


def bound_int(value, name, lo, hi):
    if type(value) is not int or not lo <= value <= hi:
        raise ValueError(f"{name} must be an integer from {lo} to {hi}")
    return value


def parameters(budget=900000, water=20, crew=30, appropriation=650000, votes=None):
    v = dict(DEFAULT_VOTES)
    if votes is not None:
        if not isinstance(votes, dict) or set(votes) - set(VOTERS):
            raise ValueError("Unrecognized/recused voter; Eli cannot vote")
        if any(choice not in {"yes", "no", "abstain"} for choice in votes.values()):
            raise ValueError("Unsupported fictional vote choice")
        v.update(votes)
    return {
        "budget": bound_int(budget, "budget", 400000, 1400000),
        "water": bound_int(water, "water", 5, 40),
        "crew": bound_int(crew, "crew", 10, 50),
        "appropriation": bound_int(appropriation, "appropriation", 250000, 850000),
        "votes": v,
    }


def surprise(seed):
    """Reproducible sampling of real INPUTS, not a stochastic solver."""
    bound_int(seed, "seed", 0, 2**32 - 1)
    rng = random.Random(seed)
    v = dict(DEFAULT_VOTES)
    for actor in rng.sample(list(VOTERS), 2):
        v[actor] = "no" if v[actor] == "yes" else "yes"
    return parameters(
        budget=rng.randrange(600000, 1200001, 50000),
        water=rng.randrange(10, 36),
        crew=rng.randrange(18, 46), votes=v,
    )


def portfolio(p):
    m = copy.deepcopy(riverbend.model(budget=p["budget"], water=p["water"]))
    constraints = {c["id"]: c for c in m["constraints"]}
    constraints["crew-capacity"]["limit"] = p["crew"]
    constraints["appropriation-limit"]["limit"] = p["appropriation"]
    return m


def run_case(p):
    p = parameters(**p)
    eng = Engine()
    seq = 0

    def cmd(name, actor, payload, required=True):
        nonlocal seq
        seq += 1
        r = eng.execute(name, {
            "command_id": f"lab-{seq:04d}", "actor_id": actor,
            "client": "desktop", "payload": payload,
        })
        if required and r["outcome"] != "accepted":
            raise RuntimeError(f"CivicOS refused {name}: {r.get('refusal')}")
        return r

    founders = [
        {"actor_id": a, "display_name": label, "roles": roles}
        for a, label, roles in (
            ("ana", "Ana (Facilitator)", ["facilitator"]),
            ("ben", "Ben (City Manager)", ["city_manager"]),
            ("cara", "Cara", ["member"]), ("dev", "Dev", ["member"]),
            ("eli", "Eli", ["member"]), ("fay", "Fay", ["member"]),
        )
    ]
    cb = cmd("civic-bodies.create", "ana", {
        "name": "Riverbend Commons (synthetic lab)",
        "jurisdiction": "Fictional Riverbend", "gml_level": 1,
        "founding_members": founders,
    })["result"]["civic_body"]["id"]
    cmd("governance-processes.adopt", "ana", {
        "civic_body_id": cb, "decision_classes": [{
            "name": "annual_budget", "method": "direct_vote",
            "approval_threshold": 0.5, "quorum": 0.5,
            "min_attestation": "verified",
        }],
    })
    cmd("authorities.grant", "ana", {
        "civic_body_id": cb, "grantee_actor_id": "ben",
        "actions": ["create_baseline", "commit"],
    })
    proposed = cmd("propositions.submit", "cara", {
        "civic_body_id": cb, "decision_class": "annual_budget",
        "title": "Synthetic Riverbend capital improvement Plan A",
        "body": "Hypothetical capital portfolio; advisory with no legal effect.",
        "requested_action": {"type": "adopt_portfolio_model", "model": portfolio(p)},
    })["result"]["proposition"]
    cmd("interest-declarations.record", RECUSAL, {
        "civic_body_id": cb, "proposition_id": proposed["id"],
        "description": "Fictional adjoining-property interest",
    })
    refused = cmd("votes.cast", RECUSAL, {
        "proposition_id": proposed["id"], "choice": "yes",
    }, required=False)
    if refused["outcome"] != "refused" or refused["refusal"]["code"] != "RECUSED":
        raise RuntimeError("Recusal guard did not hold")
    for actor, choice in p["votes"].items():
        cmd("votes.cast", actor, {"proposition_id": proposed["id"], "choice": choice})
    dres = cmd("decisions.close", "ana", {"proposition_id": proposed["id"]})["result"]
    dec = dres["decision"]
    m = dres.get("portfolio_model")
    result = {
        "label": "FICTIONAL / ADVISORY / NO LEGAL EFFECT", "inputs": p,
        "input_hash": sha(p),
        "decision": {"result": dec["result"], "tally": dec["tally"],
                     "legal_status": dec["legal_status"]["value"],
                     "decision_id": dec["id"]},
        "portfolio_adopted": m is not None, "optimization": None,
        "baseline_created": False, "synthetic_commitment_created": False,
        "recusal_refusal": refused["refusal"]["code"],
    }
    if m is not None:
        run = cmd("optimization-runs.request", "cara", {
            "civic_body_id": cb, "model_version_id": m["version_id"],
            "lane": "strict", "seed": 0,
        }, required=False)
        if run["outcome"] == "accepted":
            r = run["result"]["run"]
            result["optimization"] = {
                "run_id": r["id"], "model_version_id": m["version_id"],
                "input_hash": r["input_hash"], "result_hash": r["result_hash"],
                "solution": r["solution"], "solver_config": r["config"],
                "alternative": r.get("alternative"),
            }
            baseline = cmd("baselines.create", "ben", {
                "decision_id": dec["id"], "run_id": r["id"],
            })["result"]["baseline"]
            result["baseline_created"] = True
            cmd("commitments.reserve", "ben", {"baseline_id": baseline["id"]})
            result["synthetic_commitment_created"] = True
            result["replay"] = eng.q_replay(dec["id"])
            if not result["replay"]["reproduced"]:
                raise RuntimeError("Solver replay mismatch")
        elif run["outcome"] == "escalated":
            result["optimization"] = {"feasible": False, "escalation": run["escalation"]}
        else:
            raise RuntimeError(f"Unexpected solver outcome: {run}")
    ok, seq = verify_chain(eng.events)
    if not ok:
        raise RuntimeError(f"Hash-chain violation at record {seq}")
    result["event_count"] = len(eng.events)
    result["chain_head"] = eng.events[-1]["hash"]
    return result


def impact(original, changed):
    """Narrative facts generated only from governed output and input comparisons."""
    a, b = original["decision"], changed["decision"]
    av, bv = a["tally"]["choices"], b["tally"]["choices"]
    lines = [
        "These are fictional advisory simulations; no actual civic action has occurred.",
        f"Plan A: reference {a['result']} ({av.get('yes',0)} yes, {av.get('no',0)} no); "
        f"alternative {b['result']} ({bv.get('yes',0)} yes, {bv.get('no',0)} no).",
    ]
    flipped = [(actor, original["inputs"]["votes"][actor], changed["inputs"]["votes"][actor])
               for actor in VOTERS if original["inputs"]["votes"][actor] != changed["inputs"]["votes"][actor]]
    if flipped:
        lines.append("Changed votes: " + ", ".join(f"{x} {old} to {new}" for x, old, new in flipped) + ".")
    for name in ("budget", "water", "crew", "appropriation"):
        old, new = original["inputs"][name], changed["inputs"][name]
        if old != new:
            lines.append(f"Input '{name}' changed from {old:,} to {new:,}; these are scenario assumptions.")
    if not changed["portfolio_adopted"]:
        lines.append("Plan A was not adopted. No Plan A optimization, baseline or synthetic "
                     "funding commitment occurred in this alternative history.")
    elif changed["optimization"] and changed["optimization"].get("solution"):
        s = changed["optimization"]["solution"]
        lines.append("The actual CivicOS solver allocated " + str(round(sum(s["allocations"].values()),2)) +
                     " simulated dollars; binding constraints: " +
                     (", ".join(s["binding_constraints"]) or "none") + ".")
        old_s = (original["optimization"] or {}).get("solution")
        if old_s:
            count = sum(abs(s["allocations"][k] - old_s["allocations"][k]) > .01
                        for k in s["allocations"])
            lines.append(f"{count} initiative allocations differ from the reference branch.")
    else:
        lines.append("The approved hypothetical model was infeasible; no baseline or commitment followed.")
    lines.append("Not established: real-world welfare, ecological effects, construction costs, "
                 "legal authority, public endorsement or community impacts outside the model.")
    return {
        "method": "deterministic statements derived from engine records, no LLM",
        "statements": lines,
        "evidence": {"reference_head": original["chain_head"],
                     "alternative_head": changed["chain_head"],
                     "reference_inputs": original["input_hash"],
                     "alternative_inputs": changed["input_hash"]},
    }


def compare(p):
    reference, alternative = run_case(parameters()), run_case(p)
    return {
        "reference": reference, "alternative": alternative,
        "impact_narrative": impact(reference, alternative),
        "warning": "LOCAL ENGINE POC, NOT THE BG-1 279-EVENT REFERENCE OR PUBLIC SIMULATOR",
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--budget", type=int, default=900000)
    ap.add_argument("--water", type=int, default=20)
    ap.add_argument("--crew", type=int, default=30)
    ap.add_argument("--appropriation", type=int, default=650000)
    ap.add_argument("--flip", action="append", default=[], choices=list(VOTERS))
    ap.add_argument("--surprise", action="store_true")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    p = surprise(args.seed) if args.surprise else parameters(
        args.budget, args.water, args.crew, args.appropriation,
    )
    if args.flip:
        v = dict(p["votes"])
        for actor in args.flip:
            v[actor] = "no" if v[actor] == "yes" else "yes"
        p["votes"] = v
    print(json.dumps(compare(p), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
