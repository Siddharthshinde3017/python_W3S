list1 = [1,1,1,2,2,3,4]
list2 =[1,2,1,1,2,3,4]
set1 = set(list1)
set2 = set(list2)
if len(set1) == len(set2):
    if set1.issubset(set2):
        print("lists are equal")
    else:
        print("lists are not equal")
else:
    print("lists are not equal")