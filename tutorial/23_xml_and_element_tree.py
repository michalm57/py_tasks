import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

# Display classes in ET module
for (name, member) in getmembers(ET, isclass):
    if not name.startswith("_"):
        print(name)

# Display functions in ET module
for (name, member) in getmembers(ET, isfunction):
    if not name.startswith("_"):
        print(name)

# XML - Extensible Markup Language - Tree of Elements
# In XML each node, other than a root has a single parent
# Each node can have 0 or more children

tree = ET.parse('hodlers.xml')
root = tree.getroot()
print(ET.tostring(root))

# Get 'coin' attribute
coin = root.get('coin')
print("Crypto name = {val}".format(val = coin))

# Set 'launched' attribute
root.set('launched', '20210101')
print(root.attrib)

# Add 'id' attribute to each investor
id = 1
for investor in tree.findall('investor'):
    investor.set('id', str(id))
    id += 1

tree.write('hodlers.xml')

# Delete 'id' attributes
for investor in tree.findall('investor'):
    del(investor.attrib['id'])
    
# Add investor #1
investor1 = ET.fromstring("<investor>Allen Duffy</investor>")
root.append(investor1)

# Add investor #2
investor2 = ET.Element("investor")
investor2.text = "Karl Amber"
root.append(investor2)

# Add ids once more
for (id, investor) in enumerate(root.findall('investor')):
    investor.set('id', str(id))

# Select investor 4
investor = root.find(".//investor[@id='4']")
print(investor.text)

# Save updated XML
tree.write('hodlers.xml')