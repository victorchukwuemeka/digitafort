# lock and race conditions ,   nornal counter   ogj that count from 0  to 100000

import threading 


class Unsafecounter:
    def __init__(self):
        self.value = 0 

    def counting(self):
        current  = self.value 
        for i  in range(10000):
            print(i)
        self.value  = current +  1 



class SafeCounter:
    def __init__(self):
        self.value  = 0 
        self._lock  = threading.Lock 

    def counting(self):
        while self._lock:
            current = self.value 
            for i in range(10000):
                print(i)
            self.value  = current 


def bump(counter, time):
    for _ in range(time):
        counter.counting()

THREADS, PER = 8 , 200 


unsafe = Unsafecounter()
th = [threading.Thread(target=bump, args=(unsafe,PER))for _ in range(THREADS)]
[t.start() for t in th]
[t.join() for t in th]


"""
safe = SafeCounter()
ts = [threading.Thread(target=bump, args=(safe,PER))for _ in range(THREADS)]
[t.start() for t in ts ]
[t.join() for t in ts]
"""


expected = THREADS * PER
print(f"expected = {expected}=================================================   should be this ")
print(f"unsafe   = {unsafe.value}   (often less -> lost updates)")
#print(f"safe     = {safe.value}   (always correct)")
