import random

# Create the list of numbers
numbers = []
for num in range(10):
    numbers.append(random.randint(1, 50))

sorted = sorted(numbers)
print("the sorted numbers are", sorted)
