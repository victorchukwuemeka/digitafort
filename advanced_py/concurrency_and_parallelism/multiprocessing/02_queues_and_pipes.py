"""02 — Queues and pipes between processes.

Processes do not share memory, so results come back through Queue or Pipe.
The parent puts work in and children send results back. Each child returns
the square of a number.
"""
import multiprocessing


def worker(q, n):
    q.put((n, n * n))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    q = multiprocessing.Queue()
    processes = [multiprocessing.Process(target=worker, args=(q, n)) for n in numbers]

    for p in processes:
        p.start()

    results = [q.get() for _ in numbers]

    for p in processes:
        p.join()

    results.sort()
    for n, sq in results:
        print(f"square({n}) = {sq}")
