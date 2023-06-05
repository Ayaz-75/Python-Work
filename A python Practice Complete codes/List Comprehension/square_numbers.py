old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# TODO-1 create a new list of square numbers from old one if and only if the numbers are even
new_list = [n**2 for n in old_list if n%2 == 0]
print(new_list)
