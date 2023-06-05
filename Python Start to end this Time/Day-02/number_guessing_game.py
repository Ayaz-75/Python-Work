'''
EXERCISE 1: ```Number guessing game```
---> Then ask the user to guess what number has been chosen.
---> Each time the user enters a guess, the program indicates one of the following:
– Too high
– Too low
– Just right
---> If the user guesses correctly, the program exits. Otherwise, the user is asked to
try again.
---> The program only exits after the user guesses correctly.

'''

from numpy import random


computer_choice = random.randint(100)

attempts = 10

should_continue = True

while should_continue:
    user_input = int(input("Enter the Number: "))

    if user_input < computer_choice:
        print("Too Low")

    elif user_input > computer_choice:
        print("Too High")

    else:
        print(f"You got it number was: {computer_choice}")
        should_continue = False

    attempts -= 1

    if attempts == 0:
        should_continue = False
        print("You Loose you ran out of moves")
