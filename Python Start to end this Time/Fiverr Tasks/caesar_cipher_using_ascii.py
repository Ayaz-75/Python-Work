# The program bellow returns the ascii of each character in the string

# a_string = "abc"
#
# ASCII_values = []
# for character in a_string:
#     ASCII_values.append(ord(character))
# print(ASCII_values)


# ###########################################################################################################


print("~~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to the Encryption and Decryption Program ~~~~~~~~~~~~~~~~~~~~~~~~~")

direction = input("Write encode for encryption and decode for decryption: ")
input_string = input("Enter the message: ").lower()
shift_number = int(input('Write the shifting number: '))


def encode(input_text, shifting_number):
    new_string = ''
    for char in input_text:
        new_position = ord(char) + shifting_number
        if 97 < new_position <= 123:
            shifted_chars = chr(new_position)
            new_string += shifted_chars

        else:
            new_string += char

    return new_string


def decode(input_text, shifting_number):
    new_string = ''
    for char in input_text:
        new_position = ord(char) - shifting_number
        if 97 < new_position <= 123:
            shifted_chars = chr(new_position)
            new_string += shifted_chars

        else:
            new_string += char

    return new_string


if direction == 'encode':
    print(encode(input_string, shift_number))

else:
    print(decode(input_string, shift_number))
