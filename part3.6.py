import random
# Create the list of numbers
numbers = []
for num in range(10):
    numbers.append(random.randint(1, 50))
print("Generated list:", numbers)

#Find the average (mean) of the numbers
sum_of_numbers = sum(numbers)
count_of_numbers = len(numbers)
average = sum_of_numbers / count_of_numbers
print("Average of the numbers:", average)

#Count how many numbers are even
even_count = 0
for value in numbers:
    if value % 2 == 0:
        even_count += 1
print("Number of even values:", even_count)

#Count how many numbers are odd
odd_count = 0
for value in numbers:
    if value % 2 == 1:
        odd_count += 1
print("Number of odd values:", odd_count)