'''
Create the following using a 2D dictionary showing the sales each person has made in the different 
geographical regions: 
    1st  2nd  3rd  4th
A    1    2    3    4
B    5    6    7    8
C    9    10   11   12
D    13   14   15   16

'''


# data_set = {'A': {'1st':1, '2nd':2, '3rd':3, '4th':4},
#             'B': {'1st':5, '2nd':6, '3rd':7, '4th':8},
#             'C': {'1st':9, '2nd':10, '3rd':11, '4th':12},
#             'D': {'1st':13, '2nd':14, '3rd':15, '4th':16}
#             }
# 
# 
#         
# print(data_set['B'])

'''
101 
Using program 100, ask the user for a name and a region. Display the relevant data. Ask 
the user for the name and region of data they want to change and allow them to make 
the alteration to the sales figure. Display the sales for all regions for the name they 
choose. 

'''

# data_set = {'A': {'1st':1, '2nd':2, '3rd':3, '4th':4},
#             'B': {'1st':5, '2nd':6, '3rd':7, '4th':8},
#             'C': {'1st':9, '2nd':10, '3rd':11, '4th':12},
#             'D': {'1st':13, '2nd':14, '3rd':15, '4th':16}
#             }
# 
# user_name = input("Enter name: ")
# user_area = input("Enter Area: ")
# 
# new_data = int(input("Enter new data: "))
# data_set[user_name][user_area] = new_data
# 
# 
# print(data_set[user_name])


'''
102 
Ask the user to enter the name, age and shoe size for four 
people. Ask for the name of one of the people in the list and 
display their age and shoe size.

'''

new_dictionary = {}
for people in range(2):
    user_name = input("Enter name of user: ")
    user_age = int(input("Enter user's age: "))
    shoe_size = int(input("Enter user's shoe size: "))

    new_dictionary[user_name] = {'Age': user_age,
                                 'Shoe Size': shoe_size
                                }



'''
103 
Adapt program 102 to display the names and ages of all the people in 
the list but do not show their shoe size.

'''

for i in new_dictionary:
    print(f"{i} {new_dictionary[user_name]['Age']}")
