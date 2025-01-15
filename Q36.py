# The program should generate a random number between 1 and 10. The user guesses until they get it right.

import random

number = random.randint(1, 10)  # Generate random number between 1 and 10
guess = int(input("Guess the number between 1 and 10: "))

while guess != number:
    guess = int(input("Wrong guess. Try again: "))

print("Correct! You guessed the number.")
