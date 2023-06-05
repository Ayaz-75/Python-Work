import random

words = ["Ayaz", "Aaqib", "Ayoob", "Zahoor"]

display = []
chosen_word = random.choice(words).lower()
for _ in range(len(chosen_word)):
    display.append("_")

lives = 6

end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(f"you are out of lives the randomly selected word was: {chosen_word}")
            end_of_game = True

    print(display)

    if "_" not in display:
        end_of_game = True
        print(f"You won the selected word was: {chosen_word}")


