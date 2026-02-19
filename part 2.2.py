import random

# Create the list of numbers
numbers = []
for num in range(10):
    numbers.append(random.randint(1, 50))

# Choose a random number to search for
random_number_to_search = random.randint(1, 50)

print("Generated list:", numbers)
print("Searching for number:", random_number_to_search)

comparisons = 0  # Initialize the counter for comparisons
found = False  # Variable to track if the number was found

for num in numbers:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if num == random_number_to_search:
        found = True  # Set found to True if the number is in the list
        break  # Exit the loop early if the number is found

# Print result after the search
if found:
    print(f"Number {random_number_to_search} found in the list after {comparisons} comparisons!")
else:
    print(f"Number {random_number_to_search} not found in the list after {comparisons} comparisons!")