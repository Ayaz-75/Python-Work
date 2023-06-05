'''list_1 = ["Ayaz", "Ayoob", "Aaqib"]
for elements in list_1:
    print(elements)


list_2 = [1, 2, 3, 4]
sum_s = 0
for ints in list_2:
    squares = ints ** 2
    print(squares)

    sum_s += squares
print(sum_s)'''

'''list_3 = ["Ayoob", "Aaqib", "Ayaz"]
for names in list_3:
    if names == "Ayoob":
        print("yes")

    else:
        print("No")'''
'''should_take_input = 10
sum_s = 0
avg = 0
while should_take_input >= 1:
    user_input = int(input("Enter number: "))
    sum_s += user_input
    avg += sum_s/10
    should_take_input -= 1

print(sum_s)
print(avg)'''

'''i = 5
while i >= 1:
    print("*" * i)
    i -= 1'''
'''num = int(input("Enter the number whom table should be printed: "))
i = 1
while i <= 10:
    print(i, "X", num, "=", i*num)
    i += 1'''

'''num = int(input(" ?"))
i = 1
fact = 1
while i <= num:
    fact *= i
    i += 1

print(fact)'''


'''chosen_word = "Ayaz".lower()
dashes_list = []
for _ in range(len(chosen_word)):
    dashes_list.append("_")


# print(dashes_list)

guess = input("Guess a letter: ")
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        dashes_list[position] = letter


print(dashes_list)'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:

    direction = input("Enter encode to encrypt and decode to decrypt: ")
    text = input("Enter your message: ")
    shift = int(input("Enter shift number: "))

    if direction == "end":
        should_continue = False

    elif direction == "encode":

        def encrypt(text_m, shift_n):
            cipher_text = ""
            for letter in text_m:
                position = alphabet.index(letter)
                new_position = position + shift_n
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            print(cipher_text)


        encrypt(text, shift)

    else:
        def decrypt(text_m, shift_n):
            cipher_text_d = ""
            for letter in text_m:
                position = alphabet.index(letter)
                new_position = position - shift_n
                new_letter = alphabet[new_position]
                cipher_text_d += new_letter
            print(cipher_text_d)

        decrypt(text, shift)
