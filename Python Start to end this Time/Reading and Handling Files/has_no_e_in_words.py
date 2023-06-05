fin = open('words.txt')


def has_no_e():
    for line in fin:
        word = line.strip()

        # for letter in word:
        if 'e' not in word:
            print(word)


has_no_e()
