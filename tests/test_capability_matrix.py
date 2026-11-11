"""The Public Beta Capability Matrix (Q-14a) is generated from the build and must be current."""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import build_capability_matrix as M  # noqa: E402


def test_matrix_is_current():
    for path, text in M.outputs().items():
        with open(path, encoding="utf-8") as f:
            assert f.read() == text, f"{os.path.basename(path)} is stale. Run: python scripts/build_capability_matrix.py"


def test_every_built_capability_has_a_proposed_exposure():
    assert set(M.EXPOSURE) == set(M.COMMANDS), "add new commands to EXPOSURE in scripts/build_capability_matrix.py"
