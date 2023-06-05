# 4 x 4 matrix
row1 = ["X", "X", "X", "X"]
row2 = ["X", "X", "X", "X"]
row3 = ["X", "X", "X", "X"]
row4 = ["X", "X", "X", "X"]

matrix_map = [row1, row2, row3, row4]
print(f"{row1} \n{row2} \n{row3} \n{row4}")

position = input("Enter the position where you want to put a new element: ")

vertical_position = int(position[0])
horizontal_position = int(position[1])

matrix_map[vertical_position - 1][horizontal_position - 1] = input("With which character you want to replace previous")

print(f"{row1} \n{row2} \n{row3} \n{row4}")
