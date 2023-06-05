'''
Exercise 138: Text Messaging
On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it, multiple key presses are
needed for most letters. Pressing the number once generates the first character listed
for that key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth
or fifth character.

                       Key   Symbols
                       ______________
                      | 1   | .,?!:  |
                      | 2   | A B C  | 
                      | 3   | D E F  | 
                      | 4   | G H I  | 
                      | 5   | J K L  | 
                      | 6   | M N O  | 
                      | 7   | P Q R S| 
                      | 8   | T U V  | 
                      | 9   | W X Y Z| 
                      | 0   | space  |
                       --------------
Write a program that displays the key presses needed for a message entered by the
user. Construct a dictionary that maps from each letter or symbol to the key presses
needed to generate it. Then use the dictionary to create and display the presses needed
for the user’s message. For example, if the user enters Hello, World! then your
program should output 4433555555666110966677755531111. Ensure that
your program handles both uppercase and lowercase letters. Ignore any characters
that aren’t listed in the table above such as semicolons and parentheses.
'''




my_dictionry = {
    "1": [".", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": " "
}

print(my_dictionry["1"][0])

user_message = ''
user_input = input("Enter your message: ")
for chars in user_input:
    if chars == (my_dictionry["1"][0]):
        user_message += "1"
    elif chars == (my_dictionry["1"][1]):
        user_message += "11"

    elif chars == (my_dictionry["1"][2]):
        user_message += "111"
    
    elif chars == (my_dictionry["1"][3]):
        user_message += "1111"

    elif chars == (my_dictionry["2"][0]):
        user_message += "2"

    elif chars == (my_dictionry["2"][1]):
        user_message += "22"

    elif chars == (my_dictionry["2"][2]):
        user_message += "222"

    elif chars == (my_dictionry["3"][0]):
        user_message += "3"

    elif chars == (my_dictionry["3"][1]):
        user_message += "33"

    elif chars == (my_dictionry["3"][2]):
        user_message += "333"

    elif chars == (my_dictionry["4"][0]):
        user_message += "4"

    elif chars == (my_dictionry["4"][1]):
        user_message += "44"

    elif chars == (my_dictionry["4"][2]):
        user_message += "444"

    elif chars == (my_dictionry["5"][0]):
        user_message += "5"

    elif chars == (my_dictionry["5"][1]):
        user_message += "55"

    elif chars == (my_dictionry["5"][2]):
        user_message += "555"
    
    elif chars == (my_dictionry["6"][0]):
        user_message += "6"

    elif chars == (my_dictionry["6"][1]):
        user_message += "66"

    elif chars == (my_dictionry["6"][2]):
        user_message += "666"

    elif chars == (my_dictionry["7"][0]):
        user_message += "7"

    elif chars == (my_dictionry["7"][1]):
        user_message += "77"

    elif chars == (my_dictionry["7"][2]):
        user_message += "777"

    elif chars == (my_dictionry["7"][3]):
        user_message += "7777"

    elif chars == (my_dictionry["8"][0]):
        user_message += "8"

    elif chars == (my_dictionry["8"][1]):
        user_message += "88"

    elif chars == (my_dictionry["8"][2]):
        user_message += "888"

    elif chars == (my_dictionry["9"][0]):
        user_message += "9"

    elif chars == (my_dictionry["9"][1]):
        user_message += "99"

    elif chars == (my_dictionry["9"][2]):
        user_message += "999"

    elif chars == (my_dictionry["9"][3]):
        user_message += "9999"

    elif chars == (my_dictionry["0"]):
        user_message += "0"

    else:
        pass    


print(user_message)
