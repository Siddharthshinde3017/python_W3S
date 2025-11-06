import  numpy as np

arr_2d = np.array([[1,2,3],
                   [4,5,6]])
print(arr_2d.shape)  #checks how many rows and colums exist in data
print(arr_2d.size)   #checks how many data items in it
print(arr_2d.ndim)   # check how many dimention of data
print(arr_2d.dtype)  # checks and return data type of elements

arr_convert = arr_2d.astype(float)
print(arr_convert.dtype)