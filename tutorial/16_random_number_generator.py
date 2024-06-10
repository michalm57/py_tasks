import random


for i in range(10):
    print(random.random())
    
# Generate random numbers from interval [3, 7)
def my_random():
    return 4*random.random() + 3

for i in range(10):
    print(my_random())
    
# Easiest way to generate from interval - unifrom function
for i in range(10):
    print(random.uniform(3, 7))
    
for i in range(20):
    print(random.normalvariate(0, 9))

# randint function
for i in range(20):
    print(random.randint(1, 6))
    
# Random element from a list
outcomes = ['rock', 'papers', 'scissors']

for i in range(20):
    print(random.choice(outcomes))

