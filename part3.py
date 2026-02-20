import random

# Create the list of numbers
numbers = []
for num in range(10):
    numbers.append(random.randint(1, 50))

largest = max(numbers)

print(numbers)
print("The largest number is:", largest)