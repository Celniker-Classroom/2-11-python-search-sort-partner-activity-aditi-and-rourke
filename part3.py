import random

# Create the list of numbers
numbers = []
for num in range(10):
    numbers.append(random.randint(1, 50))

total = sum(numbers)
print(numbers)
print ("the sum of the numbers is:", total )
