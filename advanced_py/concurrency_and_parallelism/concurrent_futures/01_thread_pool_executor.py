"""01 — ThreadPoolExecutor: pool of threads for I/O-bound work.

submit() hands one callable to the pool and returns a Future. as_completed()
yields futures as they finish, so a fast request is not held up by a slow one.
"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def fetch_url(name):
    time.sleep(0.3)
    return f"{name} -> ok"


with ThreadPoolExecutor(max_workers=4) as pool:
    futures = [pool.submit(fetch_url, f"site-{i}") for i in range(8)]
    for future in as_completed(futures):
        print(future.result())

print("All fetches completed.")
