old_list = [1, 2, 3, 3, 4, 4, 5, 6, 7]

new_list = []


def duplicate(lis):
    for item in lis:
        if item not in new_list:
            new_list.append(item)

    return new_list


print(duplicate(old_list))
