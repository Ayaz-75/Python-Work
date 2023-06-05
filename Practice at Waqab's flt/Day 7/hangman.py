#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for _ in range(len(chosen_word)):
    display.append("_")
print(display)


end_game = False
while not end_game:
    lives = len(chosen_word)
    guess = input("Make a guess: \n").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        else:
            lives -= 1

    print(display)
    if "_" not in display:
        print(f"Yeah you won 🤩🤩🤩🤩")
        end_game = True
    elif lives < 1:
        print(f"Out of lives you lost 😭😭😭😭 !!!!")
        end_game = True
