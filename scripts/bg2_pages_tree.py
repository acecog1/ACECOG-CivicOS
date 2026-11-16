"""Materialize a retained prior deployment only after its protected hash matches."""
import argparse
from pathlib import Path
from scripts.bg2_publication_gate import digest, hold, read_archive


def restore(previous: Path, expected: str, destination: Path) -> dict:
    if digest(previous.read_bytes()) != expected:
        hold('prior deployment archive hash mismatch')
    files = read_archive(previous)
    if not files.get('index.html'):
        hold('prior deployment has no index')
    if destination.exists():
        hold('restore destination must be new')
    for name, data in files.items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    return {name: digest(data) for name, data in files.items()}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--previous', type=Path, required=True)
    p.add_argument('--sha256', required=True)
    p.add_argument('--destination', type=Path, required=True)
    a = p.parse_args()
    restore(a.previous, a.sha256, a.destination)
