'''
Exercise 114: Negatives, Zeros and Positives

Create a program that reads integers from the user until a blank line is entered. Once
all of the integers have been read your program should display all of the negative
numbers, followed by all of the zeros, followed by all of the positive numbers. Within
each group the numbers should be displayed in the same order that they were entered
by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then

your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
should display each value on its own line.

'''


'''
Exercise 115: List of Proper Divisors
(36 Lines)
A proper divisor of a positive integer, n, is a positive integer less than n which divides
evenly into n. Write a function that computes all of the proper divisors of a positive
integer. The integer will be passed to the function as its only parameter. The function
will return a list containing all of the proper divisors as its only result. Complete
this exercise by writing a main program that demonstrates the function by reading
a value from the user and displaying the list of its proper divisors. Ensure that your
main program only runs when your solution has not been imported into another file.

'''


# def find_properDivisor(num):
#     divisors = []
#     for divs in range(1, num):
#         if num % divs == 0:
#             divisors.append(divs)
# 
#     return divisors
# 
# print(find_properDivisor(20))
# 

'''
Exercise 116: Perfect Numbers
(Solved, 35 Lines)
An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
Write a function that determines whether or not a positive integer is perfect. Your
function will take one parameter. If that parameter is a perfect number then your
function will return True. Otherwise it will return False. In addition, write a main
program that uses your function to identify and display all of the perfect numbers
between 1 and 10,000.

'''

# def perfectNumber(num):
# 
#     divisors = []
#     addition = 0
#     for divs in range(1, num):
#         if num % divs == 0:
#             divisors.append(divs)
# 
#     print(f"{divisors} are divisors of {num}")
# 
#     for item in divisors:
#         addition += item
#     
#     if addition == num:
#         print(num, "is a perfect num")
# 
#     else:
#         print(f"{num} is not a perfect number")
# 
#     return
# 
# 
# perfectNumber(10)


# def List_of_perfectnums(num):
# 
#     divisors = []
#     addition = 0
#     for divs in range(1, num):
#         if num % divs == 0:
#             divisors.append(divs)
#             addition += divs
#     
#     # print(f"{divisors} are divisors of {num} and sum of all divisors = {addition}")
# 
#     if num == addition:
#         return True
#     
#     else:
#         return False
# 
# 
# new_list = []
# for item in range(1, 10000):
#     if List_of_perfectnums(item) == True:
#         new_list.append(item)
# 
#     else:
#         pass

# print(new_list)


'''
Exercise 117: Only the Words
(38 Lines)
In this exercise you will create a program that identifies all of the words in a
string entered by the user. Begin by writing a function that takes a string as
its only parameter. Your function should return a list of the words in the string
with the punctuation marks at the edges of the words removed. The punctuation marks
that you must consider include commas, periods, question marks,
hyphens, apostrophes, exclamation points, colons, and semicolons. Do not remove
punctuation marks that appear in the middle of a word, such as the apostrophes
used to form a contraction. For example, if your function is provided with the
string "Contractions include: don’t, isn’t, and wouldn’t."
then your function should return the list ["Contractions", "include",
"don’t", "isn’t", "and", "wouldn’t"].


'''

# def OnlyWords(s):
#     
#     print(s.split(" "))
# 
# 
# OnlyWords("Contractions include: don’t, isn’t, and wouldn’t.")




'''
Exercise 119: Below and Above Average

Write a program that reads numbers from the user until a blank line is entered. Your
program should display the average of all of the values entered by the user. Then
the program should display all of the below average values, followed by all of the
average values (if any), followed by all of the above average values. An appropriate
label should be displayed before each list of values.

'''


