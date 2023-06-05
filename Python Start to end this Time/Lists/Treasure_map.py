
row1 = ['1', '2', '3']
row2 = ['4', '5', '6']
row3 = ['7', '8', '9']

map_1 = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure ? ")
i = position[0]
j = position[1]
map_1[int(i) - 1][int(j) - 1] = input("What do you want to put at treasure")


print(f"{row1}\n{row2}\n{row3}")

