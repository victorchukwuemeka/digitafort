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

# Python Decorators

A decorator is a function that **wraps another function** to extend its behaviour — without modifying the original function's code.

---

## The Core Idea

`@decorator` syntax is just shorthand. These two are completely identical:

```python
@my_decorator
def foo():
    pass
```

```python
def foo():
    pass
foo = my_decorator(foo)  # foo is replaced with the wrapped version
```

Python takes your function, passes it into the decorator, and reassigns the name to whatever the decorator returns. That's it. There's no magic — just a function receiving another function and returning a new one.

---

## The Template (use this every time)

```python
from functools import wraps

def my_decorator(func):           # (1) receives the original function as an argument
    @wraps(func)                  # (2) copies name, docstring, etc. onto wrapper
    def wrapper(*args, **kwargs): # (3) *args/**kwargs means it works with ANY function signature
        # code that runs BEFORE
        result = func(*args, **kwargs)  # (4) actually calls the original function
        # code that runs AFTER
        return result             # (5) must return the result or the caller gets None
    return wrapper                # (6) returns the wrapper — NOT wrapper() — just the function object
```

**Three rules you cannot skip:**

| Rule | Why |
|---|---|
| `@wraps(func)` | Without it, your function loses its name and docstring. Debugging becomes painful. |
| `*args, **kwargs` | Makes the wrapper accept any function signature — not just specific ones. |
| `return result` | If you forget this, every decorated function silently returns `None`. |

---

## Basic Example

```python
from functools import wraps

def shout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(">>> Starting")          # runs first, before greet() does anything
        result = func(*args, **kwargs) # greet() runs here — prints "Hello, Alice!"
        print(">>> Done")              # runs after greet() finishes
        return result
    return wrapper


@shout                  # greet is now: greet = shout(greet)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
# >>> Starting
# Hello, Alice!
# >>> Done
```

> Notice that `greet("Alice")` is now actually calling `wrapper("Alice")` — but because of `@wraps`, it still looks and behaves like `greet` from the outside.

---

## Practical Example — Timer

Measures how long a function takes to run.

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()        # snapshot the time before the function runs
        result = func(*args, **kwargs)     # run the actual function
        end = time.perf_counter()          # snapshot the time after it finishes
        print(f"{func.__name__} took {end - start:.4f}s")  # func.__name__ gives "process_data", not "wrapper"
        return result
    return wrapper


@timer
def process_data(n):
    return sum(range(n))   # a heavy computation — good for testing


process_data(1_000_000)
# process_data took 0.0521s
```

> `time.perf_counter()` is used instead of `time.time()` because it gives a higher-resolution measurement — better for short operations. The `:.4f` in the f-string formats the number to 4 decimal places.

---

## Practical Example — Logger

Logs every call with its arguments and return value. Useful during development to trace what's happening without scattering print statements everywhere.

```python
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)  # sets up logging to print INFO-level messages to the console

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} | args={args} kwargs={kwargs}")  # logged BEFORE the call
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")                       # logged AFTER the call
        return result
    return wrapper


@log_calls
def divide(a, b):
    return a / b


divide(10, 2)
# INFO: Calling divide | args=(10, 2) kwargs={}
# INFO: divide returned 5.0
```

> In production you'd log to a file instead of the console, but the decorator itself stays exactly the same — you'd only change the `logging.basicConfig` setup at the top.

---

## Decorators with Arguments

When you need to pass configuration into your decorator, you add **one more outer function** — making it a decorator factory.

```
@decorator            ← no arguments: just a function
@decorator(arg)       ← with arguments: a function that RETURNS a decorator
```

Why the extra layer? When you write `@retry(max_attempts=3)`, Python calls `retry(max_attempts=3)` first, which returns a decorator. That decorator then wraps your function. So you end up with three nested functions instead of two.

### Pattern

```python
def decorator_factory(arg1, arg2):   # outer: called first, receives your config
    def decorator(func):             # middle: receives the function to wrap
        @wraps(func)
        def wrapper(*args, **kwargs):
            # arg1 and arg2 are available here through closure
            return func(*args, **kwargs)
        return wrapper
    return decorator                 # outer returns the decorator, not the wrapper
