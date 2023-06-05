




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+',
            '/','`', ':', ';', '.', ',', '}', '{']
def encrypt(plain_text, shift):
    cipher = ""
    for letter in plain_text:
        if letter == " ":
            cipher += " "
        else:
            position = alphabet.index(letter)
            new_position = position + shift
            cipher += alphabet[new_position]
    print(f"Plain text was: {plain_text}\nEncrypted text is: {cipher}")

def decrypt(plain_text, shift):
    cipher = ""
    for letter in plain_text:
        if letter == " ":
            cipher += " "
        else:
            position = alphabet.index(letter)
            new_position = position - shift
            cipher += alphabet[new_position]
    print(f"Encrypted text was: {plain_text}\nDecrypted text is: {cipher}")





should_continue = True
while should_continue:
    choice = input("What do you want to do ? type 'encode' for encryption and 'decode' for decryption\n")
    if choice == "encode":
        text_to_encrypt = input("Enter the text to be encrypted: \n")
        shift_number = int(input("Enter the number text should shifted to: \n"))
        encrypt(text_to_encrypt, shift_number)

    elif choice == "decode":
        text_to_decrypt = input("Enter the text to be decrypted: \n")
        shift_number = int(input("Enter the number text should shifted to: \n"))
        decrypt(text_to_decrypt, shift_number)

    else:
        should_continue = False
        print("Good bye!")
        print()
