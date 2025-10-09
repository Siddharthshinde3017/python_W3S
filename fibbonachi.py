def fubonacchi(n):
    if (n<0):
        return "Not possible for negative nummbers"
    elif (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fubonacchi(n-1)+fubonacchi(n-2)
print(fubonacchi(9))