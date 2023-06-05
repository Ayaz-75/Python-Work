
# game_level = 3
# enemies = ["skeleton", "zombies", "aliens"]
# if game_level < 5:
#     new_enemy = enemies[0]
#
# print(new_enemy)
#
# def increase_enemies():
#     return enemies + 2
#
# new_enemies = increase_enemies()
# print(new_enemies)
# print(enemies)
# enemies = 1


from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



def make_guess(guess, answer, turns):
    if guess == answer:
        print(f"You got it! Number was {answer}")

    elif guess < answer:
        print(f"Too low!")
        return turns - 1

    elif guess > answer:
        print(f"Too High!")
        return turns - 1



def set_difficulty():
    difficulty = input("Choose difficulty: ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
print(f"Pssst, the correct answer is {answer}")
turns = set_difficulty()

guess = 0
while guess != answer:
    print(f"You have {turns} attempts left.")
    try:
        guess = int(input("Make Guess: "))

    except ValueError as v:
        print("☠ You haven't entered a valid number.\nTry it out with a number and Guess again. Goodbye!")
        break
    turns = make_guess(guess, answer, turns)
    if turns == 0:
        print("Sorry you are out of moves ☠ !!!")
        break

    elif guess != answer:
        print("Guess again.")













