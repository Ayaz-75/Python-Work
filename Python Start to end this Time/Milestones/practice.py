
########################## Lists ##########################
# # s = 'hello'
# # print(s[::-1])
# list3 = [1,2,[3,4,'hello']]
# list3[2][2] = "goodbye"
# 
# # print(list3)
# 
# # Finf minimum and maximum of list given bellow:
# list4 = [5,3,4,6,1]
# a = list4[0]
# b = a
# 
# for item in list4:
#     if a > item:
#         a = item
#     
#     
#     elif a < item:
#         b = item
# 
# print("Minium number in list is: ", a)
# print("Maximum number in list is: ", b)
# 
# 
# 
# # Sort the list below
# list5 = [5,3,4,6,1]
# new_list = []
# 
# 
# list5.sort()
# print(list5)
# 
# d = {'simple_key':'hello'}
# Grab 'hello'
# print(d['simple_key'])

######################### Dictioaries ########################
# d = {'k1':{'k2':'hello world'}}
# Grab 'hello'

# print(d['k1']['k2'])


# Getting a little tricker
# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
# print(d['k1'][0]['nest_key'][1])

########################## Tupple ########################
# firs_tupple = (1, 2, 3)
# print(firs_tupple[2])


######################### Sets ###########################
# Use a set to find the unique values of the list below:
# list5 = [1,2,2,33,4,4,11,22,3,3,2]
# new_set = set(list5)
# print(new_set)


############################ Booleans #####################

# print(3.0 == 3)
# # two nested lists
# l_one = [1,2,[3,4]]
# l_two = [1,2,{'k1':4}]
# 
# # True or False?
# answer = (l_one[2][0] >= l_two[2]['k1'])
# print(answer)
# 


############################## Test #########################

# st = 'Print only those words which start with s in this sentence'
# new_list = st.split(" ")
# print(new_list)
# empty_list = []
# for item in new_list:
#     if item[0] == "s":
#         empty_list.append(item)
# 
# 
# print(empty_list)
# 

############################ Range function ##########################
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)
# 
# 


########################## List Comprehension ######################### 
# all_nums = [num for num in range(1, 51) if num % 3 == 0]
# print(all_nums)



# only those words whose length is even
# st = 'Print only those words which start with s in this sentence'
# words = st.split(" ")
# 
# print([word for word in words if (len(word)%2==0)])

# new_list = []
# for i in range(1, 101):
#     new_list.append(i)
# 
# for item in new_list:
# 
#     if item % 3 == 0 and item % 5 == 0:
#         print("FizzBuzz")
# 
#     elif item % 3 == 0:
#         print("fizz")
#     
#     elif item % 5 == 0:
#         print('Buzz')
# 
#     else:
#         print(item)


# st = 'Print only those words which start with s in this sentence'
# st_list = st.split(" ")
# new_list = [letter[0] for letter in st_list]
# 
# print(new_list)

 
# new_dictionary = {"a": 1,
#                   "b": 2,
#                   "c": 3,
#                   "d": 3}
# 
# 
# new_dict = {}
# for item in new_dictionary:
#     value = new_dictionary[item]
# 
#     if value not in new_dict:
#         new_dict['key'] = value
# 
# print(new_dict)

# new_dict = {"A": 1,
#             "B": 2,
#             "C": 3}
# 
# addition = 0
# mul = 1
# for item in new_dict:
#     value = new_dict[item]
#     addition += value
#     mul *= value
# 
# print(f"Addition = {addition} \nMultiplication = {mul}")


# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# 
# new_dict = {}
# new_dict['List_1'] = list1
# new_dict['List_2'] = list2
# 
# 
# print(new_dict)

# ################################## Sort Dictionary #########################################


# new_dict = {1:1,
#             2:2,
#             4:4,
#             3:3}
# 
# minimum_v = new_dict[1]
# maximun_v = minimum_v
# for item in new_dict:
#     if minimum_v > item:
#         minimum_v = item
# 
#     elif maximun_v < item:
#         maximun_v = item
# 
# print(minimum_v)
# print(maximun_v)


# #############################################################################################
# Write a Python program to remove duplicates from Dictionary

# new_dict = {1:1,
#             2:2,
#             4:4,
#             3:3,
#             4:4}
# 
# diction = {}
# for item in new_dict:
#     value = new_dict[item]
#     if value not in diction:
#         diction[item] = value
# 
# print(diction)
# 

# 21. Write a Python program to create and display all combinations of letters, selecting each letter
# from a different key in a dictionary. Go to the editor
'''
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
'''
your_name = input("What is your name: ")
number_of_times = int(input("How name times our name should be printed: "))
for nam in range(number_of_times):
    for name in your_name:

        print(name)
