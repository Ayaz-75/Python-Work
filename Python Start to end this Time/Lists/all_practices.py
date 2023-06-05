'''
040 
Ask for a number below 50 and then count down from 
50 to that number, making sure you show the number 
they entered in the output. 

'''

# user_number = int(input("Enter any number below 50: "))
# for i in range(user_number, 0, -1):
#     print(i)


'''
Ask the user to enter their name and a number. If the number is less than 10, then 
display their name that number of times; otherwise display the message “Too 
high” three times. 

'''

# your_name = input("name: ")
# num = int(input("Times: "))
# for nam in range(num):
#     if num < 10:
#         print(your_name)
#     else:
#         print("Too high")
#         break
#         
# print(your_name)
# print(your_name)
# print(your_name)


'''
042 
Set a variable called total to 0. Ask the user to enter 
five numbers and after each input ask them if they 
want that number included. If they do, then add the 
number to the total. If they do not want it included, 
don’t add it to the total. After they have entered all five
numbers, display the total. 

'''

# total = 0
# for num in range(5):
#     next_num = int(input("Enter number: "))
#     user_choice = input("Do you want to add this number to total: ")
#     if user_choice == "yes":
#         total += next_num
# 
# 
# print(total)


'''
Ask which direction the user wants to count (up or down). If they select up, then ask 
them for the top number and then count from 1 to that number. If they select down, ask 
them to enter a number below 20 and then count down from 20 to that number. If they 
entered something other than up or down, display the message “I don’t understand”.

'''

# direction = input("Which direction you want to count: ").lower()
# if direction == 'up':
#     top_num = int(input("Enter the top number: "))
#     for num in range(1, top_num+1):
#         print(num)
#     
# else:
#     bottom_num = int(input("Enter a number bellow 20: "))
#     for num in range(bottom_num, 0, -1):
#         print(num)


'''
Ask how many people the user wants to invite to a party. If they enter a number below 
10, ask for the names and after each name display “[name] has been invited”. If they 
enter a number which is 10 or higher, display the message “Too many people”.

'''
# new_list = []
# user_choice = int(input("How many people you want to invite in your party: "))
# if user_choice < 10:
#     for name in range(user_choice):
#         invited = input("Enter name: ")
#         new_list.append(invited)
#         print(f"{invited} has been invited!")
# 
# else:
#     print("Too many people!")
# 
# 
# print(f"These guestes has been invited!\n{new_list}")



'''
045 
Set the total to 0 to start with. While the total is 50 or less, ask 
the user to input a number. Add that number to the total and 
print the message “The total is… [total]”. Stop the loop when 
the total is over 50. 

'''
# total = 0
# while total < 50:
#     user_input = int(input())
#     total += user_input
# 
# 
# print(f"The total is: {total}")


'''
Ask the user to enter a number. Keep asking until they enter a value over 5 and 
then display the message “The last number you entered was a [number]” and 
stop the program

'''

# should_ask = True
# while should_ask:
#     user_input = int(input("Enter number: "))
#     if user_input == 5:
#         should_ask = False
#         print(f"The number was {user_input}")
# 



'''
048 
Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has 
now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this 
until they no longer want to invite anyone else to the party and then display how many people they have 
coming to the party. 

'''
# all_people = []
# counter = 0
# should_ask = True
# while should_ask:
#     
#     user_input = input("Enter who do you want to invite: ")
#     print(f"{user_input} has been invited!")
#     counter += 1
#     all_people.append(user_input)
# 
# 
#     some_body_else = input("is there someone else to be invited: ")
#     if some_body_else == 'yes':
#         continue
# 
#     else:
#         should_ask = False
#         print(f"Total {counter} people have been invited")



'''
------> 50 
Ask the user to enter a number between 10 and 20. If they enter a value under 10, 
display the message “Too low” and ask them to try again. If they enter a value 
above 20, display the message “Too high” and ask them to try again. Keep repeating 
this until they enter a value that is between 10 and 20 and then display the 
message “Thank you”. 

'''

# should_continue = True
# while should_continue:
#     user_number = int(input("Enter any number between 10 and 20: "))
#     if user_number < 10:
#         print("Too low")
# 
#     elif user_number > 20:
#         print("Too high")
# 
#     elif user_number > 10 and user_number < 20:
#         print("Thank you!")
# 
#     try_again = input("Do you want to Try again: ").lower()
# print("Thank you!")


'''
-----------> 51 

052 
Display a random integer between 1 and 100 inclusive.

'''
# import random
# new_number = random.randint(1, 10)
# print(new_number)


'''
----------->053
Display a random fruit from a list of five fruits

'''

# from numpy import random
# 
# 
# fruits = ['apple', 'orange', 'mango']
# randon_number = random.randint(len(fruits))
# print(fruits[randon_number])

'''
054
Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice. If their choice is the same 
as the randomly selected value, display the message “You win”, otherwise display “Bad luck”. At the end, tell 
the user if the computer selected heads or tails.

'''

# from operator import index
# from xxlimited import new
# from numpy import random
# from pyparsing import nums


