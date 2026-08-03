"""01 — The GIL.

The Global Interpreter Lock lets only one thread run Python bytecode at a
time inside a CPython process. This is why threads cannot speed up CPU-bound
Python, and why multiprocessing (separate interpreters) is needed for real
CPU parallelism.
"""
import sys

print(f"Python implementation: {sys.implementation.name}")
try:
    print(f"GIL enabled         : {sys._is_gil_enabled()}")
except AttributeError:
    print("GIL status not exposed on this build (assumed enabled).")

print()
print("Takeaway: for CPU-bound work use multiprocessing, not threading.")
