'''
Exercise 10-3.
Write a function called middle that takes a list and returns a new list that contains all
but the first and last elements.

For example:
t = [1, 2, 3, 4]
middle(t)
[2, 3]

'''
old_list = [1, 2, 3, 4, 5]
new_list = []


def middle(lis):
    for item in lis:
        new_list.append(item)

    return new_list[1:4]


print(middle(old_list))
