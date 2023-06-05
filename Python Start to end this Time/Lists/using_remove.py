'''
Exercise 10-4.
Write a function called chop that takes a list, modifies it by removing the first and last
elements, and returns None.

For example:
t = [1, 2, 3, 4]
chop(t)
t
[2, 3]

'''
old_list = [1, 2, 3, 4, 5]


def chop(lis):
    lis.remove()
    return lis


print(chop(old_list))
