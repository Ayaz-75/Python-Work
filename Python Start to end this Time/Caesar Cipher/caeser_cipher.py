# a = 97
#
# for i in range(26):
#     print(chr(a))
#     a += 1
#
# print(a)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b",
            "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("--------- Welcome to the Encryption and decryption Game ----------")

direction = input("Write encode for encryption and decode for decryption: ")
text = input("Enter your message: ").lower()
shift = int(input("Enter the shifting number: "))


def encode_decode(inp_text, shift_num):
    new_string = ''
    for letters in inp_text:
        if letters in alphabet:
            position = alphabet.index(letters)
            if direction == 'encode':
                new_position = position + shift_num
                new_string += alphabet[new_position]
            else:
                new_position = position - shift_num
                new_string += alphabet[new_position]
        else:
            new_string += letters

    return new_string


print(encode_decode(text, shift))
