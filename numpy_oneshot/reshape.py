import numpy as np
arr = np.array([10,20,30,40,50,60])
arr2 = arr.reshape(3,2)
print(arr2)
# Reshaping does not create copy insted it creates view