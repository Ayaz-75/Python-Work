
"""
prints all the letters from word1 that also appear in word2:

"""


def in_both(word1, word2):
    word = ""
    for letters in word1:
        if letters in word2:
            print(letters)
            word += letters
    print(word)


in_both("apples", 'oranges')

