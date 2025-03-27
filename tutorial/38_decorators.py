import random
import time
from functools import wraps
from functools import lru_cache

def compose(f, g, x):
    return f(g(x))

compose(print, len, "Hello, world!")

# Functions in python might be nested
def random_power():
    def f(x):
        return x**2
    def g(x):
        return x**3
    def h(x):
        return x**4
    
    functions = [f, g, h]
    return random.choice(functions)



for i in range(10):
    p = random_power()
    print(p(3))

def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        stop_time = time.time()
        dt = stop_time - start_time
        print(f"^t = {dt}")
        return result
    return wrapper

# Using decorator
@timer
def prime_factorization(n):
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        
    return factors

def do_nothing(f):
    @wraps(f)
    def inner(*args, **kwargs):
        return f(*args, **kwargs)
    return inner

@do_nothing
def alpha(*args, **kwargs):
    """A function for viewing arguments."""
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')
    
@lru_cache(maxsize=None)
def fibonacci(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError(f"{n} is not a positive integer")
    
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@timer
def global_fibonacci(n):
    return fibonacci(n)
    

# alpha('a', 2, None, x=7, y=11, z=28)

# print(alpha.__name__)
# print(alpha.__doc__)

# result = prime_factorization(2**29+1)
# print(result)

# for i in range(1, 10):
#     print(fibonacci(i))

for n in range(1, 34):
    nth_term = global_fibonacci(n)
    print(f"Fibonacci({n}) = {nth_term}")