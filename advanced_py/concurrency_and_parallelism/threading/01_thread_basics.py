"""01 — Thread basics: create, start, join.

Concurrency lesson: several threads make progress at once. Each thread runs
the same target function with its own arguments. join() makes the main
thread wait until every worker has finished.
"""
import threading
import time


def worker(name, delay):
    print(f"[{name}] starting")
    for i in range(3):
        time.sleep(delay)
        print(f"[{name}] step {i}")
    print(f"[{name}] done")


threads = []
for name in ("A", "B", "C"):
    t = threading.Thread(target=worker, args=(name, 0.3), name=name)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads have finished.")
