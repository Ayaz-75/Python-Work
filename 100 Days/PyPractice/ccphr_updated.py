# welcome to the caesar cipher program part 1
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]
should_continue = True
while should_continue:
    direction = input("type 'encode' to encrypt and 'decode' to decrypt \n")

    text = input("enter your message: \n").lower()
    shift = int(input("type shift number: "))
    shift = shift % 26


    def caesar(test_text, test_shift, test_direction):
        cipher_text = ""
        for char in test_text:
            if char in alphabet:
                position = alphabet.index(char)
                if test_direction == 'encode':
                    new_position = position + test_shift
                elif test_direction == 'decode':
                    new_position = position - test_shift
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += char
        print(f"The updated text is: {cipher_text}")


    caesar(test_text=text, test_shift=shift, test_direction=direction)
    choice = input("do you want to continue type 'y' to continue and 'n' to exit: ")
    if choice == "y":
        should_continue = True
    elif choice == "n":
        should_continue = False
        print("Goodbye")
