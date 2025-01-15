# Prompt the user for 5 integers and store them in a list. Print the list and its length.

numbers = []
for _ in range(5):
    numbers.append(int(input("Enter an integer: ")))

print("List:", numbers)
print("Length of the list:", len(numbers))
