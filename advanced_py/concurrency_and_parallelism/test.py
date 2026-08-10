import threading 
import time 
import sys 



def make_dish(name, minuts):
    print(f"cook {name}  in so so {minuts}")
    time.sleep(5)
    print(f"{name}  done ")



th = [threading.Thread(target=make_dish, args=(f"dish-{i}", 1)) for i in range(3)]
for t in th:
    t.start()
for t in th:
    t.join(5)


import sys


print(f"CPython GIL is used: {sys._is_gil_enabled()}")
print("Kitchen finished. Total wall time ~1 min, not 3.")
    

