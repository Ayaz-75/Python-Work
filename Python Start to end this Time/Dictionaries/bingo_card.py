''''
Exercise 146: Create a Bingo Card

A Bingo card consists of 5 columns of 5 numbers which are labelled with the letters
B, I, N, G and O. There are 15 numbers that can appear under each letter. In particular,
the numbers that can appear under the B range from 1 to 15, the numbers that can
appear under the I range from 16 to 30, the numbers that can appear under the N
range from 31 to 45, and so on.

Write a function that creates a random Bingo card and stores it in a dictionary. The
keys will be the letters B, I, N, G and O. The values will be the lists of five numbers
that appear under each letter.

Write a second function that displays the Bingo card
with the columns labelled appropriately. Use these functions to write a program that
displays a random Bingo card. Ensure that the main program only runs when the file
containing your solution has not been imported into another program.

'''

import random


cards = {
    "B":[random.randint(1,  15) for i in range(5)],
    "I":[random.randint(16, 30) for i in range(5)],
    "N":[random.randint(31, 45) for i in range(5)],
    "G":[random.randint(46, 60) for i in range(5)],
    "O":[random.randint(61, 75) for i in range(5)]
}

for key in cards:
    print(key, cards[key])

