"""04 — Events and barriers.

Event lets one thread broadcast a signal that others wait on.
Barrier forces N threads to wait until all of them have arrived, then they
all continue together (useful for synchronized phase starts).
"""
import threading
import time

print("--- Event ---")
ready = threading.Event()


def athlete(name):
    print(f"[{name}] warming up")
    time.sleep(0.3)
    ready.wait()
    print(f"[{name}] GO!")


runners = [threading.Thread(target=athlete, args=(f"runner-{i}",)) for i in range(3)]
for t in runners:
    t.start()
time.sleep(0.5)
print("[referee] ...waiting for all...")
ready.set()
for t in runners:
    t.join()

print()
print("--- Barrier ---")
barrier = threading.Barrier(3)


def phase_worker(name):
    for phase in range(2):
        time.sleep(0.2 * hash(name) % 3)
        print(f"[{name}] reached phase {phase}")
        barrier.wait()
        print(f"[{name}] passed phase {phase}")


workers = [threading.Thread(target=phase_worker, args=(f"w-{i}",)) for i in range(3)]
for t in workers:
    t.start()
for t in workers:
    t.join()

print("Barrier released all workers together.")
