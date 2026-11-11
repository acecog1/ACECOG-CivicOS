"""Restricted, one-shot BG-2 synthetic simulator process. Never accept civic commands.

Reads one bounded JSON parameter object on stdin, calls only the governed
Riverbend counterfactual adapter, prints one bounded JSON response to stdout.
This is NOT a persistent CivicOS API or real civic service.
"""
from __future__ import annotations

import json
import sys

import experiment_riverbend as lab

MAX_INPUT = 4096
MAX_OUTPUT = 524288


def main() -> None:
    raw = sys.stdin.buffer.read(MAX_INPUT + 1)
    if not raw or len(raw) > MAX_INPUT:
        raise ValueError("Payload outside allowed size")
    p = json.loads(raw)
    if type(p) is not dict or set(p) - {"budget", "water", "crew", "appropriation", "votes"}:
        raise ValueError("Unknown synthetic input")
    params = lab.parameters(**p)
    result = lab.compare(params)
    output = json.dumps(result, ensure_ascii=False, allow_nan=False).encode("utf-8")
    if len(output) > MAX_OUTPUT:
        raise ValueError("Synthetic result over limit")
    sys.stdout.buffer.write(output)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, TypeError, json.JSONDecodeError, RuntimeError):
        # No personal data or command payload in worker diagnostics.
        sys.stderr.write("BG-2 synthetic worker rejected or failed\n")
        sys.exit(2)
