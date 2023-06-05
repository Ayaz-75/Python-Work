students_height = input("Enter everybody's height: ").split()
sums = 0
for ele in range(0, len(students_height)):
    students_height[ele] = int(students_height[ele])
    sums += int(students_height[ele])
    avg = round(sums / len(students_height))
print("Sum of all elements =", sums)
print("Average of All heights =", avg)
