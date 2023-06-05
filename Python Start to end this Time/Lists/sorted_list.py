'''
Exercise 10-5.
Write a function called is_sorted that takes a list as a parameter and returns True if
the list is sorted in ascending order and False otherwise.


For example:
is_sorted([1, 2, 2])
True
is_sorted(['b', 'a'])
False


'''


def is_sorted(lis):
    while lis:
        minimum = lis[0]
        for x in lis:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        lis.remove(minimum)
    return new_list


new_list = []
list1 = [1, 4, 3, 5, 7, 2, 6]
print(is_sorted(list1))
