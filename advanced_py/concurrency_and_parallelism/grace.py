import queue 
import time 
import threading 



WORK = 10

def prod(q):
    for i in range(WORK):
        time.sleep(0.1)
        q.put(f"job -{i}")


def con(q, name):
    while True:
        item = q.get()
        if item is None: 
            q.put(None)
            q.task_done()
            break 
        time.sleep(0.2)
        print(f"{name}  and  {item}") 
        q.task_done()


q = queue.Queue()


    

threads = [
    threading.Thread(target=prod, args=(q,)),
    threading.Thread(target=con, args=(q, "w1")),
    threading.Thread(target=con, args=(q, "w2"))
]




for t in threads:
    t.start()

q.join()

print("good good ")
