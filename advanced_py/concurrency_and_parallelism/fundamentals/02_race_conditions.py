"""02 — Race conditions.

Concurrent access to shared state is the #1 source of bugs. This demo shows a
counter updated by many threads: without a lock, increments are lost.
"""
import threading


class UnsafeCounter:
    def __init__(self):
        self.value = 0

    def increment(self):
        current = self.value
        for _ in range(10000):
            pass
        self.value = current + 1


class SafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            current = self.value
            for _ in range(10000):
                pass
            self.value = current + 1


THREADS, PER = 8, 200


def run(counter):
    threads = [threading.Thread(target=lambda: [counter.increment() for _ in range(PER)])
               for _ in range(THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


unsafe = UnsafeCounter()
run(unsafe)

safe = SafeCounter()
run(safe)

expected = THREADS * PER
print(f"expected = {expected}")
print(f"unsafe   = {unsafe.value}")
print(f"safe     = {safe.value}")
