# Function that act like iterators
import string
import itertools
import sys

def g():
    yield 1 
    yield 2
    yield 3

for x in g():
    print(x)
    
# Generate the lowe case English letters
# Function that uses yield instead of "return" is called a "generator function", 
# or simply a "generator"
def letters():
    for c in string.ascii_lowercase:
        yield c
        
for letter in letters():
    print(letter)
    
def prime_numbers():
    # Handle the first prime
    yield 2
    prime_cache = [2] # Cache of primes
    
    # Loop over positive, odd integers
    for n in itertools.count(3, 2):
        is_prime = True
        
        # Check to see if any prime number divides n
        for p in prime_cache:
            if n % p == 0: # p divides n evenly
                is_prime = False
                break

        # Is it prime?
        if is_prime:
            prime_cache.append(n)
            yield n
            
for p in prime_numbers():
    print(p)
    if p > 100:
        break
    
squares = (x**2 for x in itertools.count(1))

for x in squares:
    print(x)
    
    if x > 500:
        squares.close()
        
print(sys.getsizeof(squares))
# 1 Write a function and use yield instead of return
# 2 Use a generator expression, which looks likea list comprehension with parentheses
                