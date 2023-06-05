'''
Exercise 139: Morse Code
(15 Lines)
Morse code is an encoding scheme that uses dashes and dots to represent digits and
letters. In this exercise, you will write a program that uses a dictionary to store the
mapping from these symbols to Morse code. Use a period to represent a dot, and
a hyphen to represent a dash. The mapping from characters to dashes and dots is
shown in Table 6.1.
Your program should read a message from the user. Then it should translate all of
the letters and digits in the message to Morse code, leaving a space between each
sequence of dashes and dots. Your program should ignore any characters that are not
listed in the previous table. The Morse code for Hello, World! is shown below:
.... . .-.. .-.. --- .-- --- .-. .-.. -..

 ____________________________________________________________________
| Character|Code|Character| Code  |Character|Code  |Character|Code   |
 ____________________________________________________________________
|  A      |.-  |   J     |.- - - |   S     | ...  |  1      |.- - - -|
|  B      |-...|   K     |  -.-  |   T     | -    |  2      |..- - - |
|  C      |-.-.|   L     |  .-.. |   U     | ..-  |  3      |...- -  |
|  D      |-.. |   M     |  - -  |   V     | ...- |  4      |....-   |
|  E      |.   |   N     |    -. |   W     | .- - |  5      |.....   |
|  F      |..-.|   O     |  ---  |   X     | -..- |  6      |-....   |
|  G      |- -.|   P     |  .- -.|   Y     | -.- -|  7      |- -...  |
|  H      |....|   Q     |  - -.-|   Z     | - -..|  8      |- - -.. | 
|  I      |..  |   R     |   .-. |   0     | -----|  9      |- - - -.| 
 --------------------------------------------------------------------
'''


mychars_dictionary = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"- -.",
    "H":"....",
    "I":"..",
    "J":".- - -",
    "K":"-.-",
    "L":".-..",
    "M":"- -",
    "N":'-.', 
    "O":'---',
    "P":'.- -.',
    "Q":'- -.-',
    "R":'.-.', 
    "S":"...",  
    "T":"-",    
    "U":"..-",  
    "V":"...-", 
    "W":".- -", 
    "X":"-..-", 
    "Y":"-.- -",
    "Z":"- -..",
    "0":" ",
    "1":".- - - -",
    "2":"..- - -",
    "3":"...- -",
    "4":"....-", 
    "5":".....", 
    "6":"-....", 
    "7":"- -...", 
    "8":"- - -..", 
    "9":"- - - -."
}
user_input = input("Enter your message to be encoded: ").upper()
encoded_message = ""
for item in user_input:
    if item in mychars_dictionary:
        encoded_message += mychars_dictionary[item]
        if item == " ":
            encoded_message += " "

print(encoded_message)
