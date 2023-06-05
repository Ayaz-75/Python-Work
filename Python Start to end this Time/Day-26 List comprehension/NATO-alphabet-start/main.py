
import pandas as pd


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pd.read_csv('nato_phonetic_alphabet.csv')

new_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# print(new_dictionary)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

guessed_word = input("Enter a Word: ").upper()

phonetic_list = [new_dictionary[letter] for letter in guessed_word]

print(phonetic_list)

