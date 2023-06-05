"""
write function takes a list of strings and returns a new list that contains capitalized
strings:

"""
old_list = ['a', 'b', 'c', 'd', 'e']


def capitalized(previous_list):

    new_list = []
    for item in previous_list:
        new_list.append(item.upper())

    return new_list


print("New_list = ", capitalized(old_list))