# new_list = ['heads', 'tails']
# random_number = random.randint(0, len(new_list))
# computer_choice = new_list[random_number]
# 
# user_choice = input("choose 'head' or 'tails': ")
# if user_choice == computer_choice:
#     print(f"You win! computer also chose {computer_choice}")
# 
# else:
#     print(f"You loose! computer chose {computer_choice}")


'''
071 
Create a list of two sports. Ask the 
user what their favourite sport is and 
add this to the end of the list. Sort the 
list and display it. 

'''
# sports = ['Football', 'cricket']
# user_favourite = input("What is your favourite sport ? ")
# sports.append(user_favourite)
# 
# print(sports)


'''
073 
Ask the user to enter four of their favourite foods and store them in 
a dictionary so that they are indexed with numbers starting from 1. 
Display the dictionary in full, showing the index number and the item.
Ask them which they want to get rid of and remove it from the list. 
Sort the remaining data and display the dictionary.

'''


# new_dictionary = {}
# 
# should_continue = True
# while should_continue:
#     inde_x = int(input("Write index: "))
#     food_name = input("Write food name: ")
#     new_dictionary[inde_x] = food_name
# 
# 
#     add_other_food = input("Do do you want ? add another food or remove one from above: ").lower()
#     if add_other_food == 'add':
#         continue
# 
#     else:
#         print(new_dictionary)
#         which_delete = int(input("which item do you want to delete ? "))
#         new_dictionary.__delitem__(which_delete)
#         should_continue = False
#         
# 
# print(new_dictionary)
# print("Have a nice day!")



'''
074 

Enter a list of ten colours. Ask the user for a starting number between 0 and 4 
and an end number between 5 and 9. Display the list for those colours between the start and end 
numbers the user input.

'''
# colours = ['black','red', 'blue', 'green', 'white', 'pink', 'violet', 'orange', 'yellow', 'purple']
# print(colours)
# 
# starting_number = int(input("Enter starting number 0-4: "))
# ending_number = int(input("Enter ending number 5-9: "))
# 
# 
# for color in range(starting_number+1, ending_number-1):
#     print(colours[color])


'''
075 
Create a list of four three-digit numbers. Display the list to the user, showing each item from 
the list on a separate line. Ask the user to enter a three-digit number. If the number they 
have typed in matches one in the list, display the position of that number in the list, 
otherwise display the message “That is not in the list”

'''

# nums = [123, 456, 789, 222]
# print(nums)
# 
# user_num = int(input("Enter number: "))
# if user_num not in nums:
#     print("That is not in the list")
# else:
#     print(nums.index(user_num))


'''
076 
Ask the user to enter the names of three people they want to 
invite to a party and store them in a list. After they have entered 
all three names, ask them if they want to add another. If they do, 
allow them to add more names until they answer “no”. When 
they answer “no”, display how many people they have invited to 
the party. 


'''

# new_list = ['Aaqib', 'turab', 'zahoor']
# print(new_list)
# 
# 
# should_continue = True
# while should_continue:
#     user_choice = input("do you want to add another person to list: ").lower()
#     if user_choice == 'yes':
#         new_person = input("enter name: ")
#         new_list.append(new_person)
# 
#     else:
#         should_continue = False
#         print(new_list, "has been invited!")
# 

'''
085 
Ask the user to type in their name and then tell them how many vowels are in their name.

'''


# vowels = ['a', 'e', 'i', 'o', 'u']
# 
# counter = 0
# user_string = input("Enter your message here: ")
# for character in user_string:
#     if character in vowels:
#         counter += 1
# 
# 
# print(f"There are total '{counter}' vowels in string given above!")



'''
Exercise 110: Sorted Order

Write a program that reads integers from the user and stores them in a list. Your
program should continue reading values until the user enters 0. Then it should display
all of the values entered by the user (except for the 0) in ascending order, with one
value appearing on each line. Use either the sort method or the sorted function
to sort the list

'''
# my_list = []
# should_continue = True
# while should_continue:
#     user_input = int(input("Enter number: "))
#     my_list.append(user_input)
# 
#     if user_input == 0:
#         my_list.remove(user_input)
#         should_continue = False
# 
# print(my_list[::-1])


'''
Exercise 113: Avoiding Duplicates
(Solved, 21 Lines)
In this exercise, you will create a program that reads words from the user until the
user enters a blank line. After the user enters a blank line your program should display each word entered by the
user exactly once. The words should be displayed in the same order that they were first entered. 
For example, if the user enters:
first
second
first
third
second

then your program should display:

first
second
third

'''




# new_list = []
# sorted_list = []
# should_continue = True
# while should_continue:
#     user_input = input("Enter word: ")
#     new_list.append(user_input)
#     if user_input == " ":
#         should_continue = False
#         for item in new_list:
#             if item not in sorted_list:
#                 sorted_list.append(item)
# 
# print(sorted_list)

'''
Exercise 114: Negatives, Zeros and Positives

Create a program that reads integers from the user until a blank line is entered. Once
all of the integers have been read your program should display all of the negative
numbers, followed by all of the zeros, followed by all of the positive numbers. Within
each group the numbers should be displayed in the same order that they were entered
by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then

your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
should display each value on its own line

'''
