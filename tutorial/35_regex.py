# ^Fran - to match the start of the string
# i$ - to match the end of the string
# \d - to match a numerical digit
# \s - to match space
# \w - any letter, digit and underscore
# ^\w\w\w\w\s
# [aeiou]{2} - two vowels in one word
# ^\w{7}$ - string that have 7 characters
import re

names = [
    'Finn Bindeballe',
    'Geir Anders Berge',
    'HappyCodingRobot',
    'Ron Cromberge',
    'Sohil',
]

# Find people with first and last name only
regex = '^\w+\s+\w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(name)

# Search for word char sequence starting with C
regex = 'C\w*'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)
        print(match.start())
        print(match.end())
        print(match.span())
        print(match.group()) # Return substring that match the regex

names = [
    'Brian Daugette',
    'Veronica Supersonica',
    'Tony Gasparovic',
    'Patrick Germann',
    'm!sha',
]

# Test for first name and last name
# a groups is a way to identify and even name a part of the regex pattern
regex = '^(?P<fn>\w+)\s+(?P<ln>\w+)$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(name)
        print(result.group('fn'))
        print(result.group('ln'))
     
# Detect last name
regex = '^[a-zA-Z!]+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(name)
        
# Scan for blocks of lower case letters
regex = '[a-z]+'
for name in names:
    matches = re.findall(regex, name)
    if matches:
        print(matches)
        


values = [
    'https://www.test.com',
    'com.test.de',
    'file://test.tst.ts'
    'http://www.krr.test'
]

# Test if string starts with https
regex = 'https?'
for value in values:
    if re.match(regex, value):
        print(value)
        
regex = 'https?://w{3}.\w+.(org|com)'
for value in values:
    if re.fullmatch(regex, value):
        print(value)
