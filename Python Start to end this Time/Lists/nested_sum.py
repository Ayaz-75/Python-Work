'''
Exercise 10-1

Write a function called nested_sum that takes a list of lists of integers and adds up the
elements from all the nested lists.

For example: t = [[1, 2], [3], [4, 5, 6]]

nested_sum(t)
21
'''

t = [[1, 2], [3], [4, 5, 6]]


def nested_sum(lis):
    result = 0
    for item in lis:
        for sums in item:
            result += sums
        print(item)
#    return f"result is {result}"
    print(result)


nested_sum(t)
