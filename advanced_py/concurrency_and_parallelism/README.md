# Concurrency and Parallelism in Python

A standard, hands-on course covering all four ways to do concurrent /
parallel work in Python.

> **Start here:** [CONCURRENCY_COURSE.md](CONCURRENCY_COURSE.md) is the
> single-file course — theory, runnable code snippets, and a conclusion for
> each concept. The folders below are the same content split into runnable
> scripts.

## Why this matters

- **Concurrency** is about *structure*: many tasks making progress
  without waiting for each other.
- **Parallelism** is about *execution*: many tasks actually running on
  different CPU cores at the same time.

Python gives us four tools, and picking the right one depends on whether
the work is CPU-bound or I/O-bound:

| Workload          | Tool                                    | Effect                          |
| ----------------- | --------------------------------------- | ------------------------------- |
| I/O-bound         | `threading`                             | Overlap while waiting on I/O    |
| I/O-bound, async  | `asyncio`                               | Overlap without threads         |
| CPU-bound         | `multiprocessing`                       | True parallelism across cores   |
| I/O + CPU mixed   | `concurrent.futures`                    | Managed pools of either         |

## Course structure

### 1. Fundamentals (`fundamentals/`)
- `01_gil.py` — what the GIL is and why it changes your choices
- `02_race_conditions.py` — the classic bug concurrency introduces
- `03_benchmark_cpu_vs_io.py` — measure a workload to pick a tool

### 2. Threading (`threading/`)
- `01_thread_basics.py` — creating, starting and joining threads
- `02_locks_and_synchronization.py` — `Lock`, `RLock` and safe counters
- `03_queues.py` — producer/consumer with `Queue`
- `04_events_and_barriers.py` — coordinating threads with `Event` / `Barrier`
- `05_daemon_threads.py` — background workers that die with the main thread

### 3. Multiprocessing (`multiprocessing/`)
- `01_process_basics.py` — creating, starting and joining processes
- `02_queues_and_pipes.py` — communicating between processes
- `03_shared_memory.py` — shared `Value`, `Array`, `Manager`
- `04_process_pool.py` — `Pool` for CPU-bound fan-out

### 4. Asyncio (`asyncio/`)
- `01_async_basics.py` — `async`/`await`, event loop, `asyncio.run`
- `02_tasks_and_gather.py` — `create_task`, `gather`, `wait`
- `03_semaphores_timeouts.py` — limits and deadlines

### 5. Concurrent futures (`concurrent_futures/`)
- `01_thread_pool_executor.py` — pool of threads for I/O work
- `02_process_pool_executor.py` — pool of processes for CPU work

### 6. Practice (`practice/`)
- `exercises.py` — problems with hints; try them before peeking.

## How to use the course

```bash
# Run any lesson
python3 threading/01_thread_basics.py
python3 multiprocessing/04_process_pool.py

# Run the benchmark to decide which tool fits a workload
python3 fundamentals/03_benchmark_cpu_vs_io.py
```

Every file runs standalone and prints what it demonstrates.

## Quick decision guide

1. **CPU-bound** (math, parsing big data, image processing)
   -> `multiprocessing` or `ProcessPoolExecutor`.
2. **I/O-bound** with many blocking calls (network, files, sockets)
   -> `threading` or `ThreadPoolExecutor`.
3. **I/O-bound** and already using an async library
   -> `asyncio`.
4. Keep it simple -> `concurrent.futures` hides the boilerplate.
