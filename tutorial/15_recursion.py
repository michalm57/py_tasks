from functools import lru_cache

# Fibonacci Sequence
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    
for n in range(1, 11):
    print(n, ":", fibonacci(n))
    
# Memoization
fibonacci_cache = {}

@lru_cache(maxsize = 1000)
def fib(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    #if we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n-1) + fib(n-2)
        
    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

# Golden ratio
for n in range(1, 51):
    print(fib(n+1) / fib(n))