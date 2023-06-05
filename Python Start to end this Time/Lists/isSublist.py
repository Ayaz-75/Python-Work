'''
Exercise 133: Does a List Contain a Sublist?
(44 Lines)
A sublist is a list that is part of a larger list. A sublist may be a list containing a
single element, multiple elements, or even no elements at all. For example, [1],
[2], [3] and [4] are all sublists of [1, 2, 3, 4]. The list [2, 3] is also a
sublist of [1, 2, 3, 4], but [2, 4] is not a sublist [1, 2, 3, 4] because
the elements 2 and 4 are not adjacent in the longer list. The empty list is a sublist of
any list. 

As a result, [] is a sublist of [1, 2, 3, 4]. A list is a sublist of itself,
meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4].


```In this exercise you will create a function, isSublist, that determines whether
or not one list is a sublist of another. Your function should take two lists, larger
and smaller, as its only parameters. It should return True if and only if smaller
is a sublist of larger. Write a main program that demonstrates your function```

'''


# def isSublist(larger, smaller):
#     
# 
#     
# 
#     for item in larger:
#         if item and (item+1) not in smaller:
#             return False
#         else:
#             return True
# 
# new_list = [1, 2, 3, 4]
# sub1 = [1, 3]
# 
# print(isSublist(new_list, sub1))


list1 = [1, 2, 3]
new_list = []


# for item in range(len(list1)+1):
for item2 in range(len(list1)+1):
    new_list.append(list1[:item2])
print(new_list)





# List_1 = []
# List_of_sublists = []
# 
# size = int(input('Enter the size of the list :'))
# 
# # print('Enter all elements of the list :')
# for i in range(size):
#     List_1.append(int(input('Enter element to add : ')))
# 
# for i in range(len(List_1) + 1):
#     for j in range(i + 1, len(List_1) + 1):
#         List_of_sublists.append(List_1[i:j])
# 
# print(List_1)
# print(List_of_sublists)
# 