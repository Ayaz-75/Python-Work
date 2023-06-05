'''
Exercise 10-11.

Two words are a “reverse pair” if each is the reverse of the other. Write a program that
finds all the reverse pairs in the word list.

'''

fin = open('words.txt')


def reverse_pair():
    count = 0
    for line in fin:
        word = line.strip()
        if word == word[::-1]:
            count += 1
            print(word, word[::-1])
    return count


print(reverse_pair())
