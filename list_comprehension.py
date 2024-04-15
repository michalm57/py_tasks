squares = []

for i in range(1, 101):
    squares.append(i**2) 
# print(squares)

squares2 = [i**2 for i in range(1, 101)]
# print(squares2)


remainders5 = [x**2 % 5 for x in range(1, 101)]
# print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
# print(remainders11)

movies = ["Star Wars", "Ghandi", "Casablanca", "Toy Story", "Riders of the lost Arks"]
gmovies = [title for title in movies if title.startswith("G")]
# print(gmovies)



moviesWithYear = [("Star Wars", 2001), ("Ghandi", 2014), ("Casablanca", 1992), ("Toy Story", 2001), ("Riders of the lost Arks", 1992)]
pre2k = [title for (title, year) in moviesWithYear if year < 2000]
# print(pre2k)

v = [2, -3, 1]
# print(4*v)

v = [2, -3, 1]
w = [4*x for x in v]
print(w)

#cartesian product - iloczyn kartezjański
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_product = [(a, b) for a in A for b in B]
# print(cartesian_product)

names = ["Tom", "Bob", "Kat"]
l = [n[0] for n in names]
print(l)