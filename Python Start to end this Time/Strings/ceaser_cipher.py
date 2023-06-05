"""
Write a function called rotate_word that takes a string and an integer as parameters,
and returns a new string that contains the letters from the original string rotated by
the given amount.
You might want to use the built-in function ord, which converts a character to a
numeric code, and chr, which converts numeric codes to characters. Letters of the
alphabet are encoded in alphabetical order, so for

example: ord('c') - ord('a')
2

Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for
uppercase letters are different.
Potentially offensive jokes on the Internet are sometimes encoded in ROT13, which is
a Caesar cypher with rotation 13. If you are not easily offended, find and decode
some of them.

"""


def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.
    letter: single-letter string
    n: int
    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.
    word: string
    n: integer
    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))
