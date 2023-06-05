import random

HARD = 5
EASY = 10


words = ["apple", "baboon", "camel", "donkey", "eye"]

chosen_word = random.choice(words)
print(f" fshdkuf:  {chosen_word}")

display = []
for letter in chosen_word:
    display.append("_")

# print(display)
# guess = input("Guess a letter: \n")
# for letter in chosen_word:
#     if letter == guess:
#         print("right")
#     else:
#         print("wrong")


print()
print()
should_end = False

difficulty = input("Choose the difficulty level: \n").lower()

if difficulty == "hard":
    lives = HARD

else:
    lives = EASY

print(display)
print()
print()

while not should_end:
    guess = input("Guess a letter: \n")
    lives -= 1
    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    print(display)
    print(f"\n\nYou got it the word was {chosen_word}")
    if lives == 0:
        should_end = True
        print("You are out of lives")

    if "_" not in display:
        should_end = True

