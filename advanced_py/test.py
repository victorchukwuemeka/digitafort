"""
import asyncio
import time 


async def fetch_data(url):
    print(f"start fetching data")
    await asyncio.sleep(2)
    print("keep fetching data ")
    return f"Fetched {url}"


async def main():
    urls  = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3",
        "https://example.com/4"]
    tasks = [fetch_data(url) for url in urls]

    ll = await asyncio.gather(*tasks)
    print(ll)


asyncio.run(main())

"""




"""
import threading
import time 



def print_numbers():
    for number in range(1,9):
        print(number)
        time.sleep(1)

def print_letters():
    for l in ["a","b","c","d","e"] :
        print(l)
        time.sleep(1.5)



threading_one = threading.Thread(target=print_numbers)
threading_two = threading.Thread(target=print_letters)


threading_one.start()
threading_two.start()


threading_one.join()
threading_two.join()

print(" all thread complete")
"""





"""
class Animal:
    def __init__(self):
        self.limb = 4
        self.eye = 2
        self.stomach = 1
        self.ear = 2
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
def animal_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()



animal_sound(dog)
animal_sound(cat)
"""
"""
def mega_2():
    return 4.4

def omega():
    return mega_2()
"""


# say we should use an int as para 
#it returns a float 
"""
def add(a:int, b:int)->float :
    c = omega()
    return float(c)
"""
"""
def sub(n):
    if n == 0:          
        return 0
    sub(n-1) 
    return n 

print(sub(3))
map()
"""

"""
def greet():
    return "hello"


good = greet()

def greetings(good):
    name = "kkkkk"
    return f"{name} + {good}"


def call_greet():
    return greet()


def victor(a,b):
    return a + b 
victor(2,3)


lambda a,b: a + b 



num = "victor"
for i in num:
    print(i)


"""



#sum = [2,3,4,5,55,66,6]

#lambda sum : sum[0+1] 


# map(lambda x:x+x, [1,2,3])

"""
def cd(n):
    while n > 0:
        yield n
        n -= 1

for num in cd(10):
    print(num)


def d_report():
    yield " standup"
    yield " bug fix"
    yield "pr submited"
    yield "deployments"


for today in d_report():
    print(today)



def f():
    a,b = 0,1
    while True:
        yield a,b
        a,b = b , a + b

for j in f():
    print(j) 

"""
"""
def go_and_eat(eat: bool):
    print(" EATING")
    return True

eaten = False
while eaten == False:
    go_and_eat(eaten)
    eaten = True
    print(eaten)

"""


"""
import inspect

def simp_gen():
    yield 1
    yield 2

gen = simp_gen()
print(inspect.getgeneratorstate(gen))

next(gen)
print(inspect.getgeneratorstate(gen))


next(gen)
print(inspect.getgeneratorstate(gen))   


try:
    next(gen)
except StopIteration:
    pass

print(inspect.getgeneratorstate(gen))   
g = (x for x in range(1000000))

for _ in range(20):
      print(next(g), end=' ')

even = (x for x in range(100) if x % 2 == 0)

for u in even:
    print(u)

"""


"""
m = [[1,2,3], [4,5,6], [7,8,9]]
f = (n for row in m for n in row)

for i in f:
    print(i)

"""

#load everything at once 
"""
def bring_data_at_once(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result 
"""



#first loading our file and getting the data line by line 
#making their is no spaces 

#filter error lines 
"""

def file_loading(filename):
    with open(filename) as f:
        for line in f.readlines():
            yield line.strip()


def filter_error(lines):
    for line in lines :
        if "ERROR" in lines:
            yield line


def parse_message(lines):
    for line in lines:
        parts  = line.split(' -')
        if len(parts) >= 2:
            yield [-1]


def uppercase(messages):
    for message in messages:
        yield message.upper()


csv = "example.csv"
main_csv  = file_loading(csv)
f_error = filter_error(main_csv)
message = parse_message(f_error)
result_message = uppercase(message)


for r in result_message:
    print(r)

"""




"""
creating the decorator
"""

"""
def decorator(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("stop ")
        return result
    return wrapper



@decorator
def say_hello():
    print('hello')

def hello():
    print('Good')

t  =  decorator(hello)
t()

"""





"""
from functools import wraps

def m_decorators(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@m_decorators
def add(a,b):
    return a + b
    
print(add.__name__)
print(add.__doc__)
"""
"""
import time 
from functools import wraps

def timer(func):
    """ measure the time a func takes"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        stop = time.perf_counter()
        print(f"{func.__name__} took {stop - start:.4f} seconds")
        return result
    return wrapper

"""


def add(a,b):
    c = a + b 
    return None 
