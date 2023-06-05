
new_list = []
addition = 0
for nums in range(1, 101):
    new_list.append(nums)
    if nums % 2 == 0:
        addition += nums

print(new_list)
print(addition)
