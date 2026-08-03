# Threading

Threads are the lightest-weight concurrency primitive in Python. They all
share the same memory space and the same interpreter, so creating a thread
is cheap. Because of the GIL (see `fundamentals/01_gil.py`) threads are the
right tool for **I/O-bound** work: many tasks that mostly wait on network
sockets, files or sleep.

## Lessons

- `01_thread_basics.py` — creating, starting and joining threads
- `02_locks_and_synchronization.py` — `Lock`, `RLock` and safe counters
- `03_queues.py` — producer/consumer with `Queue`
- `04_events_and_barriers.py` — coordinating threads with `Event` / `Barrier`
- `05_daemon_threads.py` — background workers that die with the main thread

## Key ideas

- `Thread(target=fn, args=(...))` creates a thread; `.start()` begins it.
- `.join()` makes the caller wait until the thread finishes.
- Threads share memory, so always protect mutable state with a `Lock`.
- `queue.Queue` is the safe, simple way to pass work between threads.
- The GIL limits threads to *concurrency*, not CPU parallelism.
