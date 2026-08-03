"""02 — Tasks and gather.

asyncio.create_task() schedules a coroutine to run concurrently in the
background and returns a Task. gather() runs several awaitables together and
collects their results in order. asyncio.wait() returns done/pending sets.
"""
import asyncio


async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"data from {name}"


async def main():
    task = asyncio.create_task(fetch("background", 1.0))
    print("Task created; doing other work...")

    results = await asyncio.gather(
        fetch("google", 0.3),
        fetch("github", 0.5),
        fetch("pypi", 0.2),
    )
    print("gather results:", results)

    background_result = await task
    print("background task result:", background_result)

    tasks = [asyncio.create_task(fetch(f"site-{i}", 0.4)) for i in range(3)]
    done, pending = await asyncio.wait(tasks)
    print(f"wait: done={len(done)}, pending={len(pending)}")


if __name__ == "__main__":
    asyncio.run(main())
