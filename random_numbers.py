# Importing the random module to generate random numbers
import random

# Creating a list of 100 random numbers from 0 to 1000
random_numbers = [random.randint(0, 1000) for _ in range(100)]

print("a list of 100 random numbers from 0 to 1000: ", random_numbers)

# Sorting the list from min to max without using sort()
for i in range(len(random_numbers)):
    # Find the minimum number in remaining list
    for j in range(i + 1, len(random_numbers)):
        if random_numbers[i] > random_numbers[j]:
            # Swap the found minimum element with the first element of remaining list
            random_numbers[i], random_numbers[j] = random_numbers[j], random_numbers[i]
print ("a list of 100 sorted random numbers from 0 to 1000: ", random_numbers)

# Initializing variables to calculate average
even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0

# Calculating the sum and count of even and odd numbers
for num in random_numbers:
    if num % 2 == 0:
        even_sum += num
        even_count += 1
    else:
        odd_sum += num
        odd_count += 1

# Calculating the average of even and odd numbers
even_average = even_sum / even_count
odd_average = odd_sum / odd_count

# Printing the average of even and odd numbers
print("Average of even numbers: ", even_average)
print("Average of odd numbers: ", odd_average)