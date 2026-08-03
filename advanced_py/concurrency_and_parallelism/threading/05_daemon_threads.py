"""05 — Daemon threads.

Daemon threads run in the background and are killed abruptly when the main
thread exits. They are useful for logging, telemetry or heartbeat tasks that
should never prevent program shutdown. Non-daemon threads keep the program
alive until they finish, so join() them if you need their results.
"""
import threading
import time

STOP = threading.Event()


def heartbeat():
    tick = 0
    while not STOP.is_set():
        tick += 1
        print(f"[daemon] heartbeat #{tick}")
        time.sleep(0.5)


daemon = threading.Thread(target=heartbeat, daemon=True)
daemon.start()

print("[main] working for 2 seconds...")
time.sleep(2)
STOP.set()

print("[main] finishing now; daemon thread is not joined, so it dies here.")
