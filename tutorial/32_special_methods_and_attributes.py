class Snowflake:
    pass

flake = Snowflake()

print(dir(flake))

class Martian:
    """Someone who live on Mars."""
    
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        
    def __setattr__(self, name, value):
        print(f">>> You set {name} = {value}")
        self.__dict__[name] = value
        
    def __getattr__(self, name):
        print(f">>> Get the '{name}' attribute")
        if name == 'full_name':
            return f"{self.first_name} {self.last_name}"
        else:
            raise AttributeError(f"No attribute named {name}")
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    # Override less than
    def __lt__(self, other):
        print(f">>> Comparint {self} with {other}")
        if self.last_name != other.last_name:
            return (self.last_name < other.last_name)
        else:
            return (self.first_name < other.first_name)
            

m1 = Martian("Owen", "Phelps")
m2 = Martian("Klaus", "Iserlohn")
m1.first_name = 'Owen'
m1.last_name = 'Phelps'
m1.arrival_date = '2037-12-15'
print(m1.__dict__)
print(Martian.__doc__)
print(m2.__dict__)

m3 = Martian('Pierre', 'Aberg')
print(f"First name = {m3.first_name}")
print(f"Last name = {m3.last_name}")
print(m3.full_name)
print(m3.__str__())
print(id(m3))

m4 = Martian("Cyrille", "Collin")
m5 = Martian("Len", "Klein")
m6 = Martian("Len", "Klein")
m7 = Martian("Matthias", "Stein")
m8 = Martian("Mike", "Lenox")
m9 = Martian("Bob", "Hillier")

martians = [m4, m5, m6, m7, m8, m9]
martians.sort()
for m in martians:
    print(m)