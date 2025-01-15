# Find the second largest element in a list of unique integers.

# Example list of unique integers
numbers = [10, 20, 30, 40, 50]

# Find the second largest element
numbers.sort()
second_largest = numbers[-2]

# Print the result
print("Second largest element:", second_largest)
