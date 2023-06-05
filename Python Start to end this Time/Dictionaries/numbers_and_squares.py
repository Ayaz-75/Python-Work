new_dictionary = {}
# for nums in range(1, 11):
mul = 1
for nums in range(1, 6):
    new_dictionary[nums] = nums
    mul *= nums
new_dictionary.pop(2)

print(new_dictionary)
print(mul)
