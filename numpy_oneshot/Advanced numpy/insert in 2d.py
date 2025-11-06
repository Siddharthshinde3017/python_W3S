import numpy as np

arr = np.array([[10,20,30],
                [40,50,60]])
new2d_arr = np.insert(arr,1,[5,6],axis=none)
print(new2d_arr)