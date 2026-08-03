# Multiprocessing

Processes are fully separate Python interpreters, each with its own memory
and its own GIL. That means they can run on **multiple CPU cores at the same
time** — true parallelism — which makes `multiprocessing` the right tool for
**CPU-bound** work.

The trade-offs:

- Process creation is expensive (spawns a fresh interpreter).
- No shared memory by default: pass data through `Queue`, `Pipe`, or
  explicit shared objects (`Value`, `Array`, `Manager`).
- Code must be guarded by `if __name__ == "__main__":` on platforms that
  use the `spawn` start method (Windows, and macOS by default).

## Lessons

- `01_process_basics.py` — creating, starting and joining processes
- `02_queues_and_pipes.py` — communicating between processes
- `03_shared_memory.py` — shared `Value`, `Array`, `Manager`
- `04_process_pool.py` — `Pool` for CPU-bound fan-out
