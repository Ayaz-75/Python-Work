import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_number(user_guess, selected_number, attempts):
    if user_guess > selected_number:
        print("too high \nGuess again")
        return attempts - 1

    elif user_guess < selected_number:
        print("too low \nGuess Again")
        return attempts - 1
    else:
        print(f"You got it the number was {user_guess}")


def set_difficulty():
    level = input("Choose a difficulty level: ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print(f"Welcome to the number guessing game!")
    print(f"I am thinking a number between 1 and 100")

    selected_number = random.randint(1, 100)
    print(f"pssts: {selected_number}")

    attempts = set_difficulty()

    user_guess = 0
    while user_guess != selected_number:
        print(f"you have {attempts} attempts remaining")
        user_guess = int(input("Make a Guess: "))
        attempts = check_number(user_guess, selected_number, attempts)
        if attempts <= 0:
            print(f"You loose! you are out of moves ")
            return


game()
