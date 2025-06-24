 Number Guessing Game

Concepts used: while loop, conditions, random module

import random

secret = random.ranndit(1, 10)
guess = None

while guess != secret:
    guess = int(input("Guess a number (1-10): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Congratulations! You guessed it.")
