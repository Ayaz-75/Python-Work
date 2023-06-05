import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# -------------- printing elements from 3 to 5 -------------------#
# print(arr[2: 5])

# -------------- including step of 2 in above array ---------------#
# print(arr[1:5:2])

# print(arr[1:len(arr-1):2])

# from 3rd index from last to onwards
# print(arr[-3:])


# ---------------- printing every element of array without given index ---------------- #
print(arr[::2])
