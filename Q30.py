# Prompt the user for a password and print a masked version (e.g., ****** for 6 characters).

password = input("Enter your password: ")
masked_password = "*" * len(password)
print("Masked password:", masked_password)
