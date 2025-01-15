# Implement the bubble sort algorithm to sort a list of numbers in ascending order.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example list
numbers = [64, 34, 25, 12, 22, 11, 90]

# Sort the list
bubble_sort(numbers)

# Print the sorted list
print("Sorted list:", numbers)
