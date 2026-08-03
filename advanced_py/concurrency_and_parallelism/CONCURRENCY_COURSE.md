# Concurrency and Parallelism in Python — Complete Course

> A single-file course: theory, runnable code snippets, and a conclusion for
> every concept. Everything below is standard-library only — no installs needed.

---

## Table of contents

1. [Concurrency vs Parallelism — the big picture](#1-concurrency-vs-parallelism)
2. [The GIL — why Python needs four tools](#2-the-gil)
3. [Choosing a tool](#3-choosing-a-tool)
4. [Threading](#4-threading)
   - [Thread basics](#41-thread-basics)
   - [Locks and race conditions](#42-locks-and-race-conditions)
   - [Thread-safe queues](#43-thread-safe-queues)
   - [Events and barriers](#44-events-and-barriers)
5. [Multiprocessing](#5-multiprocessing)
   - [Process basics](#51-process-basics)
   - [Process communication](#52-process-communication)
   - [Shared memory](#53-shared-memory)
   - [Process pools](#54-process-pools)
6. [Asyncio](#6-asyncio)
   - [async/await basics](#61-asyncawait-basics)
   - [Tasks, gather, wait](#62-tasks-gather-wait)
   - [Semaphores and timeouts](#63-semaphores-and-timeouts)
7. [concurrent.futures](#7-concurrentfutures)
   - [ThreadPoolExecutor](#71-threadpoolexecutor)
   - [ProcessPoolExecutor](#72-processpoolexecutor)
8. [Final conclusions](#8-final-conclusions)

---

## 1. Concurrency vs Parallelism

These two words are often mixed up, and the difference decides which Python
tool you use.

- **Concurrency** is about *structure*: a program where many tasks can make
  progress without waiting for each other. It is a *design property*. With
  concurrency, one CPU core can still juggle many tasks — it just switches
  between them.
- **Parallelism** is about *execution*: many tasks genuinely run at the same
  instant on **different CPU cores**. It is a *hardware property*.

Analogy: concurrency is one chef rapidly alternating between cooking three
dishes; parallelism is three chefs each cooking one dish. A single-cook
kitchen can still be "concurrent" (all dishes eventually get cooked), but it
can never be "parallel".

```python
import threading
import time


def make_dish(name, minutes):
    print(f"[{name}] cooking for {minutes} min")
    time.sleep(minutes)
    print(f"[{name}] done")


# CONCURRENCY: one thread per dish, all started before any joins.
threads = [threading.Thread(target=make_dish, args=(f"dish-{i}", 1)) for i in range(3)]
for t in threads:
    t.start()          # all three dishes begin "at the same time"
for t in threads:
    t.join()           # wait for all of them
print("Kitchen finished. Total wall time ~1 min, not 3.")
```

**Conclusion:** the code above is *concurrent*: three tasks interleave on the
same interpreter. It is *not* parallel — the GIL (next section) prevents
threads from running Python bytecode on multiple cores at once. Concurrency
gives you **overlap of waiting time**; parallelism gives you **sharing of CPU
time across cores**. For I/O-heavy work, overlap is usually all you need.

---

## 2. The GIL

The **GIL (Global Interpreter Lock)** is a mutex inside CPython that allows
only one thread to execute Python bytecode at a time. This is why plain
threads never speed up CPU-bound Python.

```python
import sys

print(f"CPython GIL is used: {sys._is_gil_enabled()}")
```

**Conclusion:** the GIL exists to protect CPython's internals (and makes
single-threaded code fast), but it means threading cannot give real
parallelism for CPU-bound tasks. Therefore Python splits the work:

| Tool            | GIL impact                     | Best for           |
| --------------- | ------------------------------ | ------------------ |
| `threading`     | limited by GIL                 | I/O-bound work     |
| `asyncio`       | single-threaded, no GIL issue  | I/O-bound, async   |
| `multiprocessing` | bypasses GIL (own interpreters) | CPU-bound work |
| `concurrent.futures` | depends on pool type      | mixed workloads    |

> Note: Python 3.13+ added the experimental free-threaded build (no GIL).
> On a stock CPython, the reasoning above still holds.

---

## 3. Choosing a tool

Ask two questions about the workload:

1. **CPU-bound** (math, compression, image processing) → the task wants a CPU
   core for the whole time. Threads can't help → `multiprocessing`.
2. **I/O-bound** (network requests, file reads, database calls) → the task
   spends most of its time *waiting*. Threads or asyncio can overlap that
   waiting → `threading` or `asyncio`.

Quick decision flow:

```
Is the task CPU-bound?
   yes -> multiprocessing / ProcessPoolExecutor
   no  -> Is your ecosystem already async (aiohttp, asyncpg, FastAPI)?
             yes -> asyncio
             no  -> threading / ThreadPoolExecutor
```

**Conclusion:** there is no single "best" concurrency tool — the workload
determines the choice. Getting this choice wrong is the most common mistake:
people use threads for CPU-bound work and see *slower* results because of
thread-creation overhead plus the GIL.

---

## 4. Threading

Threads are lightweight (they share the process memory and file descriptors)
and are the default choice for I/O-bound fan-out.

### 4.1 Thread basics

```python
import threading
import time


def worker(name, delay):
    print(f"[{name}] starting")
    for i in range(3):
        time.sleep(delay)
        print(f"[{name}] step {i}")
    print(f"[{name}] done")


threads = []
for name in ("A", "B", "C"):
    t = threading.Thread(target=worker, args=(name, 0.3), name=name)
    threads.append(t)
    t.start()          # schedules the thread to run

for t in threads:
    t.join()           # main thread blocks until t finishes

print("All threads finished.")
```

**Conclusion:** `Thread(target=..., args=...)` defines the work, `.start()`
launches it without blocking, and `.join()` lets the caller wait. Threads
run in the *same* interpreter and memory space, so there is no pickling of
arguments and almost no startup cost — perfect for many concurrent sockets,
HTTP calls, or file operations.

### 4.2 Locks and race conditions

Threads share memory. If two threads update the same variable "at the same
time", the operations interleave and updates get lost — a **race condition**.

```python
import threading


class UnsafeCounter:
    def __init__(self):
        self.value = 0

    def increment(self):
        current = self.value          # read
        for _ in range(10000):
            pass                      # simulate work -> race window
        self.value = current + 1      # write (overwrites other thread's write)


class SafeCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:              # only one thread inside at a time
            current = self.value
            for _ in range(10000):
                pass
            self.value = current + 1


def bump(counter, times):
    for _ in range(times):
        counter.increment()


THREADS, PER = 8, 200

unsafe = UnsafeCounter()
ts = [threading.Thread(target=bump, args=(unsafe, PER)) for _ in range(THREADS)]
[t.start() for t in ts]
[t.join() for t in ts]

safe = SafeCounter()
ts = [threading.Thread(target=bump, args=(safe, PER)) for _ in range(THREADS)]
[t.start() for t in ts]
[t.join() for t in ts]

expected = THREADS * PER
print(f"expected = {expected}")
print(f"unsafe   = {unsafe.value}   (often less -> lost updates)")
print(f"safe     = {safe.value}   (always correct)")
```

**Conclusion:** the unsafe counter routinely reports fewer than 1600 because
two threads read the same value, then both write, and one increment vanishes.
A `Lock` (used with `with`) turns the read-modify-write sequence into an
**atomic critical section**. Rules of thumb: lock the *smallest* region you
can, always use `with` (it releases on exceptions), and prefer a
`queue.Queue` when you don't need fine-grained control.

### 4.3 Thread-safe queues

The cleanest way to hand work between threads: producers `put()`, consumers
`get()`, and the queue handles locking internally.

```python
import queue
import threading
import time

WORK = 10


def producer(q):
    for i in range(WORK):
        time.sleep(0.1)
        q.put(f"job-{i}")
    q.put(None)                        # sentinel: no more work


def consumer(q, name):
    while True:
        item = q.get()
        if item is None:               # forward sentinel, then stop
            q.put(None)
            q.task_done()
            break
        time.sleep(0.2)
        print(f"[{name}] processed {item}")
        q.task_done()                  # tells q.join() we finished one item


q = queue.Queue()
threads = [
    threading.Thread(target=producer, args=(q,)),
    threading.Thread(target=consumer, args=(q, "w1")),
    threading.Thread(target=consumer, args=(q, "w2")),
]
for t in threads:
    t.start()

q.join()                               # returns when all items are task_done()
print("All work processed.")
```

**Conclusion:** `queue.Queue` is the recommended way to pass data between
threads because it hides all the locking. The **sentinel** (`None`) is the
standard way to tell consumers "no more work". `q.join()` gives the main
thread a natural rendezvous point. This producer/consumer pattern scales to
any number of workers by just adding threads.

### 4.4 Events and barriers

- `Event` — one thread broadcasts a signal; others `wait()` for it.
- `Barrier(N)` — exactly `N` threads must arrive before any of them continue.

```python
import threading
import time

# Event: all runners start on the referee's signal
ready = threading.Event()


def athlete(name):
    print(f"[{name}] warming up")
    time.sleep(0.3)
    ready.wait()
    print(f"[{name}] GO!")


runners = [threading.Thread(target=athlete, args=(f"r{i}",)) for i in range(3)]
for t in runners:
    t.start()
time.sleep(0.5)
ready.set()                            # release everyone
for t in runners:
    t.join()

print("---")

# Barrier: three workers must all reach phase 1 before any enters phase 2
barrier = threading.Barrier(3)


def phase_worker(name):
    for phase in range(2):
        time.sleep(0.1 * phase)
        print(f"[{name}] reached phase {phase}")
        barrier.wait()
        print(f"[{name}] passed phase {phase}")


workers = [threading.Thread(target=phase_worker, args=(f"w{i}",)) for i in range(3)]
for t in workers:
    t.start()
for t in workers:
    t.join()
print("Barrier released all workers together.")
```

**Conclusion:** `Event` is for a *broadcast* (start signal, shutdown flag).
`Barrier` is for *synchronization of phase boundaries*: nobody proceeds to
the next phase until the whole group has arrived. Events are far more common;
barriers shine in parallel algorithms with rounds (e.g. distributed
simulations, iterative solvers).

---

## 5. Multiprocessing

Processes are separate interpreters with separate memory and **their own
GIL**, so they truly run on multiple cores. This is the tool for
CPU-bound work. The cost: process creation is slow and data must be
explicitly passed between processes.

### 5.1 Process basics

```python
import multiprocessing
import os
import time


def worker(name):
    print(f"[{name}] pid={os.getpid()} parent={os.getppid()}", flush=True)
    time.sleep(1)
    print(f"[{name}] done", flush=True)


if __name__ == "__main__":
    print(f"[main] pid={os.getpid()}", flush=True)
    procs = [multiprocessing.Process(target=worker, args=(f"P{i}",)) for i in range(4)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print("All processes finished.")
```

**Conclusion:** each worker prints a *different* `pid` — a real OS process.
The `if __name__ == "__main__":` guard is mandatory because child processes
re-import the module (the `spawn` start method). The API mirrors
`threading`, but memory and the GIL are no longer shared: each process runs
Python bytecode in true parallel. Always wrap process-heavy code in the
`__main__` guard.

### 5.2 Process communication

Because processes don't share memory, results travel through `Queue` or
`Pipe`.

```python
import multiprocessing


def square(q, n):
    q.put((n, n * n))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    q = multiprocessing.Queue()
    procs = [multiprocessing.Process(target=square, args=(q, n)) for n in numbers]

    for p in procs:
        p.start()
    results = [q.get() for _ in numbers]
    for p in procs:
        p.join()

    for n, sq in sorted(results):
        print(f"square({n}) = {sq}")
```

**Conclusion:** `Queue` is a thread- and process-safe pipe. The pattern is
"children `put` results, parent `get`s them". This is the idiomatic way to
collect output: each child writes its answer, and the parent reads exactly
one value per child. Never try to share plain Python objects between
processes — use `Queue`/`Pipe` or the shared objects of the next section.

### 5.3 Shared memory

When a mutable value really must be shared, use `Value`, `Array`, or a
`Manager` (which serves proxy objects for dicts, lists, namespaces...).

```python
import multiprocessing


def add_money(value, lock, amount):
    for _ in range(100):
        with lock:
            value.value += amount


if __name__ == "__main__":
    value = multiprocessing.Value("i", 0)      # shared int
    lock = multiprocessing.Lock()
    procs = [
        multiprocessing.Process(target=add_money, args=(value, lock, 5))
        for _ in range(4)
    ]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print(f"shared value = {value.value}")      # expected 2000

    with multiprocessing.Manager() as manager:
        d = manager.dict()
        d["count"] = 0

        def bump():
            d["count"] += 1

        ps = [multiprocessing.Process(target=bump) for _ in range(4)]
        for p in ps:
            p.start()
        for p in ps:
            p.join()
        print(f"manager dict count = {d['count']}")
```

**Conclusion:** `Value`/`Array` give fast, low-level shared memory but you
still need a `Lock` to make read-modify-write atomic. `Manager` is slower but
much more convenient — it hosts real Python containers and hands out proxies,
so you can share dicts and lists without serialization worries. Rule of
thumb: prefer `Queue` for *communication*, `Manager` for *state* you want to
read from anywhere, `Value`/`Array` when performance matters.

### 5.4 Process pools

`multiprocessing.Pool` pre-spawns workers and distributes many tasks across
them — the standard way to parallelize CPU-bound work.

```python
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


if __name__ == "__main__":
    ranges = [(0, 100_000), (100_000, 200_000),
              (200_000, 300_000), (300_000, 400_000)]
    with multiprocessing.Pool(4) as pool:
        results = pool.starmap(count_primes, ranges)
    print("primes per range:", results)
    print("total primes    :", sum(results))
```

**Conclusion:** `pool.map(fn, items)` runs `fn` across the pool and returns
results in order. This single line parallelizes the CPU-bound loop across all
cores — the GIL does not apply because each worker is a separate process.
Using a pool is almost always better than hand-managing `Process` objects:
the pool reuses workers, handles the work queue, and cleans up. This is the
snippet to reach for whenever you have a pure-Python loop over a big dataset.

---

## 6. Asyncio

`asyncio` gives concurrency **without threads**: one event loop drives
thousands of coroutines, suspending each at `await` and resuming when I/O is
ready. Best for I/O-bound programs already using async libraries.

### 6.1 async/await basics

```python
import asyncio
import time


async def worker(name, duration):
    print(f"[{name}] starting")
    await asyncio.sleep(duration)
    print(f"[{name}] finished")
    return name


async def main():
    start = time.perf_counter()
    results = await asyncio.gather(worker("A", 1), worker("B", 1), worker("C", 1))
    print(f"results: {results}")
    print(f"elapsed: {time.perf_counter() - start:.2f}s  (not 3s!)")


if __name__ == "__main__":
    asyncio.run(main())
```

**Conclusion:** `async def` defines a *coroutine* — it runs nothing until
scheduled. `await` is the magic switch: while one coroutine sleeps, the loop
runs others. `asyncio.run()` bootstraps the loop. Three 1-second tasks finish
in ~1 second because they *overlap their waiting*. The whole program is a
single thread — no locks, no race conditions on shared data (unless you mix
in blocking calls).

### 6.2 Tasks, gather, wait

```python
import asyncio


async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"data from {name}"


async def main():
    task = asyncio.create_task(fetch("background", 1.0))   # runs in background
    print("task created; doing other work...")

    results = await asyncio.gather(fetch("google", 0.3), fetch("github", 0.5), fetch("pypi", 0.2))
    print("gather:", results)

    print("background:", await task)                        # collect the background result

    tasks = [asyncio.create_task(fetch(f"site-{i}", 0.4)) for i in range(3)]
    done, pending = await asyncio.wait(tasks)
    print(f"wait: done={len(done)} pending={len(pending)}")


if __name__ == "__main__":
    asyncio.run(main())
```

**Conclusion:** `create_task` schedules a coroutine to run concurrently while
you keep working — the async equivalent of starting a thread. `gather` is the
async equivalent of "join all and collect results", preserving order.
`wait` gives more control (timeout, return when-first-done) at the cost of
more bookkeeping. In real programs (FastAPI endpoints, web scrapers with
`aiohttp`) these three primitives handle 99% of the coordination.

### 6.3 Semaphores and timeouts

```python
import asyncio

SEMAPHORE = asyncio.Semaphore(3)


async def limited(name):
    async with SEMAPHORE:                 # at most 3 inside at once
        print(f"[{name}] working")
        await asyncio.sleep(1)
        print(f"[{name}] done")


async def slow():
    await asyncio.sleep(10)
    return "too slow"


async def main():
    await asyncio.gather(*(limited(f"req-{i}") for i in range(6)))

    try:
        async with asyncio.timeout(1.5):  # deadline of 1.5s
            await slow()
    except TimeoutError:
        print("timed out waiting for slow()")


if __name__ == "__main__":
    asyncio.run(main())
```

**Conclusion:** concurrency doesn't mean *unlimited* — a `Semaphore` caps how
many tasks run at once (e.g. polite rate limits on a public API). `timeout`
gives every await a deadline so a hung service can't stall the whole
program. These two tools make async programs both fast *and* resilient.

---

## 7. concurrent.futures

`concurrent.futures` is a thin, uniform wrapper over threads and processes.
It exposes the same interface for both and is often the simplest thing that
works.

### 7.1 ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def fetch_url(name):
    time.sleep(0.3)                       # pretend network call
    return f"{name} -> ok"


with ThreadPoolExecutor(max_workers=4) as pool:
    futures = [pool.submit(fetch_url, f"site-{i}") for i in range(8)]
    for f in as_completed(futures):       # yield results as they finish
        print(f.result())
```

**Conclusion:** `submit` returns a `Future`; `as_completed` iterates as
results arrive, so a fast request isn't held up by a slow one. The `with`
block shuts the pool down cleanly. Thread pools are ideal for the many-small-
network-requests pattern and save you from writing manual thread bookkeeping.

### 7.2 ProcessPoolExecutor

```python
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
        totals = pool.map(sum_primes, ranges)     # spread across cores
    print("primes:", list(totals))
```

**Conclusion:** switching from `ThreadPoolExecutor` to
`ProcessPoolExecutor` is a one-line change that gives real parallelism for
CPU-bound code. The interface is identical to threads — that is the whole
point of `concurrent.futures`. For most applications, if you don't need
asyncio's scale, this module is the right default: simple, predictable, and
easy to switch between thread and process modes.

---

## 8. Final conclusions

**The one thing to remember:** *workload decides the tool.*

1. **CPU-bound** work needs real cores → `multiprocessing` or
   `ProcessPoolExecutor`. Threads cannot help; the GIL gets in the way.
2. **I/O-bound** work needs overlapped waiting → `threading` or
   `ThreadPoolExecutor`, or `asyncio` if your ecosystem is already async.
3. **Shared mutable state** is the root of most bugs:
   - threads: guard with `Lock` or use `queue.Queue`;
   - processes: use `Queue`/`Pipe`/`Manager` — never plain objects;
   - async: usually no locks needed at all.
4. **`concurrent.futures`** is the lowest-friction entry point: one interface,
   two backends, zero manual bookkeeping.
5. **Verify with measurement.** The `fundamentals/03_benchmark_cpu_vs_io.py`
   script in this directory measures a workload under all four strategies.
   A tool only "works" if it's actually faster on *your* workload.

Where the concepts fit:

| Task                       | Tool            | Speed-up vs serial |
| -------------------------- | --------------- | ------------------ |
| 1000 HTTP requests         | threads / async | up to ~1000x overlap |
| 1M prime check             | processes       | ~number of cores   |
| many file reads/writes     | threads / async | high (I/O wait)    |
| heavy matrix math          | processes (or NumPy) | ~cores       |

Start simple: use `concurrent.futures`, measure, and only reach for
`asyncio` or hand-managed `multiprocessing` when you hit its limits.
