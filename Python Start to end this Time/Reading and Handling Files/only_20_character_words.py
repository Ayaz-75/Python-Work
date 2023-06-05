
fin = open('words.txt')
count = 0
for line in fin:
    word = line.strip()
    if len(word) == 20:
        print(word)
        count += 1

print(count)
