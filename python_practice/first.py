# Define a generator function to generate a sequence of numbers
def number_generator(n):
    for i in range(1, n + 1):
        yield i

# Calculate the sum of numbers using the generator
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Generate numbers from 1 to 1,000,000 using the generator
numbers = number_generator(10_00_00_00_000)

# Calculate and print the sum without loading all numbers into memory
result = calculate_sum(numbers)
print("Sum of numbers:", result)
