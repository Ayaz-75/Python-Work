prefixes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
suffix = 'ack'

for letters in prefixes:
    if letters == 'O' or letters == 'Q':
        letters += 'u'
    # print(letters + suffix)

s = 'Monty Python'

length = len(s)

print(s[:])
print(s[6:12])
