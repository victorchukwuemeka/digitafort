"""
# Python Decorators: Comprehensive In-Depth Guide

This file provides an exhaustive, production-grade guide to mastering
Python Decorators. It covers core syntax, function wrappers, *args/**kwargs
handling, syntactic sugar, practical real-world application, edge cases,
and common pitfalls.
"""

# --- 0. Setup / Initial State ---
import time
import functools

print("=" * 70)
print("  PYTHON DECORATORS — COMPREHENSIVE MASTERCLASS")
print("=" * 70)

# =====================================================================
print("\n--- 1. Functions Are First-Class Objects ---")
# =====================================================================
# In Python, functions are objects. They can be assigned to variables,
# passed as arguments, and returned from other functions.

def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"

# Assign function to a variable (no parentheses = no invocation)
say_hello = greet

print(f"greet('Alice')     -> {greet('Alice')}")
print(f"say_hello('Alice') -> {say_hello('Alice')}")
print(f"greet is say_hello -> {greet is say_hello}")


# =====================================================================
print("\n--- 2. Higher-Order Functions ---")
# =====================================================================
# A higher-order function accepts or returns another function.
# Decorators exploit both properties.

def create_multiplier(factor):
    """Returns a new function that multiplies by `factor`."""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
print(f"double(5) -> {double(5)}")
print(f"triple(5) -> {triple(5)}")


# =====================================================================
print("\n--- 3. Closures — The Engine Behind Decorators ---")
# =====================================================================
# A closure is an inner function that captures variables from its
# enclosing scope even after the outer function has returned.

def outer(message):
    def inner():
        print(f"  Closure captured: '{message}'")
    return inner

my_closure = outer("I persist beyond the outer call!")
my_closure()
print(f"  Free variables: {my_closure.__code__.co_freevars}")


# =====================================================================
print("\n--- 4. Building Your First Decorator (Manual Application) ---")
# =====================================================================
# A decorator: (1) takes a function, (2) wraps it, (3) returns the wrapper.

def simple_logger(func):
    """Logs entry and exit of a function."""
    def wrapper():
        print(f"  [LOG] Calling '{func.__name__}'...")
        result = func()
        print(f"  [LOG] '{func.__name__}' returned: {result}")
        return result
    return wrapper

def say_goodnight():
    return "Goodnight, Moon!"

# Manual decoration
say_goodnight = simple_logger(say_goodnight)
returned = say_goodnight()
print(f"  Final returned value: {returned}")


# =====================================================================
print("\n--- 5. The @ Syntactic Sugar ---")
# =====================================================================
# @decorator above a def is shorthand for: func = decorator(func)

def uppercase_result(func):
    """Converts the return value to uppercase."""
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_result
def make_greeting():
    return "hello from the decorated function"

print(f"make_greeting() -> {make_greeting()}")


# =====================================================================
print("\n--- 6. Handling Arguments with *args and **kwargs ---")
# =====================================================================
# Real functions accept arguments. The wrapper must forward ALL
# positional (*args) and keyword (**kwargs) arguments transparently.

def timer(func):
    """Measures execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  ⏱ '{func.__name__}' took {elapsed:.6f}s")
        return result
    return wrapper

@timer
def compute_sum(n):
    """Sum integers from 0 to n-1."""
    return sum(range(n))

@timer
def greet_person(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(f"compute_sum(1_000_000) -> {compute_sum(1_000_000)}")
print(f"greet_person('Bob', greeting='Hey') -> {greet_person('Bob', greeting='Hey')}")


# =====================================================================
print("\n--- 7. Preserving Metadata with functools.wraps ---")
# =====================================================================
# Without @functools.wraps, the decorated function loses its original
# __name__, __doc__, etc. This breaks introspection and debugging.

def smart_logger(func):
    @functools.wraps(func)   # <-- copies func's metadata onto wrapper
    def wrapper(*args, **kwargs):
        print(f"  [SMART LOG] Calling '{func.__name__}'")
        return func(*args, **kwargs)
    return wrapper

@smart_logger
def add(a, b):
    """Return the sum of a and b."""
    return a + b

print(f"add.__name__ -> '{add.__name__}'")   # 'add', not 'wrapper'
print(f"add.__doc__  -> '{add.__doc__}'")
print(f"add(10, 20)  -> {add(10, 20)}")


# =====================================================================
print("\n--- 8. Decorator Factories (Decorators with Arguments) ---")
# =====================================================================
# To parameterise a decorator, add a third nesting level:
#   Level 1: factory(args)  — accepts decorator config
#   Level 2: decorator(func) — accepts the function
#   Level 3: wrapper(*args) — accepts the function's arguments

def repeat(n=2):
    """Decorator factory: calls the decorated function n times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                print(f"  [repeat] Execution {i + 1}/{n}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(n=3)
def announce(msg):
    print(f"    📢 {msg}")

announce("Decorators are powerful!")


# =====================================================================
print("\n--- 9. Stacking Multiple Decorators ---")
# =====================================================================
# Multiple decorators are applied bottom-up but execute top-down.

def bold(func):
    @functools.wraps(func)
    def wrapper(*a, **kw):
        return f"<b>{func(*a, **kw)}</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*a, **kw):
        return f"<i>{func(*a, **kw)}</i>"
    return wrapper

@bold      # outer
@italic    # inner (applied first)
def styled(text):
    return text

# Result: bold(italic(styled)) => <b><i>text</i></b>
print(f"styled('Stacked!') -> {styled('Stacked!')}")


# =====================================================================
print("\n--- 10. Class-Based Decorators ---")
# =====================================================================
# Any callable works as a decorator. A class with __call__ qualifies.

class CallCounter:
    """Counts how many times a function is called."""
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"  [CallCounter] '{self.func.__name__}' called {self.count}x")
        return self.func(*args, **kwargs)

@CallCounter
def say_hi(name):
    return f"Hi, {name}!"

print(say_hi("Alice"))
print(say_hi("Bob"))
print(f"Total calls: {say_hi.count}")


# =====================================================================
print("\n--- 11. Real-World: Access Control Decorator ---")
# =====================================================================

def require_role(role):
    """Restrict function access by user role."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                print(f"  ⛔ DENIED: {user['name']} (role={user.get('role')})")
                return None
            print(f"  ✅ GRANTED: {user['name']}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_database(user):
    return f"Database deleted by {user['name']}"

admin = {"name": "SuperAdmin", "role": "admin"}
viewer = {"name": "Joe", "role": "viewer"}
print(f"  Result: {delete_database(admin)}")
print(f"  Result: {delete_database(viewer)}")


# =====================================================================
print("\n--- 12. Real-World: Memoization / Caching ---")
# =====================================================================

def memoize(func):
    """Cache results based on arguments."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"  [HIT]  {func.__name__}{args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        print(f"  [MISS] {func.__name__}{args} = {result}")
        return result
    wrapper.cache = cache
    return wrapper

@memoize
def fib(n):
    """Nth Fibonacci number."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(f"fib(10) = {fib(10)}")
print(f"Cache entries: {len(fib.cache)}")


# =====================================================================
print("\n--- 13. Common Pitfalls ---")
# =====================================================================

# Pitfall 1: Forgetting functools.wraps
def broken(func):
    def wrapper(*a, **kw):
        return func(*a, **kw)
    return wrapper

@broken
def my_func():
    """Important docstring."""
    pass

print(f"Without @wraps: name='{my_func.__name__}', doc='{my_func.__doc__}'")
print("Always use @functools.wraps to preserve metadata!")


print("\n" + "=" * 70)
print("  End of Python Decorators Explanation")
print("=" * 70)
