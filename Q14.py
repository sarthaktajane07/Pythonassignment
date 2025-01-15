# Given a string, count how many vowels (a, e, i, o, u) it contains.

s = input("Enter a string: ")
vowels = "aeiou"
count = sum(1 for char in s if char.lower() in vowels)
print("Number of vowels:", count)

