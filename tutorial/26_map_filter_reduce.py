import math
import statistics
from functools import reduce

radii = [2, 5, 7.1, 0.3, 10]

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

# Method 1: Direct method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)
    
print(areas)

# Method 2: Use 'map' function
map(area, radii)
list(map(area, radii))

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)
list(map(c_to_f, temps))

# Filter Function
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

filter(lambda x: x > avg, data)

# Values above average
print(list(filter(lambda x: x > avg, data)))

# Values below average
print(list(filter(lambda x: x < avg, data)))

# Remove missing data
countries = ["", "Argentina", "Brazil", "Chile", "", "Colombia", "", "", "Ecuador", "", "Venezuela"]
print(list(filter(None, countries)))

# Python false values - "", 0, 0.0, 0j, [], (), {}, False, None, instances which signal they are empty

# Reduce function 
# Multiply all numbers in a list
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y

reduce(multiplier, data)

# Use for loop instead of reduce function
product = 1
for x in data:
    product = product * x

print(product)