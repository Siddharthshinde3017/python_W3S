import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8])

sliced_array = arr1[2:7]

print("sliced arry is6",sliced_array)

arr2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
sliced_arr2d = arr2d[0:2,1:3]
print(sliced_arr2d)


print(arr1[1:8:2])