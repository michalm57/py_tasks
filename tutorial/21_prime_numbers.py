# Prime Number: Positive intiger only divisible by itself and 1
import time
import math

def is_primve_v1(n):
    """Return True if n is a prime number. False otherwise."""
    if n <= 1:
        return False # 1 is not prime
    
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def is_primve_v2(n):
    """Return True if n is a prime number. False otherwise."""
    if n <= 1:
        return False # 1 is not prime
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

def is_primve_v3(n):
    """Return True if n is a prime number. False otherwise."""
    if n <= 1:
        return False # 1 is not prime

    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True


# ==== Time Function ====
t0 = time.time()
for n in range(1, 10000):
    is_primve_v3(n)
t1 = time.time()
print("Time required: ", t1 - t0)

# Results for 10000 numbers:
# is_prime_v1(): Time required:  0.40436267852783203
# is_prime_v2(): Time required:  0.01023244857788086
# is_prime_v3(): Time required:  0.007283449172973633