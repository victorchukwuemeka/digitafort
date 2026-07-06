
"""
import functools
import time


# create a simple function
def greet():
    return "Hello!"

# create var in to store the func
say_hi  = greet
#print(say_hi())




#pass the func as arg 
def run_t(func):
    func()
    func()
    


#print(run_t(greet))



def make_greeter(name):
    # the greeter func
    def greeter():
        return f"Hello, {name}"
    return greeter 

hello = make_greeter("alice")
print(hello())

"""
"""
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)

def log_call(func):
    #log the func call with arguments  
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"calling {func.__name__} with args={args}, Kwargs={kwargs} ")
        result = func(*args, **kwargs)
        logging.info(f"calling{func.__name__} and {result}")
        return result 
    return wrapper


@log_call
def divide(a,b):
    return a / b 


divide(19,89)








from functools import wraps

def shout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(">>> Start the action")
        result = func(*args, **kwargs)
        print(">>> Stop the action")
    return wrapper 



@shout
def greet(name):
    print("Hello, {name}")
    
greet("Alice")