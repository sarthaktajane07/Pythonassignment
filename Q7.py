# Prompt the user for three numbers and determine which one is the largest.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(f"The largest number is: {a}")
elif b > c:
    print(f"The largest number is: {b}")
else:
    print(f"The largest number is: {c}")
