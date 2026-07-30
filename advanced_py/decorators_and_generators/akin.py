"""
timer 
"""

# we are to import  

 

"""
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        stop  = time.perf_counter()
        return result 
    return wrapper 


@timer
def process_data(n):
    return sum(range(n))


print(process_data(100000))
"""


import time 
from functools import wraps


# todo 
# dec fac

def deco_fac(max_at=3 , de=1.0):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_e = None
            for attempt in range(1, max_at + 1):   
                try:
                    return func(*args, **kwargs)          
                except Exception as e:
                    last_e = e
                    print(f"Attempt {attempt}/{max_at} failed: {e}")
                    if attempt < max_at:
                        time.sleep(de)
            raise last_e
        return wrapper 
    return deco 

@deco_fac(max_at=3, de=0.5)
def api_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("server down")
    return "ok"


result = api_call()



