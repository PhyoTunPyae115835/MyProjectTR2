import random

# Line 1
print(random.randint(5, 20))
# Smallest: 5, Largest: 20

# Line 2
print(random.randrange(3, 10, 2))
# Smallest: 3, Largest: 9, could not produce 4 (only odd numbers between 3 and 9)

# Line 3
print(random.uniform(2.5, 5.5))
# Smallest: 2.5, Largest: 5.5

# Random number between 1 and 100 inclusive
print(random.randint(1, 100))
