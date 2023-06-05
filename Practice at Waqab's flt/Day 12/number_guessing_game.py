import random

print(f"\n\n-----------------------Welcome to the number Guessing Game-----------------------\n\n")
print("I am thinking a number between 1 and 50.")
random_number = random.randint(1, 20)
print(f"Number is: {random_number}")

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def set_difficulty():
    level = input("Choose difficulty: type 'easy' or 'hard': ").lower()

    if level == 'hard':
        return HARD_ATTEMPTS
    else:
        return EASY_ATTEMPTS


def check_answer(user_guess, number, turns):
    if user_guess < number:
        print("Too low !!!!!!!")
        return turns - 1

    elif user_guess > number:
        print("Too high !!!!")
        return turns - 1

    else:
        print(f"You got it !!!!!!! number was {random_number}")

turns = set_difficulty()
guess = 0

is_game_over = False

while guess != random_number and turns > 0:
    print(f"You have {turns} attempts left.")
    guess = int(input("Make a guess: "))
    check_answer(guess, random_number, turns)
    turns -= 1
    if turns < 1:
        print("You are out of moves !!!!!!!")
        is_game_over = True
