# Prompt for a string s and a substring sub. Check if sub is present in s.

s = input("Enter the main string: ")
sub = input("Enter the substring: ")

if sub in s:
    print("The substring is present in the string.")
else:
    print("The substring is not present in the string.")
