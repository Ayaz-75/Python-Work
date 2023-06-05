

print('''
 ____   ____   ____   ____   ____  _____     ____  _ _____  _   _  ____ _____ 
/ (__` / () \ | ===| (_ (_` / () \ | () )   / (__`| || ()_)| |_| || ===|| () )
\____)/__/\__\|____|.__)__)/__/\__\|_|\_\   \____)|_||_|   |_| |_||____||_|\_\                                             
''')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


should_continue = True
while should_continue:

    direction = input("Enter encode to encrypt and decode to decrypt: ")

    if direction == "end":
        should_continue = False
        print("Goodbye")
        break

    elif direction == "encode":
        text = input("Enter your message: ")
        shift = int(input("Enter shift number: "))

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
        text = input("Enter your message: ")
        shift = int(input("Enter shift number: "))

        def decrypt(text_m, shift_n):
            cipher_text_d = ""
            for letter in text_m:
                position = alphabet.index(letter)
                new_position = position - shift_n
                new_letter = alphabet[new_position]
                cipher_text_d += new_letter
            print(cipher_text_d)

        decrypt(text, shift)
