# Prompt for principal, rate, and time to calculate simple interest.

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print(f"Simple Interest: {si}")
