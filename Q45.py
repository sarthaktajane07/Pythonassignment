# Given a dictionary, invert it (keys become values, values become keys).

n = int(input("Enter a number: "))

squares_dict = {x: x**2 for x in range(1, n + 1)}

print("Dictionary of squares:", squares_dict)
