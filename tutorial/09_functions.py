import math

def f():
    pass # skip this line and do nothing

def ping():
    return "Ping!"

x = ping()

# Volume of the sphere
def volume(r):
    """Return the volume of a sphere with radius r."""
    v = (4.0/3.0) * math.pi * r**3
    return v
volume(4)

# Compute area of the triangle
def triangle_area(b, h):
    """Return the area of a triange with base b and height h."""
    return 0.5 * b * h

triangle_area(3, 6)

# Keyword Arguments 
# 1 inch = 2.54 cm
# 1 foot = 12 inches
def cm(feet = 0, inches = 0):
    """"Converts a length from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

cm(1)
cm(inches = 8, feet = 5)

def g(y, x = 0):
    return x + y



