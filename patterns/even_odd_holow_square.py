""" 00000
    1   1
    0   0
    11111"""

r = 6
c = 6
for i in range (1,r+1):
    for j in range (1,c+1):
        if i == 1  :
            print("0",end=" ")
        elif i==r :#and i %2==0#:
            print("1",end=" ")
        elif j==1 or j==c:
            if i%2 ==0:
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            print(" ",end=" ")
    print()