"""
Write a function to compare two words and return True if one of the words is the
reverse of the other :

"""


def wordInverse(word1, word2):
    if word1 == word2[::-1]:
        return word2, " is inverse of ", word1
    else:
        return 0


print(wordInverse("aman", "nama"))
