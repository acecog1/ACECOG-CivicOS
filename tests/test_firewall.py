"""The public source tree never contains proprietary edition files, on any branch."""
from pathlib import Path


def test_no_commercial_directory_outside_the_commercial_branch():
    root = Path(__file__).resolve().parents[1]
    assert not (root / 'commercial').exists(), 'Proprietary edition content belongs in its separate private repository'
