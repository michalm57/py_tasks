# Text Files: Plain Text, XML, JSON, Source Code
# Binary Files: Compiled code, App data, Media files (~images, ~audio, ~video)
f = open("text_files/guido_bio.txt")
text = f.read()
f.close()
print(text)
with open("text_files/guido_bio.txt") as fobj:
    bio = fobj.read()

try:
    with open("future.txt") as f:
        text = f.read()
except FileNotFoundError:
    text = None
print(text)

# How to write to files
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("text_files/oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")

# Open file in append mode
with open("text_files/oceans.txt", "a") as f:
    print(23*"=", file=f)
    print("These are the 5 oceans.", file=f)

