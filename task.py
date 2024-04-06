print("Hello World!")

#incremantation
#z++, z-- do not exists
z = 1
z += 1

#string Interpolation
placeName = "Jungle"
text = f"Welcome to the {placeName}"
print(text)

#logical operators
print(True and False)
print(True or False)
print(not True or False)

#long text """
longText = """ Long
    text
example is example"""
print(longText)

#string methods
text = 'This is exampLe string! '
print(text.upper())
print(text.capitalize())
print(text.lower())
print(text.strip())
print(text.startswith("t"))
print(text.lower().startswith("t"))
print(text.replace("string", "test"))
print(text.split(" "))

#string slicing
text = 'Another example string'
print(text[0:3])
print(text[1:])
print(text[1:-1])
print(text[:-1])
print(text[-1:])
print(len(text))

#dynamically and strongly typed
def add(a, b):
    print(a + b)
a = 2 
b = 3 
c = 'test'
d = '1'
d = int(d)

add(a, b)
add(str(a), c)
print(type(a))
print(type(c))
print(type(d))


