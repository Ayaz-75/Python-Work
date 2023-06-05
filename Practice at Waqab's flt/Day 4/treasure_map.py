# 🚨 Don't change the code below 👇
row1 = ["A","B","C"]
row2 = ["D","E","F"]
row3 = ["G","H","I"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

first = int(position[0])-1
second = int(position[1])-1

treasure = map[first][second]
map[first][second] = "X"


#Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")