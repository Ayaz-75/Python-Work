list1 = [1, 2, 3]

list2 = [item ** 2 for item in list1]

# print(list2)
name = 'ayaz'

new_name = [letter for letter in name]

new_range_list = [item for item in range(1, 5)]

new_list1 = [item ** 2 for item in range(1, 5)]

new_list2 = [item ** 2 for item in range(1, 5) if item % 2 == 0]

names = ['ayaz', 'lakho', 'Naresh', 'Dani', 'Aaqib', 'Haju']

new_names_list = [name for name in names if len(name) <= 4]

new_names_list_upper = [name.upper() for name in names if len(name) >= 5]

# ##interactive coding exercise squaring the numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(f"Numbers: {numbers}")

squared_numbers = [nums ** 2 for nums in numbers]
print(f"Squared Numbers: {squared_numbers}")

# ##interactive coding exercise filtering the even numbers
even_numbers_only = [nums for nums in numbers if nums % 2 == 0]
print(f"Only even numbers: {even_numbers_only}")
