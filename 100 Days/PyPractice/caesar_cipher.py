# welcome to the caesar cipher program part 1
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z", ]

direction = input("type 'encode' to encrypt and 'decode' to decrypt \n")

text = input("enter your message: \n").lower()
shift = int(input("type shift number: "))


def encrypt(test_text, test_shift, ):
    cipher_text = ""
    for letter in test_text:
        position = alphabet.index(letter)
        new_position = position + test_shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}")
    # return cipher_text


def decrypt(test_text, text_shift):
    cipher_text = ""
    for letter in test_text:
        position = alphabet.index(letter)
        new_position = position - text_shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"Th decoded text is: {cipher_text}")


if direction == "encode":
    encrypt(test_text=text, test_shift=shift)
elif direction == "decode":
    decrypt(test_text=text, text_shift=shift)
