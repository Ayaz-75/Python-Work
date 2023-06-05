"""
When you pass a list to a function, the function gets a reference to the list. If the func‐
tion modifies the list, the caller sees the change. For example, delete_head removes
the first element from a list

"""
old_list = ['a', 'b', 'c']


def delete_head(lis):
    del lis[0]
    return lis


print(delete_head(old_list))

# ##################################################
# difference between modifying and creating new_list

new_list = [1, 2, 3, 4, 5]
new_list.append(6)
print(new_list)


next_list = new_list + [7]
print(next_list)


print(new_list is next_list)

t1 = [1, 3, 2]
t2 = t1[:]

print(t2.sort())
print(t1, t2)
