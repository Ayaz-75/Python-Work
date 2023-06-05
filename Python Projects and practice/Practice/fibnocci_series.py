'''
Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34

'''
'''x = 0
y = 1

while y<50:
    # print(y)
    x,y = y,x+y
	
    print(x)'''

'''row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)'''


'''
row1 = ['1', '2','3']
row2 = ['4', '5','6']
row3 = ['7', '8','9']

map = [f"{row1}\n,{row2}\n, {row3}\n"]
print(f"{row1}\n{row2}\n{row3}\n")


row=int(input("enter row number..."))
column=int(input("enter column number..."))
val=input("enter the value you want to change with...")
# val2=int(input("enter the second value to be changed..."))

if row == 1:
    row1[column-1]=val

elif row == 2:
    row2[column-1]=val

elif row == 3:
    row3[column-1]=val

else:
    print("invalid row")
# row1[column-1]=val2
print(f"{row1}\n{row2}\n{row3}\n")
'''

'''num_of_rows = int(input('Enter number of rows: '))
num_of_columns = int(input('Enter number of columns: '))


a = []
b = []


for i in range(0, num_of_columns):
    b.append(1)

for j in range(0, num_of_rows):
    a.append(b)

print(a)'''

'''import random
letters = ['a','b','c','d','e','f']
numbers = [1,2,3,4,5,6]
symbols = ['!','@','#','%','&','*']

password = []

ltrs_input = int(input('How many letters ?'))
nums_input = int(input('How many numbers ?'))
symb_input = int(input('How many Symbols ?'))

for i in range(ltrs_input):
    password.append(random.choice(letters))

for i in range(nums_input):
    password.append(random.choice(numbers))

for i in range(symb_input):
    password.append(random.choice(symbols))


random.shuffle(password)


print(password)'''

'''nums = []
for i in range(200, 400):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        nums.append(s)

print(','.join(nums))'''

'''for i in range(5):
    for j in range(1, 6-i):
        print(i+j, end="")
    print()
'''
