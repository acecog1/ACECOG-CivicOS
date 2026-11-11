"""Regenerate docs/api/openapi.yaml from src/acecog/contract.py."""
import os, runpy, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
runpy.run_module("acecog.gen_openapi", run_name="__main__")
