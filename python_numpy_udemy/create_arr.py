import numpy as np

arr1 = np.array([1,2,3,4,5])

print(arr1)

arr2d = np.array([[1,3,2,4],[5,6,7,8]])
print("2d array is ", arr2d)

arr3d = np.array([[1,3,2,4],[5,6,7,8],[9,10,11,12]], ndmin=3)
print( arr3d)

arr = np.array([1,2,3,4,5], ndmin=3)
print(arr, arr.ndim)
