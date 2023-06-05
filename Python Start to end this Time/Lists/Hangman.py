import random
print(f"Welcome to the Hangman Game")
word_list = ['aardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)


display = []


for letter in chosen_word:
    display.append("_")
print(display)

while "_" in display:
    guess = input("Make a guess: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

print("You won")
