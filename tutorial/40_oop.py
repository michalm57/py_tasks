# OOP - Object oriented programinng
# Define class 
class Person:
    #"dunder mothod, because of double underscore"
    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name
        self.full_name = f"{first_name} {last_name}"

    def introduction(self):
        print(f"Hello! My name is {self.full_name}. I am human... Trust me.")

    @classmethod
    def help(cls):
        print("Do you really need help, or are you just testing me?")


# Create object
p = Person("Maik", "Wagner")

# Access attributes 
print(f"First name = {p.fn}")
print(f"Last name = {p.ln}")
print(f"Full name = {p.full_name}")
p.introduction()
Person.help()

class Person:
    counter = 0 # Class attribute, number of Person objects

    def __init__(self, name):
        self.full_name = name # Instance attribute
        Person.counter += 1 # Increment the class attribute

    def introduction(self):
        print(f"Hello! My name is {self.full_name}. I am human... Trust me.")

    @classmethod
    def population(cls):
        print(f"The current population is {cls.counter}")

p1 = Person("Jeff Schroeder")
p1.introduction()
p1.population()

p2 = Person("Juergen Pichler")
p2.introduction()
Person.population()

# Monkey patching
# Attach coin attribute to p1
p1.coin = 1618033

# Attach version attribute to class 
Person.version = 1.0



