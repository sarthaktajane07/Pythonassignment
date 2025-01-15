# Write a function that returns the length of a string without using the built-in len().

def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
result = string_length("I am sarthak tajane")
print(result)  