old_list = [1, 4, 3, 2, 7, 6, 9, 8]

new_list = []

while old_list:
    minimum = old_list[0]
    for itm in old_list:
        if itm < minimum:
            minimum = itm

    new_list.append(minimum)
    old_list.remove(minimum)


print(new_list)
