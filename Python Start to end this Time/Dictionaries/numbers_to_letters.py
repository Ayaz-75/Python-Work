'''
Exercise 141: Write out Numbers in English

While the popularity of cheques as a payment method has diminished in recent years,
some companies still issue them to pay employees or vendors. The amount being
paid normally appears on a cheque twice, with one occurrence written using digits,
and the other occurrence written using English words. Repeating the amount in two
different forms makes it much more difficult for an unscrupulous employee or vendor
to modify the amount on the cheque before depositing it.

In this exercise, your task is to create a function that takes an integer between 0 and
999 as its only parameter, and returns a string containing the English words for that
number. For example, if the parameter to the function is 142 then your function should
return [`` one hundred forty two ```] . Use one or more dictionaries to implement
your solution rather than large if/elif/else constructs. Include a main program that
reads an integer from the user and displays its value in English words.

'''

user_input = input("Enter Your digit: ")

my_dictionary = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}

alphabetic_numbers = []

for chars in user_input:

    if chars in my_dictionary:
        alphabetic_numbers.append(my_dictionary[chars])

        if len(alphabetic_numbers) == 4:
            alphabetic_numbers[0] += " thousands "
            alphabetic_numbers[1] += " hundreds"
            if alphabetic_numbers[2] == my_dictionary["2"]:
                alphabetic_numbers[2] = " and twenty "

            elif alphabetic_numbers[2] == my_dictionary["3"]:
                alphabetic_numbers[2] = " and thirty "

            elif alphabetic_numbers[2] == my_dictionary["4"]:
                alphabetic_numbers[2] = " and forty "

            elif alphabetic_numbers[2] == my_dictionary["5"]:
                alphabetic_numbers[2] = " and fifty "

            elif alphabetic_numbers[2] == my_dictionary["6"]:
                alphabetic_numbers[2] = " and sixty "

            elif alphabetic_numbers[2] == my_dictionary["7"]:
                alphabetic_numbers[2] = " and seventy "

            elif alphabetic_numbers[2] == my_dictionary["8"]:
                alphabetic_numbers[2] = " and eighty "

            elif alphabetic_numbers[2] == my_dictionary["9"]:
                alphabetic_numbers[2] = " and ninty "
            
            else:
                pass

        if len(alphabetic_numbers) == 3:
            # alphabetic_numbers[0] += " thousands "
            alphabetic_numbers[0] += " hundreds"
            if alphabetic_numbers[1] == my_dictionary["2"]:
                alphabetic_numbers[1] = " and twenty "

            elif alphabetic_numbers[1] == my_dictionary["3"]:
                alphabetic_numbers[1] = " and thirty "

            elif alphabetic_numbers[1] == my_dictionary["4"]:
                alphabetic_numbers[1] = " and forty "

            elif alphabetic_numbers[1] == my_dictionary["5"]:
                alphabetic_numbers[1] = " and fifty "

            elif alphabetic_numbers[1] == my_dictionary["6"]:
                alphabetic_numbers[1] = " and sixty "

            elif alphabetic_numbers[1] == my_dictionary["7"]:
                alphabetic_numbers[1] = " and seventy "

            elif alphabetic_numbers[1] == my_dictionary["8"]:
                alphabetic_numbers[1] = " and eighty "

            elif alphabetic_numbers[1] == my_dictionary["9"]:
                alphabetic_numbers[1] = " and ninty "
            
            else:
                pass


        if len(alphabetic_numbers) == 2:
            # alphabetic_numbers[0] += " thousands "
            # alphabetic_numbers[0] += " hundreds"
            if alphabetic_numbers[0] == my_dictionary["2"]:
                alphabetic_numbers[0] = "Twenty "

            elif alphabetic_numbers[0] == my_dictionary["3"]:
                alphabetic_numbers[0] = "Thirty "

            elif alphabetic_numbers[0] == my_dictionary["4"]:
                alphabetic_numbers[0] = "Forty "

            elif alphabetic_numbers[0] == my_dictionary["5"]:
                alphabetic_numbers[0] = "Fifty "

            elif alphabetic_numbers[0] == my_dictionary["6"]:
                alphabetic_numbers[0] = "Sixty "

            elif alphabetic_numbers[0] == my_dictionary["7"]:
                alphabetic_numbers[0] = "Seventy "

            elif alphabetic_numbers[0] == my_dictionary["8"]:
                alphabetic_numbers[0] = "Eighty "

            elif alphabetic_numbers[0] == my_dictionary["9"]:
                alphabetic_numbers[0] = "Ninty "
            
            else:
                pass
        
nums_string = ""
print(alphabetic_numbers)

for item in alphabetic_numbers:
    nums_string += item

print(nums_string)
