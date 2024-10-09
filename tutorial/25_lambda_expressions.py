#Lambda Expressions, Anonymous functions, Something Simple the you will only use once

#Compute 3x+1
def f(x):
    return 3*x + 1

# print(f(2))

g = lambda x: 3*x + 1
print(f(2))


#Combine first name and last name into single "Full Name"
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
# print(full_name(" Josh", "EULER"))

#lambda <...args>: <returned value>

#Sort authors by last name
scifi_authors = ["Ray Bradbury", "Leigh Brackett", "Isaac Asimove"]
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)

#Quadratic Functions - Funkcje kwadratowe
def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))

val = build_quadratic_function(3, 0, 1)(2) #3x^2+1 evaluated for x=2
print(val)