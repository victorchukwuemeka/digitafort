"""04 — Process pool.

A Pool manages a fixed set of worker processes and fans work out to them.
map() blocks and returns results in order; apply_async() is non-blocking and
returns AsyncResult objects you can get() later. This is the idiomatic way to
parallelize CPU-bound work.
"""
import multiprocessing


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(start, end):
    return sum(1 for n in range(start, end) if is_prime(n))


if __name__ == "__main__":
    ranges = [(0, 100_000), (100_000, 200_000), (200_000, 300_000), (300_000, 400_000)]

    with multiprocessing.Pool(4) as pool:
        results = pool.starmap(count_primes, ranges)

    print("Primes per range:", results)
    print("Total primes    :", sum(results))
