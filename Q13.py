# Demonstrate various string slicing operations (e.g., reverse a string, skip letters).

s = input("Enter a string: ")

# Reverse the string
print("Reversed:", s[::-1])

# Skip every second letter
print("Skip every second letter:", s[::2])

# Skip every second letter in reverse
print("Skip every second letter in reverse:", s[::-2])

# Get a substring from index 1 to 4
print("Substring (1 to 4):", s[1:5])

# Get substring from index 2 to the end
print("Substring (from index 2):", s[2:])

