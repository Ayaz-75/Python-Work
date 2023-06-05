'''
Write a function called in_bisect that takes a sorted list and a target value and
returns the index of the value in the list if it’s there, or None if it’s not
'''


def in_bisect(lis, val):
    if val in lis:
        return lis.index(val)


list1 = [1, 2, 3, 4, 5, 6]


print(in_bisect(list1, 5))
