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

