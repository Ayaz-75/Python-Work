"""
Looping and Counting
The following program counts the number of times the letter a letter that appears
in a string:
"""


def loopingCounting(word, letter):
    index = 0
    count = 0
    while index < len(word):
        if word[index] == letter:
            count += 1
        index += 1
    return f"a appears {count} times in {word}"


print(loopingCounting("aaqib ali sahito", 'a'))
