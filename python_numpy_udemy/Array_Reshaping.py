import numpy as np

Orgnal = np.array([1,2,3,4,5,6])
reshaped = Orgnal.reshape(2,3)
print("Oirgnal")
print(Orgnal)
print("reshaped")
print(reshaped)

# REshaped With Order
row_mejor = Orgnal.reshape(2,3, order='C')
print("row_mejor")
print(row_mejor)
col_mejor = Orgnal.reshape(2,3, order='F')
print("col_mejor")
print(col_mejor)