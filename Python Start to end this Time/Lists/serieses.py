# Write a function called cumsum that takes a list of numbers and returns the cumulative
# sum; that is, a new list where the ith element is the sum of the first i+1 elements from
# the original list.
# For example:
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# output: [1, 3, 6]
a = [1, 2, 3]
b = []
result = 0
for nums in a:
    result += nums
    b.append(result)
    # print(result, end="")

print(b)
