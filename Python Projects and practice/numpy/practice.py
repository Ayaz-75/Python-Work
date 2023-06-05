import numpy as np

# NumPy array object
# a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 13, 14]])

# returning a 2-d array of specific elements from both arrays
# print(a[0:2, 1:2])

# checking the shape of array that what is the dimension of the array ex: above (2, 5)
# print(a.shape)

# accessing any specific element from the given array
# print(a[1, 3])

# accessing any specific row from given array
# print(a[0, :])

# accessing any specific column in given array
# print(a[:, 2])

a1 = np.array([[1, 2], [8, 9]])

mul = [a1[0] * a1[1]]
print(mul)


