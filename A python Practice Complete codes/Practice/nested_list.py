# list_1 = [1, 2, 3, 4, 5]
# list_2 = [6 ,7, 8, 9, 10]

# combined_list = [list_1, list_2]

# print(combined_list[0][2])

################################### Treasure Map #####################################

row_1 = ['😍', '🤣', '😀']
row_2 = ['😀', '😍', '🤣']
row_3 = ['😀', '🤣', '😍']

map = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")


row = int(input("Tell the row number ? ")) - 1
column = int(input("Tell the column number ? ")) - 1

position = map[row][column]

new_value = input("What do you want to replace with: ")
map[row][column] = new_value
print(f"{row_1}\n{row_2}\n{row_3}")
