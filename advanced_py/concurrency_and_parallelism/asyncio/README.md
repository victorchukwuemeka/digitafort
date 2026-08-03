# Asyncio

`asyncio` provides concurrency **without threads**. A single event loop
runs thousands of "tasks" by suspending them at every `await` and resuming
them when the awaited I/O completes. This is ideal for I/O-bound programs
that use async libraries (`aiohttp`, `asyncpg`, FastAPI, ...).

## Key differences from threading

- No OS threads are spawned; context switches happen at `await` points.
- The code looks sequential: no locks needed for plain async code.
- Nothing blocks: an `async def` must never call a blocking function
  directly, or the whole loop stalls.

## Lessons

- `01_async_basics.py` — `async`/`await`, the event loop, `asyncio.run`
- `02_tasks_and_gather.py` — `create_task`, `gather`, `wait`
- `03_semaphores_timeouts.py` — limits and deadlines
