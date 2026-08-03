"""Practice exercises — model solutions.

Each exercise maps to a course lesson. Uncomment an exercise block to run its
solution.
"""
import asyncio
import queue
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# ---------------------------------------------------------------------------
# 1. Parallel prime counter (CPU-bound)
# ---------------------------------------------------------------------------
import multiprocessing


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(lo, hi):
    return sum(1 for n in range(lo, hi) if is_prime(n))


def exercise_1():
    ranges = [(0, 250_000), (250_000, 500_000), (500_000, 750_000), (750_000, 1_000_000)]
    with multiprocessing.Pool(4) as pool:
        counts = pool.starmap(count_primes, ranges)
    print("exercise 1 — primes below 1M:", sum(counts))


# ---------------------------------------------------------------------------
# 2. Concurrent downloader (I/O-bound)
# ---------------------------------------------------------------------------
def fake_fetch(i):
    time.sleep(0.3)
    return f"item-{i}"


def exercise_2():
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = [pool.submit(fake_fetch, i) for i in range(20)]
        for f in as_completed(futures):
            print("exercise 2 — fetched", f.result())


# ---------------------------------------------------------------------------
# 3. Producer/consumer with queues
# ---------------------------------------------------------------------------
def exercise_3():
    even_sum, odd_sum = [], []
    even_q = queue.Queue()
    odd_q = queue.Queue()

    def producer():
        for i in range(50):
            (even_q if i % 2 == 0 else odd_q).put(i)
        even_q.put(None)
        odd_q.put(None)

    def consumer(q):
        total = 0
        while True:
            item = q.get()
            if item is None:
                q.task_done()
                return total
            total += item
            q.task_done()

    threading.Thread(target=producer).start()
    t1 = threading.Thread(target=lambda: even_sum.append(consumer(even_q)))
    t2 = threading.Thread(target=lambda: odd_sum.append(consumer(odd_q)))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("exercise 3 — even sum:", even_sum, "odd sum:", odd_sum)


# ---------------------------------------------------------------------------
# 4. Async rate limiter
# ---------------------------------------------------------------------------
async def exercise_4():
    sem = asyncio.Semaphore(3)
    start = time.perf_counter()

    async def work(i):
        async with sem:
            await asyncio.sleep(1)

    await asyncio.gather(*(work(i) for i in range(10)))
    elapsed = time.perf_counter() - start
    print(f"exercise 4 — 10 tasks, max 3 concurrent -> {elapsed:.1f}s (expect ~4s)")


# ---------------------------------------------------------------------------
# 5. Locked bank account
# ---------------------------------------------------------------------------
def exercise_5():
    balance = 0
    lock = threading.Lock()

    def deposit():
        nonlocal balance
        for _ in range(100):
            with lock:
                balance += random.uniform(0.5, 2.0)

    threads = [threading.Thread(target=deposit) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"exercise 5 — final balance: {balance:.2f}")


if __name__ == "__main__":
    for fn in (exercise_1, exercise_2, exercise_3, exercise_5):
        fn()
        print()
    asyncio.run(exercise_4())
    print()
