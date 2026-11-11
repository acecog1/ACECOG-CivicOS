"""Every object version the engine stores must satisfy its Section 7 / Section 8 schema.

Mismatches the gap register already tracks are listed in KNOWN_GAPS with their gap ID. They
are expected to fail today; when the code is fixed, the entry must be removed (the test
fails if a listed gap no longer occurs, so the register cannot go stale).
"""
import json
import pathlib
import sys
from collections import defaultdict

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "src"), str(ROOT / "tests")]
from acecog import schemas  # noqa: E402
from acecog.engine import Engine  # noqa: E402

# (engine object_type, top-level field) -> gap register ID
KNOWN_GAPS = {
    ("membership_credential", "tier"): "G-021",   # two prototype tiers vs the four of 23.1.1
    ("authority", "monitoring_role"): "G-016",    # granted authorities may leave the flag unset
    ("proposition", "state"): "G-007",            # prototype uses 'Decided'; spec states per 8.3 (CL-063)
}


def registry():
    return Registry().with_resources(
        [(s["$id"], Resource.from_contents(s)) for s in schemas.all_schemas().values()])


def test_schema_set_is_well_formed():
    all_s = schemas.all_schemas()
    for name, s in all_s.items():
        Draft202012Validator.check_schema(s)
    section7 = [s for s in all_s.values() if s.get("x-acecog-section") == "7"]
    assert len(section7) == 38, "one schema per Section 7 row"
    assert {s["x-acecog-phase1"] for s in section7} == {"build", "interface"}
    # every generated file on disk is current
    for name, s in all_s.items():
        path = ROOT / "docs" / "api" / "schemas" / f"{name}.schema.json"
        assert path.exists(), f"{path} missing: run python scripts/gen_openapi.py"
        assert json.loads(path.read_text()) == s, f"{path} is stale: run python scripts/gen_openapi.py"


def test_engine_objects_conform():
    import scenario
    engine = Engine()
    scenario.run_all(engine)
    by_type, reg = schemas.by_engine_type(), registry()
    validators = {t: Draft202012Validator(s, registry=reg) for t, s in by_type.items()}
    unmapped, seen_gaps, unexpected = set(), set(), defaultdict(list)
    for versions in engine.versions.values():
        for v in versions:
            val = validators.get(v["object_type"])
            if val is None:
                unmapped.add(v["object_type"])
                continue
            for err in val.iter_errors(v):
                field = err.absolute_path[0] if err.absolute_path else (err.validator, err.message)
                key = (v["object_type"], field)
                if key in KNOWN_GAPS:
                    seen_gaps.add(key)
                else:
                    unexpected[v["version_id"]].append(f"{list(err.absolute_path)}: {err.message}")
    assert not unmapped, f"engine stores object types with no schema: {sorted(unmapped)}"
    assert not unexpected, json.dumps(unexpected, indent=1)[:3000]
    closed = set(KNOWN_GAPS) - seen_gaps
    assert not closed, f"gaps no longer occur; remove from KNOWN_GAPS and close in the register: {closed}"
