
# word = "banana"
# new_word = input("Whats new word:? ")
#
# if new_word == word:
#     print(f"All right, bananas.!")
#
# elif new_word < word:
#     print(f'Your word, ' + new_word + f', comes before {word}.')
#
# else:
#     print(f'Your word, ' + new_word + f', comes after {word}.')


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2)
    while j > 0:
        if word1[i-1] != word2[j-1]:
            return False
        i = i + 1
        j = j - 1
    return True


print(is_reverse("aaqib", 'biqaa'))
