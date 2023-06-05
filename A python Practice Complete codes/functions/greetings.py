

# def greetings():
#     print("Welcome")
#     print("TO the world of")
#     print("Functions")


# greetings()


# def greetings_with_name(name):
#     print(f"Hey! {name} Welcome")
#     print("TO the world of")
#     print("Functions")

# my_name = input("Enter your name please!\n")
# greetings_with_name(my_name)

'''
042 
Set a variable called total to 0. Ask the user to enter five numbers and after each input ask 
them if they want that number included. If they do, then add the number to the total. 
If they do not want it included, don't add it to the total. After they have entered all five
numbers, display the total. 
'''

'''total = 0
for number in range(1, 6):
    should_include = input(f"Do you want to include the {number} in total?\n")
    if should_include == "yes":
        total += number


print(total)'''


'''
043 
Ask which direction the user wants to count (up or down). If they select up, then ask 
them for the top number and then count from 1 to that number. If they select down, ask 
them to enter a number below 20 and then count down from 20 to that number. If they 
entered something other than up or down, display the message “I don't understand”. 
'''

# user_direction = input("which direction you wants to count (up or down) ?\n")
# if user_direction == "up":
#     top_number = int(input("Enter the number to be counted till ?\n"))
#     for num in range(1, top_number + 1):
#         print(num)

# elif user_direction == "down":
#     lower_num = int(input("enter a number below 20 ?\n"))
#     for i in range(lower_num, -1, -1):
#         print(i)



'''
044 
Ask how many people the user wants to invite to a party. If they enter a number below 
10, ask for the names and after each name display “[name] has been invited”. If they 
enter a number which is 10 or higher, display the message “Too many people”.
'''

# number_of_people = int(input("How many people you want to invite to the party ?\n"))

# for person in range(number_of_people):
#     if person < 10:
#         name_of_person = input("Enter the name of person ?\n")
        
#         print(f"{name_of_person} has been invited!\n")


#     else:
#         print("Too many people")

'''
047 
Ask the user to enter a number and then enter another number. Add these 
two numbers together and then ask if they want to add another number. If they 
enter “y", ask them to enter another number and keep adding numbers until they 
do not answer “y”. Once the loop has stopped, display the total.

'''

number_1 = int(input("Enter First number: "))
number_2 = int(input("Enter second number: "))

add = number_1 + number_2

user_next_choice = input("Do you want to add another to previous sum ?")
while user_next_choice == "y":
    another_num = int(input("Enter another number: "))
    add += another_num
    if user_next_choice != "y":
        print(add)
        break

