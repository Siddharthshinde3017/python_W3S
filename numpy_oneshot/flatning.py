# use when we want to convert multidimentional arrya in 1d array
import numpy as np

arr = np.array([[10,20,30],
                [40,50,60]])
print(arr)
print('\n',arr.flatten())   # it returns a copy of arry
print('\n',arr.ravel())     # it returns a view of array
