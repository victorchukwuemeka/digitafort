"""01 — Async basics: async/await and the event loop.

A coroutine only runs when awaited or scheduled. asyncio.run() creates an
event loop, runs the coroutine, and cleans up. During await asyncio.sleep()
the loop switches to other coroutines, which is why the total time is ~1s,
not 3s.
"""
import asyncio
import time


async def worker(name, duration):
    print(f"[{name}] starting")
    await asyncio.sleep(duration)
    print(f"[{name}] finished")
    return name


async def main():
    start = time.perf_counter()
    results = await asyncio.gather(
        worker("A", 1),
        worker("B", 1),
        worker("C", 1),
    )
    elapsed = time.perf_counter() - start
    print(f"Results: {results}")
    print(f"Elapsed: {elapsed:.2f}s (concurrent, not 3s)")


if __name__ == "__main__":
    asyncio.run(main())
