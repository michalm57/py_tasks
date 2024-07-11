# List: [1, 2, "a", 3.14]
# List Comprehensions: [<expr for each term in the list> for val in collection]
# List Comprehensions: [expr for val in collection if <test>]
# List Comprehensions: [expr for val in collection if <test> and <test2>]
# List Comprehensions: [expr for val1 in collection1 if and val2 in collection2]
# Example 1: List of squares
squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)

# Example 2: List Comprehension
squares2 = [i**2 for i in range(1, 101)]
print(squares2)

# Example 2: List Comprehension - more complex example
remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)

# All movies that starts with G
movies = ["Star Wars", "Ghandi", "Casablanca", "Toy Story", "Riders of the lost Arks", "Ghostbusters"]
gmovies = [title for title in movies if title.startswith("G")]
print(gmovies)

# All movies that was released before 2000
moviesWithYear = [("Star Wars", 2001), ("Ghandi", 2014), ("Casablanca", 1992), ("Toy Story", 2001), ("Riders of the lost Arks", 1992)]
pre2k = [title for (title, year) in moviesWithYear if year < 2000]
print(pre2k)

# Cartesian Product (A X B)
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesianProduct = [(a, b) for a in A for b in B]
print(cartesianProduct)