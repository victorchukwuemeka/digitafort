"""03 — Benchmark: is the workload CPU-bound or I/O-bound?

Run this to *measure* which tool fits a workload instead of guessing.
We compare serial, threads, and processes on the same fake task.

CPU-bound task : heavy pure-Python math  -> processes win.
I/O-bound task : mostly sleeping/waiting -> threads win (or match).

Change BOUND = "cpu" / "io" to feel the difference.
"""
import threading
import multiprocessing
import time

BOUND = "cpu"
WORK_UNITS = 6


def cpu_task(x):
    total = 0
    for i in range(2_000_000):
        total += (i * x) % 7
    return total


def io_task(x):
    time.sleep(1.0)
    return x


def task(x):
    return cpu_task(x) if BOUND == "cpu" else io_task(x)


def run_serial():
    start = time.perf_counter()
    results = [task(x) for x in range(WORK_UNITS)]
    return time.perf_counter() - start, results


def run_threads():
    start = time.perf_counter()
    threads = [threading.Thread(target=lambda x=x: task(x)) for x in range(WORK_UNITS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.perf_counter() - start


def run_processes():
    start = time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(task, range(WORK_UNITS))
    return time.perf_counter() - start


if __name__ == "__main__":
    t_serial, results = run_serial()
    t_threads = run_threads()
    t_processes = run_processes()

    print(f"Workload type : {BOUND}-bound")
    print(f"Serial        : {t_serial:.2f}s")
    print(f"Threads       : {t_threads:.2f}s")
    print(f"Processes     : {t_processes:.2f}s")
