# Write an iterative binary search function to find an element in a sorted list.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Element found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Focus on the right half
        else:
            high = mid - 1  # Focus on the left half
    return -1  # Element not found

# Example sorted list
numbers = [1, 3, 5, 7, 9, 11, 13, 15]

# Search for the element
target = int(input("Enter the number to search for: "))
result = binary_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")
