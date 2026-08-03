"""01 — Process basics: create, start, join.

Each Process runs in its own interpreter and its own memory, so these truly
run in parallel on separate cores. Note the classic guard
`if __name__ == "__main__":` — required because child processes re-import
the module.
"""
import multiprocessing
import os
import time


def worker(name):
    print(f"[{name}] pid={os.getpid()}, parent={os.getppid()}", flush=True)
    time.sleep(1)
    print(f"[{name}] done", flush=True)


if __name__ == "__main__":
    print(f"[main] pid={os.getpid()}", flush=True)
    processes = [multiprocessing.Process(target=worker, args=(f"P{i}",)) for i in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("All processes have finished.")
