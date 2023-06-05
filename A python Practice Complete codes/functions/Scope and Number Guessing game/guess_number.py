from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Let the user guess a number.
        guess = int(input("Make a guess: "))

        #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()

















#
#
# guess = 0
# def game():
#     while guess != chosen_number:
#         guess = int(input("Make Guess: "))
#         make_guess(guess, chosen_number, turns)
#
#
# game()
# attempts = 10
# def decrease_enemies():
#     return attempts - 1


# print(decrease_enemies()
#
# def make_guess(guess, answer, turns):
#     if guess == answer:
#         print(f"You got it! the number was {chosen_number}")
#     elif guess < answer:
#         print(f"Too Low! \nGuess again")
#         return turns - 1
#     elif guess > answer:
#         print(f"Too High! \nGuess again")
#         return turns - 1
#
# print("Welcome to the Number guessing game 🙋‍")
# print("I am thinking a number between 1 and 100.")
#
# chosen_number = random.randint(1, 100)
# print(f"Chosen_number: {chosen_number}")
#
# level = input("Choose the difficulty level: ").lower()
#
# should_end = False
# while not should_end:
#     turns = set_difficulty()
#     print(f"You have {turns} attempts left")
#
#     guess = int(input("Make a Guess: "))
#     make_guess(guess, chosen_number, turns)
#
#     if guess == chosen_number:
#         should_end = True
#     if turns == 0:
#         should_end = True


#
# def choose_difficulty():
#     global attempts
#     if difficulty == "hard":
#         attempts = HARD
#     elif difficulty == "easy":
#         attempts = EASY
#     else:
#         print("!!!!! Invalid difficulty level!")
#
#     return attempts
#
#
# def make_guess():
#     guess = int(input("Make a guess: "))
#     if guess == chosen_number:
#         print(f"You got it! the number was 👉 {chosen_number}")
#     elif guess < chosen_number:
#         print(f"Too low!\nGuess again")
#         return f"You have {attempts -1} attempts remaining to guess the number."
#     elif guess > chosen_number:
#         print(f"Too high!\nGuess again")
#         return f"You have {attempts -1} attempts remaining to guess the number."
#
#
#
# choose_difficulty = choose_difficulty()
# should_end = False
# while not should_end:
#     make_guess()
#     if attempts <= 0:
#         should_end = True
#         print("Goodbye!")


