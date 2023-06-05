# welcome to the Treasure map game
row1 = ["😝", "😝", "😝"]
row2 = ["😝", "😝", "😝"]
row3 = ["😝", "😝", "😝"]
t_map = [row1, row2, row3]
print(f"{row1} \n{row2} \n{row3}")
position = input("Where do you want treasure: ")

# first number stands for columns
# second number stands for rows

horizontal_position = int(position[0])
vertical_position = int(position[1])

t_map[vertical_position - 1][horizontal_position - 1] = input("With what character you want to replace current "
                                                              "treasure with: ")
print(f"{row1} \n{row2} \n{row3}")
