# concurrent.futures

A uniform interface over threads and processes. The same `submit` / `map` /
`Future` API works whether the pool is made of threads or processes, so you
can switch backends with one word.

- `01_thread_pool_executor.py` — pool of threads for I/O work
- `02_process_pool_executor.py` — pool of processes for CPU work

Use it when you don't need asyncio's scale or manual `Process` control: it is
the simplest thing that works for most fan-out workloads.
