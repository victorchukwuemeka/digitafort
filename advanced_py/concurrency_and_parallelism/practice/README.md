# Practice exercises

Try each one with the course knowledge before looking at solutions. Run a
file to reveal the model solution.

## 1. Parallel prime counter (CPU-bound)

Use `multiprocessing` to count primes below 1,000,000, split into 4 ranges.

## 2. Concurrent downloader (I/O-bound)

Simulate 20 network requests (`time.sleep`) with `ThreadPoolExecutor`
`max_workers=5`. Print each result as it finishes with `as_completed`.

## 3. Producer/consumer with queues

One producer thread generates numbers 0..49, two consumer threads sum the
even and odd ones separately. Use `queue.Queue` and sentinels.

## 4. Async rate limiter

Write an asyncio program with 10 tasks using a `Semaphore(3)`; each task
sleeps 1s. Assert the whole run takes about 4s, not 10s.

## 5. Locked bank account

Simulate 5 threads depositing 100 times with a random small amount into a
shared balance guarded by `threading.Lock`. Final balance must be exact.
