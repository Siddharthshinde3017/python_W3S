import numpy as np

Orignal= np.array([1,2,3,4,5,6,7])

# copid = Orignal.copy() # for creating view
#
# copid[0]=16
#
# print("Orignal Array is : ",Orignal)
# print("Copied Array is: ",copid)


# for creating view
# make_view = Orignal.view()
# print("Orignal Array is: ",Orignal)
# print("Array View is : ",make_view)
Orignal1 = np.array([[1,2,3,4],[5,6,7,8]])
arry_view = Orignal1.view()
print("Orignal")
print(Orignal1)
print("View is")
arry_view.shape =(4,2)
print(arry_view)