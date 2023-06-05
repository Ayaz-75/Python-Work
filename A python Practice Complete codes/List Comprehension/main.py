

with open('file1.txt') as file_1:
    contents_1 = file_1.readlines()
#     new_c1 = [int(x.replace('\n', '')) for x in contents_1]

with open('file2.txt') as file_2:
    contents_2 = file_2.readlines()
#     new_c2 = [int(x.replace('\n', '')) for x in contents_2]

# print(new_c1)
# print(new_c2)
result = [int(item) for item in contents_1 if item in contents_2]

# Write your code above 👆
print(result)


