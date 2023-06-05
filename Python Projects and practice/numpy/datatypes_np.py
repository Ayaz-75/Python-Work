import numpy as np

'''arr = np.array([1, 2, 3, 4, 5])

print(arr.dtype)'''

# -------------- Get the data type of array containing strings: -----------------
'''arr1 = np.array(['apple', 'banana', 'cherry'])

print(arr1.dtype)'''


# ------------------- Create an array with data type string: -----------------------
arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

print(arr.itemsize)
print(arr.size)
