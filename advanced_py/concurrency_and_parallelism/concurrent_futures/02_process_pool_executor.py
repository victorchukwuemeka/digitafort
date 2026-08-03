"""02 — ProcessPoolExecutor: pool of processes for CPU-bound work.

Identical API to ThreadPoolExecutor, but the pool is made of processes, so
CPU-bound tasks actually run in parallel across cores.
"""
from concurrent.futures import ProcessPoolExecutor


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_primes(limit):
    return sum(1 for n in range(limit) if is_prime(n))


if __name__ == "__main__":
    ranges = [50_000, 100_000, 150_000, 200_000]
    with ProcessPoolExecutor() as pool:
        totals = pool.map(sum_primes, ranges)
    print("primes per range:", list(totals))
