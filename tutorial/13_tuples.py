import sys
import timeit

# Smaller and faster alternative for lists

# List example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple example
perfect_squares = (1, 4, 9, 16, 25, 35)

# Display lengths
print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfect_squares))

# Iterate over both sequences
for p in prime_numbers:
    print("Prime: ", p)
    
for n in perfect_squares:
    print("Square: ", n)
    
# List occupied more memory than tuples
# Compare size of lists and tuples
list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)
print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

empty_list_eg = []
empty_tuple_eg = ()
print("List size = ", sys.getsizeof(empty_list_eg))
print("Tuple size = ", sys.getsizeof(empty_tuple_eg))

# In lists you can add data, remove data, change data
# Tuples cannot be changed, Immutable

list_test = timeit.timeit(stmt="[1,2,3,4,5]",
                          number=1000000)


tuple_test = timeit.timeit(stmt="(1,2,3,4,5)",
                          number=1000000)

# It's took much more time to create 1000000 lists than a tuples
print("List time: ", list_test)
print("List time: ", tuple_test)

empty_tuple = ()
test = ("a",)
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test)
print(test2)
print(test3)

# Another way to create tuples
testEg = 1,
testEg1 = 1, 2
testEg2 = 1, 2
testEg3 = 1, 2, 3
print(testEg)
print(testEg1)
print(testEg2)
print(testEg3)

# Tuple Assigment
# (age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

# Another way of assigment
survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2


