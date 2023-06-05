old_list = [5, 6, 3, 1, 2]

sum_s = 0
maximum = old_list[0]
minimum = maximum
for item in old_list:
    sum_s += item
    if maximum < item:
        maximum = item
    elif minimum > item:
        minimum = item

print("Maximum: ", maximum)
print("Minimum: ", minimum)
print("Average", sum_s/len(old_list))