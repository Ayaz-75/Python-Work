import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# ---- From the second element, slice elements from index 1 to index 4 (not included):----
# print(arr[1, 1:4])

# From the second element, slice elements from index 1 to index 4 (not including 4):
# print(arr[1, 1:])

print(arr[0:2, 1:2])

print(arr[0:2, 2])
