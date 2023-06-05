"""
Write a function called has_no_e that returns True if the given word doesn’t have the
letter “e” in it

"""
fin = open('words.txt')
count = 0


def without_e(word):
    for letters in word:
        if letters == 'e':
            return True
    return False


print(without_e("word"))
