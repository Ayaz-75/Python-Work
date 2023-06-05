import numpy as np

'''array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
array1 = np.array([[[1, 2, 3], [4, 5, 6]], [[6, 7, 8], [9, 10, 11]], [[1, 2, 3], [4, 5, 6]]])
arr = np.array(42)
array2 = np.array([[[1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4]]])

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(f"{array1}")
print(f"version of numpy: {np.__version__}")
print(f"dimension of array 2: {array2.ndim}")
print(arr)
print(array)

print("new line ")
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)'''

'''array2 = np.array([1, 2, 3, 4, 5], ndmin=5)
print(array2)

print(f"number of dimensions: {array2.ndim}")'''
# array2 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]])
# sums = array2[2] + array2[3]
# print(f"sum of 3rd and 4th element of array: {array2[1, 2]}")
# array3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(array3[0, 1, 2])
array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
last_item = array2[1, -1]
print(f"last item of the array is: {last_item}")

