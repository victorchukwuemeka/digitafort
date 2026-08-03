"""03 — Shared memory.

When you truly need a mutable value across processes, multiprocessing gives
you Value / Array (shared, synchronous objects) and Manager (a server that
hosts proxies to shared dicts, lists, Namespaces, etc.).
"""
import multiprocessing


def add_money(shared_value, lock, amount):
    for _ in range(100):
        with lock:
            shared_value.value += amount


if __name__ == "__main__":
    shared_value = multiprocessing.Value("i", 0)
    lock = multiprocessing.Lock()

    depositers = [
        multiprocessing.Process(target=add_money, args=(shared_value, lock, 5))
        for _ in range(4)
    ]

    for p in depositers:
        p.start()
    for p in depositers:
        p.join()

    print(f"Final shared value: {shared_value.value}")

    with multiprocessing.Manager() as manager:
        shared_dict = manager.dict()
        shared_dict["count"] = 0

        def worker():
            shared_dict["count"] = shared_dict["count"] + 1

        procs = [multiprocessing.Process(target=worker) for _ in range(4)]
        for p in procs:
            p.start()
        for p in procs:
            p.join()

        print(f"Manager dict count: {shared_dict['count']}")
