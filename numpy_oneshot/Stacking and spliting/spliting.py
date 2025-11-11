import  numpy as np
arr = np.array([1,2,3,4,5,6,7,8])

new_arr = np.split(arr,2)
print(new_arr)


arr2d = np.array([[1,2,3,4],[4,5,6,7]])
print(arr2d)

new2d_arrr = np.vsplit(arr2d,2)     #virtical split
new2d_harrr = np.hsplit(arr2d,2)    #horizontal split

print(new2d_arrr)