```

### Example — Retry on Failure

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1.0):     # (1) outer — takes the config
    def decorator(func):                  # (2) middle — takes the actual function
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, max_attempts + 1):   # try up to max_attempts times
                try:
                    return func(*args, **kwargs)          # success — return immediately
                except Exception as e:
                    last_error = e
                    print(f"Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)                 # wait before trying again
            raise last_error                             # all attempts failed — re-raise last error
        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.5)   # retry() runs first, returns decorator, which wraps call_api
def call_api():
    import random
    if random.random() < 0.7:       # simulates a flaky API that fails 70% of the time
        raise ConnectionError("Server down")
    return "OK"


result = call_api()
```

> `last_error` is stored outside the try/except block so we can re-raise it after all attempts are exhausted. Without this, the variable `e` goes out of scope when the loop ends and you'd get a `NameError`.

### Example — Memoize (Cache Results)

```python
from functools import wraps

def memoize(func):
    cache = {}          # created once when the decorator is applied — persists across all calls

    @wraps(func)
    def wrapper(*args): # only *args here — kwargs can't be dict keys (they're not hashable)
        if args not in cache:
            cache[args] = func(*args)   # compute and store the result on first call
        return cache[args]              # return the stored result on every call after

    wrapper.cache = cache   # attach cache to the function so you can inspect it: fibonacci.cache
    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # recursive calls also hit the cache automatically


print(fibonacci(50))   # instant — without memoize, this makes ~2^50 recursive calls
```

> The `cache = {}` dict is created once when the decorator is applied — not on every function call. This is a **closure**: `wrapper` keeps a reference to `cache` even after `memoize` has finished running. That's how the cache survives between calls.

> Python ships with `@functools.lru_cache` which does the same thing and is production-ready. Prefer that in real projects.

---

## Stacking Decorators

You can apply multiple decorators to one function.

```python
@decorator_a
@decorator_b
@decorator_c
def my_func():
    pass
```

**Application order:** bottom-up — `c` wraps `my_func` first, then `b` wraps that, then `a` wraps that.  
**Execution order:** top-down — when called, `a`'s code runs first, then `b`'s, then `c`'s, then the original function.

Think of it like layers of clothing: you put on a shirt first (`c`), then a jumper (`b`), then a jacket (`a`). When someone looks at you, they see the jacket first.

### Example

```python
from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"   # wraps whatever the inner function returns in <b> tags
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"   # wraps whatever the inner function returns in <i> tags
    return wrapper


@bold           # applied second — outermost layer, runs first
@italic         # applied first — innermost layer, runs second
def greet(name):
    return f"Hello, {name}!"   # returns the raw string, italic wraps it, then bold wraps that


print(greet("Alice"))
# <b><i>Hello, Alice!</i></b>
```

> Execution trace when `greet("Alice")` is called: `bold`'s wrapper runs → calls `italic`'s wrapper → calls original `greet` → returns `"Hello, Alice!"` → `italic` wraps it in `<i>` → `bold` wraps that in `<b>` → final result printed.

---

## Quick Reference

```python
from functools import wraps

# ── Basic decorator ───────────────────────────────────────────────────────────
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def my_func():
    pass


# ── Decorator with arguments (factory pattern) ────────────────────────────────
def repeat(times=2):         # outer: takes config
    def decorator(func):     # middle: takes function
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi():
    print("Hi!")             # prints "Hi!" three times when called


# ── Stacking (bottom applies first, top runs first) ───────────────────────────
@decorator_a    # runs first when the function is called
@decorator_b    # runs second when the function is called
def my_func():
    pass
```

---

## What to Know, What to Skip

| Topic | Priority |
|---|---|
| Basic decorator structure + `@wraps` | **Essential** |
| Decorators with arguments (factory pattern) | **Important** |
| Stacking decorators | **Good to know** |
| Class-based decorators | Skip until you need stateful decorators |
| Real-world frameworks (Flask, Django) | Pick up naturally when working in those frameworks |

---

*Python standard library decorators worth knowing: `@functools.lru_cache`, `@functools.cached_property`, `@staticmethod`, `@classmethod`, `@property`*