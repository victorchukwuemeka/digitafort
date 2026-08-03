"""03 — Semaphores and timeouts.

Semaphore caps how many coroutines may run at once (e.g. a polite limit of
3 concurrent requests). asyncio.timeout() / asyncio.wait_for() set deadlines
so a slow operation cannot hang the program forever.
"""
import asyncio

SEMAPHORE = asyncio.Semaphore(3)


async def limited_request(name):
    async with SEMAPHORE:
        print(f"[{name}] acquired semaphore")
        await asyncio.sleep(1)
        print(f"[{name}] released semaphore")
    return name


async def slow_operation():
    await asyncio.sleep(10)
    return "never seen"


async def main():
    print("--- semaphore: max 3 concurrent ---")
    await asyncio.gather(*(limited_request(f"req-{i}") for i in range(6)))

    print("--- timeout ---")
    try:
        async with asyncio.timeout(1.5):
            await slow_operation()
    except TimeoutError:
        print("Timed out waiting for slow_operation()")


if __name__ == "__main__":
    asyncio.run(main())
