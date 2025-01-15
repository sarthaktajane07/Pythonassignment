# Prompt for principal, rate, and time to calculate compound interest.

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
a = p * (1 + r / 100) ** t
ci = a - p
print(f"Compound Interest: {ci}")

