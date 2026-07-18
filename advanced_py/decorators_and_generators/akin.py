"""
timer 
"""

# we are to import  

import time 
from functools import wraps 


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
