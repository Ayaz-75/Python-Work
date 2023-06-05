
# Searching
#  modify find so that it has a third parameter: the index in word where
# it should start looking


def find(word, letter, index):
    # index = int(input("Where should it start looking ?"))
    while index < len(word):
        if word[index] == letter:
            return letter
        index += 1
    return 'No not in word'


ind = int(input("Where should it start looking ?"))
print(find("Aaqib", 'q', index=ind))

