
heights = [5, 6, 5.2, 5.6, 6.2, 5.5, 5.3]

addition = 0
for item in heights:
    addition += item

average = addition/len(heights)

print(average.__round__(3))
