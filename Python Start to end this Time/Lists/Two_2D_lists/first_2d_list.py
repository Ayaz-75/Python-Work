'''grades = [[50, 60, 70],[60, 70, 80], [70, 80, 90]]
grades[1].append(4)
grades[1][2] = 5
print(grades)
'''



'''
-----> 96
Create the following using a simple 2D list using the standard Python indexing: 

1 2 3
4 5 6
7 8 9
'''
# first_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(first_2d)


'''
97 
Using the 2D list from program 96, ask the user to 
select a row and a column and display that value. 

'''

user_input = int(input("Which row: "))
user_input2 = int(input("Which column: "))
second_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(second_2d[user_input - 1][user_input2 - 1])

