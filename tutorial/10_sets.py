example = set()
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")
# {False, 42, 3.14159, 'Thorium'} new order

example.add(42)
# {False, 42, 3.14159, 'Thorium'} Existing value is not added
len(example) # length of set

example.remove(42)

# example.remove(52) # Returns KeyError: 52

# discard if the element is not a member, do nothing
example.discard(50)

example2 = set([28, True, 2.71828, "Helium"])
example2.clear() # Has become the empty set

# Evaluate union, and intersections of two sets
# Union = A u B
# Intersections A n B
# Integers 1 - 10
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composities = set([4, 6, 8, 9, 10]) # Integers that can be factored

odds.union(evens)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(odds.intersection(primes))
# {3, 5, 7}

print(evens.intersection(primes))
# {2}

2 in primes
# True

9 not in evens
# True