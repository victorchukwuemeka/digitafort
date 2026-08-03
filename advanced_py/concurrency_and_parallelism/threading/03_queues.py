"""03 — Producer / consumer with Queue.

queue.Queue is thread-safe: producers put work in, consumers take it out.
This is the classic way to hand tasks between threads without manual locks.
queue.task_done() + queue.join() lets the main thread wait until the queue
is fully drained.
"""
import queue
import threading
import time

WORK_ITEMS = 10


def producer(q):
    for i in range(WORK_ITEMS):
        time.sleep(0.1)
        q.put(f"job-{i}")
        print(f"[producer] queued job-{i}")
    q.put(None)


def consumer(q, name):
    while True:
        item = q.get()
        if item is None:
            q.put(None)
            q.task_done()
            break
        time.sleep(0.2)
        print(f"[{name}] processed {item}")
        q.task_done()


q = queue.Queue()
threads = [
    threading.Thread(target=producer, args=(q,)),
    threading.Thread(target=consumer, args=(q, "worker-1")),
    threading.Thread(target=consumer, args=(q, "worker-2")),
]

for t in threads:
    t.start()

q.join()
print("All work items processed.")
