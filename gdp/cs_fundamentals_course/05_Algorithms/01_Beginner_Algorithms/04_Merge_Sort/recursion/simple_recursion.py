# The simplest examples of recursion.

# Example 1: Countdown
# The function calls itself with a smaller number until it reaches 0.
def countdown(n):
    print(n)
    if n == 0:
        return            # base case: stop
    countdown(n - 1)      # recursive step: get closer to 0

countdown(5)


# Example 2: Factorial (n!)
# 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    if n <= 1:
        return 1          # base case: 0! = 1! = 1
    return n * factorial(n - 1)   # recursive step: n * (n-1)!

print(factorial(5))       # 120


# The SAME two problems, but with normal loops (iteration).
# Compare each one with its recursive version above.

# Example 1: Countdown with a loop
def countdown_loop(n):
    while n >= 0:
        print(n)
        n -= 1

countdown_loop(5)


# Example 2: Factorial with a loop
# Start from 1 and multiply up to n.
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial_loop(5))  # 120
