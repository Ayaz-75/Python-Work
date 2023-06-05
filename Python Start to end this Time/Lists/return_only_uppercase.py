"""
Another common operation is to select some elements from a list and return a
sublist. For example, the following function takes a list of strings and returns a list
that contains only the uppercase strings
"""

old_list = ['a', 'B', "c", "D", "e", "F"]
new_list = []


def only_upper(previous_list):
    for item in previous_list:
        if item.isupper():
            new_list.append(item)
    return new_list


print(only_upper(old_list))
