import random
# random password using list
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]

letters_input = int(input("How many letters do you want in your password: "))
numbers_input = int(input("How many numbers do you want in your password: "))
symbols_input = int(input("How many symbols do you want in your password: "))

password = []

for letter in range(letters_input):
    # random_chosen_letter = random.choice(letters)
    password.append(random.choice(letters))

for number in range(numbers_input):
    # random_chosen_numbers = random.choice(numbers)
    password.append(random.choice(numbers))

for symbol in range(symbols_input):
    # random_chosen_symbol = random.choice(symbols)
    password.append(random.choice(symbols))

random.shuffle(password)
print(password)

final_password = ""
for char in password:
    final_password += char

print(final_password)
