
""""
def get_num_list(num):
    num_list = []
    for n in range(num):
        num_list.append(n *1)
    return num_list 

num = 10000000000
#num_index  = get_num_list(num)
#print(num_index)
"""

"""
def get_num_gen(num):
    for n in range(num):
        yield n * 1 
num = 100000000000

num_gen  = get_num_gen(num)
for n in num_gen:
    print(n)
    
print(next(num_gen))
print(next(num_gen))


def countdown(n):
    while n > 0:
        yield n 
        n -=  1

gen2 = countdown(3)
print(next(gen2))
print(next(gen2))
print(next(gen2))
"""
"""
num = 200
name = "victor"
 
gen  = (x + x for  x in range(200))
"""



"""
import itertools 

def count_up(start=0):
    n = start 
    while True :
        yield n 
        n += 1

good = list(itertools.islice(count_up(),8))
print(good)



def acc():
    total = 0  
    while True:
       value = yield total  
       if value is None:
           break 
       total +=  value  


print(acc())      
gen = acc()
next(gen)
print(gen.send(10))
print(gen.send(20))
print(gen.send(6))
"""







from functools import wraps

def shout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("anything ")
        result = func(*args, **kwargs)
        print("something")
        return result 
    return wrapper 

@shout
def greet(name):
    print(f"Good morning {name}")

greet("Bob")


 


