# Collect string / text length

input = input("Please enter a test string: " )

if len(input) < 6:
    print("Your string is too short.")
    print("Please enter a string with at least 6 characters.")

#Prompt user to enter number / test if even or odd
second_input  = input("Please enter an integer: ")
number = int(second_input)

if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

# Scalene triangle: All sides have different lengths.
# Isosceles triangle: Two sides have the same length.
# Equilateral triangle: All sides are equal.

a = int(input("The length of side a = "))
b = int(input("The length of side b = "))
c = int(input("The length of side c = "))

if a != b and b != c and a != c:
    print("This is a scalene triangle.")
elif a == b and b == c:
    print("This is a equilateral triangle.")
else:
    print("This is an isosceles triangle.")
