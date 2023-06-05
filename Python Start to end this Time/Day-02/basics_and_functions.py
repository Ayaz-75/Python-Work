# import math
################################################################################
"""print("Mohsin once said, 'Do it before it's so late'")

# person_name = "Mohsin"
# message = "Do it before it's so late"
#
# print(f"{person_name}, '{message}'")"""

# x = y = 1
# print(x)
# print(y)
# '''The volume of a sphere with radius r is 4/3πr3.What is the volume of a sphere with
# radius 5?'''
# PI = 3.4145
# r = 1
# volume_of_sphare = 4/3 * PI *5**3
# print(volume_of_sphare)

'''
##############################################################################
Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
Shipping costs $3 for the first copy and 75 cents for each additional copy. What is
the total wholesale cost for 60 copies?'''

# cover_price = 24.95
# discount = (cover_price * 40) / 100
# shipping_cost_for_first_copy = 3
# rest_of_copy = 0.75 * 59
# price_of_first_copy = (cover_price + shipping_cost_for_first_copy) - discount
# price_for_all_remaining_copies = ((cover_price * 59 + rest_of_copy) - (discount * 59))
#
# total_price = price_of_first_copy + price_for_all_remaining_copies
#
# print("$", price_of_first_copy)
# print("$", price_for_all_remaining_copies)
# print("$", total_price)
'''
###################################################################################
If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then
3 miles at tempo (7:12 per mile) and 1 mile at an easy pace again, what time do I
get home for breakfast?
'''

# easy_pace = 2
# tempo = 3
# hours = 3
# minutes = 6
#
# print(f"I will arrive at house in {hours} Hours and {minutes} minutes"
#       f" from 6:52am to 9:58am")

#####################################################################################
# Conversion of datatypes
# a = 3.45
# b = int(a)  # this will convert the float into integer
# print(b, type(b))
#
# a = '123'
# b = int(a)  # this will convert the string into integer
# print(b, type(b))
#
# a = 3
# b = float(a)  # this will convert int into float
# print(b, type(b))
#
# a = 4.567
# b = str(a)  # this will convert the float into string
# print(b, type(b))

##################################################################################
#    ############################ FUNCTIONS ##############################
# create new functions without parameters


# def my_fun():
#     print("Ayaz")
#     print("Lakho")
#
#
# my_fun()
#
#
# def rep_func():
#     my_fun()
#     my_fun()
#
#
# rep_func()
#
# cube = math.pow(2, 3)
# print(cube)

#####################################################################################
# functions with parameters

# def print_twice(michel):
#     print(michel)
#     print(michel)
#
#
# print_twice(michel="I am the half of the bee")
#
#
# def cat_twice(part1, part2):
#     cat = part1 + part2
#     print_twice(cat)
#
#
# cat_twice('Big Cat', 'Small Cat')

# ######################################################################################
'''
Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the string is
in column 70 of the display:
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> right_justify('monty')
'''

# def right_justify(s):
#
#     spaces = " "*65
#     modified = spaces+s
#     print(modified)
#
#
# right_justify('monty')

# ###################################################################################################
'''
A function object is a value you can assign to a variable or pass as an argument. For
example, do_twice is a function that takes a function object as an argument and calls
it twice:
def do_twice(f):
 f()
 f()
'''

# def do_twice(f):
#     f()
#     f()
#
#
# def fun():
#     print("Spam")
#
#
# do_twice(f=fun)

'''
Define a new function called do_four that takes a function object and a value and
calls the function four times, passing the value as a parameter. There should be
only two statements in the body of this function, not four.
'''

# def do_twice(funct, args):
#     funct(args)
#     funct(args)
#
#
# def do_four(func, arg):
#     """Runs a function four times.
#     func: function object
#     arg: argument passed to the function
#     """
#     do_twice(func, arg)
#     do_twice(func, arg)
#
#
# do_twice(print, 'spam')
# print('')
#
# do_four(print, 'spam')

# #####################################################################################################
'''
Note: This exercise should be done using only the statements and other features we
have learned so far.
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
'''
# ###################################################################################################
'''
Write a function that draws a similar grid with four rows and four columns
'''


# def grid():
#     plus_minus()
#     lines_func()
#     plus_minus()
#     lines_func()
#     plus_minus()
#     lines_func()
#     plus_minus()
#     lines_func()
#     plus_minus()
#
#
# def plus_minus():
#     print(f"+ - - - - + - - - - + - - - - + - - - - +")
#
#
# def lines():
#     print(f"|         |         |         |         |")
#
#
# def lines_func():
#     lines()
#     lines()
#     lines()
#     lines()
#
#
# grid()

