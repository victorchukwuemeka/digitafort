# Generators & Decorators in Python
## A Complete Course
*Master two of Python's most powerful and elegant features*

---

## Table of Contents

**Part 1 — Generators**
1. [What is a Generator?](#module-1-what-is-a-generator)
2. [The yield Keyword](#module-2-the-yield-keyword)
3. [Generator Expressions](#module-3-generator-expressions)
4. [Chaining and Pipelines](#module-4-chaining-generators-into-pipelines)
5. [send(), throw(), and close()](#module-5-advanced-generators---send-throw-close)
6. [Real-World Generator Use Cases](#module-6-real-world-generator-use-cases)

**Part 2 — Decorators**

7. [What is a Decorator?](#module-7-what-is-a-decorator)
8. [Writing Your First Decorator](#module-8-writing-your-first-decorator)
9. [Decorators with Arguments](#module-9-decorators-with-arguments)
10. [Class-Based Decorators](#module-10-class-based-decorators)
11. [Stacking Decorators](#module-11-stacking-decorators)
12. [Real-World Decorator Use Cases](#module-12-real-world-decorator-use-cases)

**Bonus**

13. [Practical Exercise](#module-13-practical-exercise)
14. [Quick Reference Cheat Sheet](#quick-reference-cheat-sheet)

---

# PART 1 — GENERATORS

---

## Module 1: What is a Generator?

A generator is a special type of function that **produces values one at a time** instead of computing and returning everything at once. It pauses after each value and resumes when the next value is needed.

> 💡 **Think of a generator like a vending machine.** It does not make all the snacks upfront and pile them on the floor. It produces one snack at a time, only when you press the button.

### The Problem Generators Solve

```python
# ❌ Bad approach — loads ALL 1 million numbers into memory at once
def get_numbers_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

numbers = get_numbers_list(1_000_000)   # Uses ~400MB of memory!
print(numbers[0])


# ✅ Generator approach — produces one number at a time, uses almost no memory
def get_numbers_gen(n):
    for i in range(n):
        yield i * i

numbers = get_numbers_gen(1_000_000)   # Uses ~100 bytes of memory!
print(next(numbers))   # 0
print(next(numbers))   # 1
print(next(numbers))   # 4
```

### Regular Function vs Generator

| Feature | Regular Function | Generator |
|---------|-----------------|-----------|
| Returns | A single value | A sequence of values |
| Memory | Loads everything at once | One item at a time |
| Keyword | `return` | `yield` |
| Resumes | No — starts fresh | Yes — pauses and continues |
| Type | Any value | `generator` object |

---

## Module 2: The yield Keyword

`yield` is what turns a regular function into a generator. Every time Python hits a `yield`, it pauses the function, sends the value out, and waits. When you call `next()` again, it resumes from exactly where it left off.

### Basic yield Example

```python
def countdown(n):
    print("Starting countdown...")
    while n > 0:
        yield n          # pause here, send n out
        n -= 1           # resume here next time
    print("Done!")


# Create the generator — nothing runs yet!
gen = countdown(3)

print(next(gen))   # "Starting countdown..." then yields 3
print(next(gen))   # yields 2
print(next(gen))   # yields 1
print(next(gen))   # "Done!" then raises StopIteration
```

```
Output:
Starting countdown...
3
2
1
Done!
StopIteration
```

### Looping Over a Generator

You almost never call `next()` manually. Use a `for` loop instead — it handles `StopIteration` automatically:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)
# Output: 5, 4, 3, 2, 1
```

### yield with Multiple Values

```python
def daily_report():
    yield "Morning standup done"
    yield "Code review completed"
    yield "Bug fixed in production"
    yield "PR submitted"

for update in daily_report():
    print(f"✅ {update}")
```

### Infinite Generators

A generator can run forever — this is safe because it only produces values on demand:

```python
def fibonacci():
    """Infinite Fibonacci sequence"""
    a, b = 0, 1
    while True:        # runs forever
        yield a
        a, b = b, a + b


gen = fibonacci()

# Take only the first 10 numbers
for _ in range(10):
    print(next(gen), end=' ')

# Output: 0 1 1 2 3 5 8 13 21 34
```

### Checking the Generator State

```python
import inspect

def simple_gen():
    yield 1
    yield 2

gen = simple_gen()
print(inspect.getgeneratorstate(gen))   # GEN_CREATED

next(gen)
print(inspect.getgeneratorstate(gen))   # GEN_SUSPENDED

next(gen)
print(inspect.getgeneratorstate(gen))   # GEN_SUSPENDED

try:
    next(gen)
except StopIteration:
    pass

print(inspect.getgeneratorstate(gen))   # GEN_CLOSED
```

---

## Module 3: Generator Expressions

Generator expressions are like list comprehensions but with `()` instead of `[]`. They create a generator on the spot without writing a full function.

### List Comprehension vs Generator Expression

```python
# List comprehension — creates entire list in memory immediately
squares_list = [x * x for x in range(1_000_000)]   # ~400MB
print(type(squares_list))   # <class 'list'>

# Generator expression — creates a lazy generator, uses almost no memory
squares_gen = (x * x for x in range(1_000_000))    # ~100 bytes
print(type(squares_gen))    # <class 'generator'>
```

### Syntax

```python
# List:      [expression for item in iterable if condition]
# Generator: (expression for item in iterable if condition)

# Examples:
evens = (x for x in range(100) if x % 2 == 0)
names = (name.upper() for name in ['alice', 'bob', 'charlie'])
lengths = (len(word) for word in ['hello', 'world', 'python'])
```

### Passing Generators Directly to Functions

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# You can pass generator expressions directly — no extra parentheses needed
total = sum(x * x for x in numbers)
maximum = max(x for x in numbers if x % 2 == 0)
filtered = list(x for x in numbers if x > 5)

print(total)    # 385
print(maximum)  # 10
print(filtered) # [6, 7, 8, 9, 10]
```

### Nested Generator Expressions

```python
# Flatten a 2D matrix lazily
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = (num for row in matrix for num in row)

print(list(flat))   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Module 4: Chaining Generators into Pipelines

One of the most powerful uses of generators is building **lazy pipelines** — a series of steps where data flows through without loading everything into memory.

### Building a Data Pipeline

```python
# Imagine processing a massive log file

def read_lines(filename):
    """Step 1: Read file line by line"""
    with open(filename) as f:
        for line in f:
            yield line.strip()

def filter_errors(lines):
    """Step 2: Keep only error lines"""
    for line in lines:
        if 'ERROR' in line:
            yield line

def parse_message(lines):
    """Step 3: Extract just the message part"""
    for line in lines:
        parts = line.split(' - ')
        if len(parts) >= 2:
            yield parts[-1]

def uppercase(lines):
    """Step 4: Transform to uppercase"""
    for line in lines:
        yield line.upper()


# Connect the pipeline — nothing runs yet!
lines = read_lines('app.log')
errors = filter_errors(lines)
messages = parse_message(errors)
result = uppercase(messages)

# Now process — data flows through all steps one line at a time
for message in result:
    print(message)
```

>  This pipeline processes one line at a time through all steps. Even a 10GB log file uses almost no memory.

### Using itertools for More Power

```python
import itertools

def count_up(start=0):
    n = start
    while True:
        yield n
        n += 1

# itertools.islice — take only N items from an infinite generator
first_10 = list(itertools.islice(count_up(), 10))
print(first_10)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# itertools.chain — combine multiple generators
gen1 = (x for x in [1, 2, 3])
gen2 = (x for x in [4, 5, 6])
combined = list(itertools.chain(gen1, gen2))
print(combined)   # [1, 2, 3, 4, 5, 6]

# itertools.takewhile — take values until condition fails
numbers = count_up()
below_10 = list(itertools.takewhile(lambda x: x < 10, numbers))
print(below_10)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Module 5: Advanced Generators — send(), throw(), close()

Generators are not just one-way. You can communicate back into a running generator using `send()`, inject exceptions with `throw()`, and shut it down with `close()`.

### Better Note — How Advanced Generators Actually Work

Think of a generator as a **paused function frame**. Each `yield` is a checkpoint that both sends a value **out** and can receive a value **back in**. That leads to a few important rules:

- You must **prime** the generator (call `next(gen)` or `gen.send(None)`) before you can send real values.
- `value = yield something` means: **send `something` out now, then later assign the next sent-in value to `value`**.
- `throw()` raises an exception **inside** the generator at the current pause point, so it behaves like an internal error you can catch.
- `close()` triggers `GeneratorExit` and runs any `finally` blocks, which is where cleanup should live.

This mental model makes `send()`, `throw()`, and `close()` feel less magical and more like controlled pause/resume with a two‑way channel.

### send() — Passing Values INTO a Generator

```python
def accumulator():
    """A generator that keeps a running total"""
    total = 0
    while True:
        value = yield total    # yield sends total OUT, receives new value IN
        if value is None:
            break
        total += value


gen = accumulator()
next(gen)           # Must call next() first to start the generator — yields 0

print(gen.send(10))   # sends 10 in, total becomes 10, yields 10
print(gen.send(20))   # sends 20 in, total becomes 30, yields 30
print(gen.send(5))    # sends 5 in, total becomes 35, yields 35
```

### throw() — Injecting Exceptions

```python
def safe_processor():
    while True:
        try:
            value = yield
            print(f"Processing: {value}")
        except ValueError as e:
            print(f"Caught error: {e}, continuing...")

gen = safe_processor()
next(gen)

gen.send("hello")             # Processing: hello
gen.throw(ValueError, "bad data")   # Caught error: bad data, continuing...
gen.send("world")             # Processing: world
```

### close() — Shutting Down a Generator

```python
def resource_generator():
    print("Opening resource...")
    try:
        while True:
            yield "data"
    finally:
        print("Closing resource...")   # Always runs on close()


gen = resource_generator()
print(next(gen))   # Opening resource... then "data"
print(next(gen))   # "data"
gen.close()        # Closing resource...
```

---

## Module 6: Real-World Generator Use Cases

### Use Case 1 — Reading Large Files

```python
def read_large_csv(filepath):
    """Read a CSV file line by line without loading it all into memory"""
    with open(filepath, 'r') as f:
        header = next(f).strip().split(',')
        for line in f:
            values = line.strip().split(',')
            yield dict(zip(header, values))


# Process a 5GB CSV file with almost no memory usage
for row in read_large_csv('huge_dataset.csv'):
    process_row(row)   # handle one row at a time
```

### Use Case 2 — Database Pagination

```python
import sqlite3

def paginate_query(query, page_size=100):
    """Fetch database results in chunks instead of all at once"""
    conn = sqlite3.connect('mydb.sqlite')
    cursor = conn.cursor()
    offset = 0

    while True:
        cursor.execute(f"{query} LIMIT {page_size} OFFSET {offset}")
        rows = cursor.fetchall()

        if not rows:
            conn.close()
            return

        for row in rows:
            yield row

        offset += page_size


# Works seamlessly — fetches 100 rows at a time
for user in paginate_query("SELECT * FROM users"):
    send_email(user)
```

### Use Case 3 — Generating Unique IDs

```python
import uuid
import itertools

def id_generator(prefix='USR'):
    """Generate unique sequential IDs"""
    for i in itertools.count(1):
        yield f"{prefix}-{i:06d}"


gen = id_generator()
print(next(gen))   # USR-000001
print(next(gen))   # USR-000002
print(next(gen))   # USR-000003
```

### Use Case 4 — Real-Time Data Streaming

```python
import time

def sensor_stream(sensor_id, interval=1.0):
    """Simulate a real-time sensor data stream"""
    import random
    while True:
        yield {
            'sensor': sensor_id,
            'temperature': round(random.uniform(20.0, 30.0), 2),
            'timestamp': time.time()
        }
        time.sleep(interval)


# Process sensor data as it arrives
stream = sensor_stream('SENSOR-01', interval=0.5)
for i, reading in enumerate(stream):
    print(f"Reading {i}: {reading}")
    if i >= 9:   # stop after 10 readings
        break
```

---

# PART 2 — DECORATORS

---

## Module 7: What is a Decorator?

A decorator is a function that **wraps another function** to add extra behaviour before or after it runs — without changing the original function's code.

>  **Think of a decorator like a sandwich wrapper.** The filling (your function) stays the same. The wrapper just adds something around it — maybe logging, timing, or authentication. You can change the wrapper without touching the filling.

### Better Note — Mental Model

A decorator is just **function reassignment** done neatly. This:

```python
@decorator
def foo():
    pass
```

is exactly the same as:

```python
def foo():
    pass

foo = decorator(foo)
```

So the decorator **replaces** the original name with a wrapped function. That is why `functools.wraps` is important — it copies the original metadata to the wrapper so tools, docs, and debugging still show the real function name.

### The Core Idea

```python
# Without a decorator — you have to manually wrap every function
def my_function():
    print("Hello!")

# Manually adding behaviour before and after
print("Before")
my_function()
print("After")


# With a decorator — the wrapping is automatic and reusable
@my_decorator
def my_function():
    print("Hello!")

my_function()   # automatically runs "Before", "Hello!", "After"
```

### Functions Are First-Class Objects

To understand decorators, you need to know that in Python, functions are objects. They can be stored in variables, passed as arguments, and returned from other functions:

```python
def greet():
    return "Hello!"

# Assign function to a variable
say_hi = greet
print(say_hi())   # Hello!

# Pass function as argument
def run_twice(func):
    func()
    func()

run_twice(greet)   # Hello! Hello!

# Return a function from a function
def make_greeter(name):
    def greeter():
        return f"Hello, {name}!"
    return greeter

hello_alice = make_greeter("Alice")
print(hello_alice())   # Hello, Alice!
```

---

## Module 8: Writing Your First Decorator

A decorator is just a function that takes a function and returns a new function.

### The Basic Structure

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Code that runs BEFORE the original function
        print("Before the function runs")

        result = func(*args, **kwargs)   # Call the original function

        # Code that runs AFTER the original function
        print("After the function runs")

        return result   # Return the original result
    return wrapper
```

### Applying a Decorator

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper


# Method 1: Using @ syntax (preferred)
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before
# Hello!
# After


# Method 2: Manual wrapping (same result, less elegant)
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
```

### The functools.wraps Fix

Without `functools.wraps`, your decorated function loses its name and docstring. Always use it:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)          # This preserves the original function's metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def add(a, b):
    """Adds two numbers together"""
    return a + b


print(add.__name__)   # add       (without wraps: "wrapper")
print(add.__doc__)    # Adds two numbers together   (without wraps: None)
```

### Practical Example — Timing Decorator

```python
import time
from functools import wraps

def timer(func):
    """Measures how long a function takes to run"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1.5)
    return "Done"

@timer
def fast_function(n):
    return sum(range(n))


slow_function()         # slow_function took 1.5001 seconds
fast_function(1000000)  # fast_function took 0.0523 seconds
```

### Practical Example — Logger Decorator

```python
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)

def log_calls(func):
    """Logs every time a function is called with its arguments"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper


@log_calls
def divide(a, b):
    return a / b


divide(10, 2)
# INFO: Calling divide with args=(10, 2), kwargs={}
# INFO: divide returned 5.0
```

---

## Module 9: Decorators with Arguments

Sometimes you want to pass configuration into your decorator. To do this, you wrap the decorator inside another function — creating a **decorator factory**.

### The Pattern

```python
# Without arguments:    @decorator
# With arguments:       @decorator(arg1, arg2)

def decorator_factory(arg1, arg2):
    def decorator(func):
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            # use arg1 and arg2 here
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Example — Retry Decorator

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1.0):
    """Retry a function if it raises an exception"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_error
        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.5)
def unstable_api_call():
    import random
    if random.random() < 0.7:   # fails 70% of the time
        raise ConnectionError("API is down")
    return "Success!"


result = unstable_api_call()
print(result)
```

### Example — Rate Limiter Decorator

```python
import time
from functools import wraps

def rate_limit(calls_per_second=1):
    """Limit how often a function can be called"""
    min_interval = 1.0 / calls_per_second
    last_called = [0.0]   # use list to allow mutation in closure

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait = min_interval - elapsed
            if wait > 0:
                time.sleep(wait)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator


@rate_limit(calls_per_second=2)   # max 2 calls per second
def fetch_data(url):
    print(f"Fetching: {url}")
    return "data"


for url in ['url1', 'url2', 'url3', 'url4']:
    fetch_data(url)   # automatically throttled to 2 per second
```

### Example — Cache / Memoize Decorator

```python
from functools import wraps

def memoize(func):
    """Cache function results to avoid repeated expensive computations"""
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.cache = cache   # expose cache for inspection
    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(50))   # instant — without memoize this would take forever!
print(fibonacci.cache) # see what was cached

# Python also has a built-in version:
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## Module 10: Class-Based Decorators

You can also create decorators using classes by implementing the `__call__` method. This is useful when your decorator needs to maintain state.

### Basic Class Decorator

```python
from functools import wraps

class Timer:
    """A class-based decorator for timing functions"""

    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        self.total_time = 0
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        import time
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        elapsed = time.perf_counter() - start

        self.total_time += elapsed
        self.call_count += 1

        print(f"{self.func.__name__} took {elapsed:.4f}s "
              f"(total: {self.total_time:.4f}s, calls: {self.call_count})")
        return result


@Timer
def compute(n):
    return sum(range(n))


compute(1000000)   # compute took 0.0521s (total: 0.0521s, calls: 1)
compute(2000000)   # compute took 0.1043s (total: 0.1564s, calls: 2)

print(compute.call_count)   # 2
print(compute.total_time)   # 0.1564...
```

### Class Decorator with Arguments

```python
class retry:
    def __init__(self, max_attempts=3, exceptions=(Exception,)):
        self.max_attempts = max_attempts
        self.exceptions = exceptions

    def __call__(self, func):
        from functools import wraps

        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(self.max_attempts):
                try:
                    return func(*args, **kwargs)
                except self.exceptions as e:
                    if attempt == self.max_attempts - 1:
                        raise
                    print(f"Retrying... ({attempt + 1}/{self.max_attempts})")
        return wrapper


@retry(max_attempts=4, exceptions=(ConnectionError, TimeoutError))
def connect_to_server():
    raise ConnectionError("Server unreachable")


connect_to_server()
```

---

## Module 11: Stacking Decorators

You can apply multiple decorators to a single function. They are applied **bottom-up** but execute **top-down**.

```python
from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

def underline(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<u>{result}</u>"
    return wrapper


@bold
@italic
@underline
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))
# Output: <b><i><u>Hello, Alice!</u></i></b>

# Execution order:
# 1. underline wraps greet first (bottom decorator)
# 2. italic wraps that
# 3. bold wraps that (top decorator)
# When called: bold runs → italic runs → underline runs → greet runs
```

### Real Example — Stacking Auth + Logging + Timing

```python
from functools import wraps
import time

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if not user or not user.get('is_authenticated'):
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    return wrapper

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"LOG: {func.__name__} called")
        result = func(*args, **kwargs)
        print(f"LOG: {func.__name__} completed")
        return result
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"TIME: {func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper


@timer
@log_call
@require_auth
def get_user_data(user_id, user=None):
    return {"id": user_id, "data": "secret"}


# Usage:
authenticated_user = {"name": "Alice", "is_authenticated": True}
result = get_user_data(42, user=authenticated_user)
print(result)
```

---

## Module 12: Real-World Decorator Use Cases

### Use Case 1 — Flask Route Protection (like JWT middleware)

```python
from functools import wraps
from flask import request, jsonify
import jwt

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            request.current_user = payload
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Unauthorized'}), 401
        return func(*args, **kwargs)
    return wrapper


@app.route('/profile')
@login_required
def profile():
    return jsonify(request.current_user)
```

### Use Case 2 — Input Validation Decorator

```python
from functools import wraps

def validate_types(**expected_types):
    """Validates argument types at runtime"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            import inspect
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            for param_name, expected_type in expected_types.items():
                if param_name in bound.arguments:
                    value = bound.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"Argument '{param_name}' must be {expected_type.__name__}, "
                            f"got {type(value).__name__}"
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_types(name=str, age=int, score=float)
def create_profile(name, age, score):
    return {"name": name, "age": age, "score": score}


create_profile("Alice", 30, 95.5)       # Works fine
create_profile("Bob", "thirty", 80.0)  # TypeError: 'age' must be int, got str
```

### Use Case 3 — Singleton Pattern

```python
def singleton(cls):
    """Ensure a class only has one instance"""
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class DatabaseConnection:
    def __init__(self):
        print("Connecting to database...")
        self.connected = True


db1 = DatabaseConnection()   # "Connecting to database..."
db2 = DatabaseConnection()   # nothing printed
print(db1 is db2)            # True — same instance!
```

### Use Case 4 — Django-Style Permission Decorator

```python
from functools import wraps

def permission_required(*permissions):
    """Require specific permissions to access a function"""
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            user_permissions = set(request.user.get('permissions', []))
            required = set(permissions)

            if not required.issubset(user_permissions):
                missing = required - user_permissions
                raise PermissionError(f"Missing permissions: {missing}")

            return func(request, *args, **kwargs)
        return wrapper
    return decorator


@permission_required('read_users', 'write_users')
def admin_panel(request):
    return "Admin panel content"
```

---

## Module 13: Practical Exercise

Build a **task management system** that uses both generators and decorators together.

### Requirements

- A generator that yields tasks from a database one page at a time
- A `@timer` decorator to track how long operations take
- A `@retry` decorator for unreliable database calls
- A `@log_calls` decorator that logs all function calls to a file
- A `@validate_types` decorator to ensure correct argument types

### Starter Code

```python
import time
import logging
from functools import wraps

# ─── YOUR DECORATORS ────────────────────────────────────

def timer(func):
    # TODO: measure and print execution time
    pass

def retry(max_attempts=3):
    # TODO: retry on failure
    pass

def log_calls(func):
    # TODO: log function name, args, and result
    pass


# ─── YOUR GENERATORS ────────────────────────────────────

def task_generator(tasks, page_size=5):
    # TODO: yield tasks in pages
    pass

def overdue_tasks(tasks):
    # TODO: yield only tasks past their deadline
    pass

def priority_pipeline(tasks, min_priority=5):
    # TODO: filter by priority, sort, yield one at a time
    pass


# ─── TEST DATA ──────────────────────────────────────────

tasks = [
    {"id": i, "title": f"Task {i}", "priority": i % 10, "done": i % 3 == 0}
    for i in range(1, 51)
]


# ─── MAIN ───────────────────────────────────────────────

@timer
@log_calls
def process_tasks(tasks):
    for task in priority_pipeline(tasks, min_priority=7):
        print(f"Processing: {task['title']} (priority {task['priority']})")


process_tasks(tasks)
```

---

## Quick Reference Cheat Sheet

```python
# ════════════════════════════════════════════════════════
# GENERATORS
# ════════════════════════════════════════════════════════

# Basic generator function
def my_gen():
    yield 1
    yield 2
    yield 3

for val in my_gen():
    print(val)

# Generator expression
gen = (x * x for x in range(10) if x % 2 == 0)

# Infinite generator
def count_forever(start=0):
    n = start
    while True:
        yield n
        n += 1

# Take N items from infinite generator
import itertools
first_5 = list(itertools.islice(count_forever(), 5))

# send() — pass values into a generator
def accumulator():
    total = 0
    while True:
        value = yield total
        total += value

gen = accumulator()
next(gen)        # prime it
gen.send(10)     # 10
gen.send(20)     # 30


# ════════════════════════════════════════════════════════
# DECORATORS
# ════════════════════════════════════════════════════════

from functools import wraps

# Basic decorator
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello, {name}!"


# Decorator with arguments
def repeat(times=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi():
    print("Hi!")


# Stacking decorators (bottom applies first)
@decorator_a    # applies third, runs first
@decorator_b    # applies second, runs second
@decorator_c    # applies first, runs third
def my_func():
    pass


# Class-based decorator
class CountCalls:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@CountCalls
def add(a, b):
    return a + b

add(1, 2)
add(3, 4)
print(add.count)   # 2
```

---

>  **You now understand two of Python's most powerful features.**
> Generators let you work with data lazily and efficiently at any scale. Decorators let you add reusable behaviour to any function cleanly and elegantly. Together, they make your Python code more professional, readable, and production-ready.
