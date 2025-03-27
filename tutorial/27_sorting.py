# Alkaline earth metals

earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]

earth_metals.sort(reverse=True)
print(earth_metals)

planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Jupiter", 71492, 1.33, 5.210)
]

size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)

density = lambda planet: planet[2]
planets.sort(key=density)


earth_metals2 = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
sorted_earth_metals = sorted(earth_metals2)
print(earth_metals2)
print(sorted_earth_metals)

# Tuples do not have sort method, because they are immutable and can not be changed.
data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)

# sorted() method convert Tuples to list, than sort, then return list with sorted order
print(sorted(data))

# Using sorted() methods with string
sorted("Alphabetical")
#['A', 'a', 'a', 'b', 'c', 'e', 'h', 'i', 'l', 'l', 'p', 't']