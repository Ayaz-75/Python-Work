import random

HARD = 5
EASY = 10


def check_number(guess, answer, attempts):
    if guess > answer:
        print(f"too high \nGuess again")
        return attempts - 1
    elif guess < answer:
        print(f"too low \nGuess  again")
        return attempts - 1
    else:
        print(f"you got it number was {guess}")


def difficulty():
    level = input("Choose a difficulty level: ").lower()
    if level == 'easy':
        return EASY
    else:
        return HARD


def game():
    print(f"Welcome to the Number Guessing game !")
    print(f"I am thinking a number between 1 and 100")
    answer = random.randint(1, 100)
    # print(f"psst: {answer}")
    attempts = difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {attempts} turns left")
        guess = int(input("Make a guess: "))
        attempts = check_number(guess, answer, attempts)
        if attempts == 0:
            print(f"you run out of moves you loose! \nNumber was '{answer}'")
            return


game()
