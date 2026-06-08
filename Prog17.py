#Number Guessing Game – Provide hints until the correct guess
import random
n= random.randint(1, 100)
while True:
    g= int(input("Guess a number between 1 and 100: "))
    if g < n:
        print("Too low! Try again.")
    elif g > n:
        print("Too high! Try again.")
    else:
        print("Congratulations!!!! You guessed the number.")
        break