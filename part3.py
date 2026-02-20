import random

# Create the list of numbers
numbers = []
for num in range(10):
    numbers.append(random.randint(1, 50))

smallest = min(numbers)

print(numbers)
print("The smallest number is:", smallest)