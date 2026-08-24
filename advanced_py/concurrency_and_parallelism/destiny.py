import multiprocessing 
#import os 



#todo -> import 
"""
def call_name():
    print("don't call Please")

names = ['bob', 'alice',"sunday"]

for _ in names:
    call_name()
"""


def sq(q,n):
    q.put((n,n*n))


if __name__ == "__main__":
    nums = [6,7,8,9,10]
    q = multiprocessing.Queue()
    procs = [multiprocessing.Process(target=sq, args=(q,num)) for num in nums]

    for p in procs:
        p.start()
    result = [q.get() for _ in nums]
    for p in  procs: 
        p.join()
    
    for n, sq sorted(result):
        print(f"square({n}) = {sq}")






"""
def worker(name):
    print(f"{name} pid={os.getpid()}, parent={os.getpid()}",  flush=True)
    time.sleep(0.3)
    print(f"{name}Done", flush=True )


if __name__ == "__main__":
    mp = [multiprocessing.Process(target=worker , args=(f"P{i}",))for i in range(3)]
    for m in mp:
        m.start()
    for p in mp:
        p.join()
    print('done')
"""
































"""
import threading 
import time 


# creating our event obj 
ready = threading.Event()


# person 
def person(name):
    #  the name of the person this is  when he started 
    print(f" he is warming up  {name}")
    time.sleep(0.3)
    ready.wait()
    print(f" Start Running  {name}  Go! ")


names  = ['bob','alice','john']


runner   = [threading.Thread(target=person, args=(i,))for i in names]

#  loop into t hread to call the methods in the thrreead 

for t in runner :
    t.start()
time.sleep(0.5)
ready.set()

#
for t in runner: 
    t.join()



print(" ----")


b = threading.Barrier(3)

def p_w(name):
    for p in range(3):
        time.sleep(0.3 *  p)
        print(f"{name} this is before the first {p} ")
        b.wait()
        print(f"{name} this is after the  B phase  {p}")



worker = [threading.Thread(target=p_w, args=())for i in range(3)]    

for t_b in worker:
    t_b.start()
for t_b in worker:
    t_b.join()


print("hfhfhfhfhfhfhfhfh")


"""






"""
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

"""
safe = SafeCounter()
ts = [threading.Thread(target=bump, args=(safe,PER))for _ in range(THREADS)]
[t.start() for t in ts ]
[t.join() for t in ts]
"""

"""
expected = THREADS * PER
print(f"expected = {expected}=================================================   should be this ")
print(f"unsafe   = {unsafe.value}   (often less -> lost updates)")
#print(f"safe     = {safe.value}   (always correct)")
"""
