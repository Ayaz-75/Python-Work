alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def cipher(the_text, shift_number, direct):
    end_text = ""
    if direct == 'decode':
        shift_number *= -1
    for char in the_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direct} text is: {end_text}")

cipher(text, shift, direction)
