"""02 — Locks and synchronization.

Threads share memory. Without protection, concurrent updates to a shared
counter race each other and lose updates. A Lock makes the critical section
exclusive. RLock is re-entrant: the same thread can acquire it again.

Compare the "wrong" counter (unprotected) with the "safe" counter (locked).
Run several times to see the wrong counter drift.
"""
import threading


class UnprotectedCounter:
    def __init__(self):
        self.value = 0

    def increment(self):
        current = self.value
        for _ in range(10000):
            pass
        self.value = current + 1


class LockedCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            current = self.value
            for _ in range(10000):
                pass
            self.value = current + 1


def bump(counter, times):
    for _ in range(times):
        counter.increment()


THREADS = 8
PER_THREAD = 200

wrong = UnprotectedCounter()
wrong_threads = [threading.Thread(target=bump, args=(wrong, PER_THREAD)) for _ in range(THREADS)]
for t in wrong_threads:
    t.start()
for t in wrong_threads:
    t.join()

safe = LockedCounter()
safe_threads = [threading.Thread(target=bump, args=(safe, PER_THREAD)) for _ in range(THREADS)]
for t in safe_threads:
    t.start()
for t in safe_threads:
    t.join()

expected = THREADS * PER_THREAD
print(f"Expected result : {expected}")
print(f"Unprotected     : {wrong.value}   (lost updates?)")
print(f"Protected (Lock): {safe.value}   (correct)")
