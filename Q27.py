# Prompt for a string and replace all occurrences of a specific character with another.

s = input("Enter a string: ")
old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")

result = s.replace(old_char, new_char)
print("Updated string:", result)
