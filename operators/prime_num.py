num = 32
if num>0:
    for i in range(2,num):
        if num%i == 0 :
            print("number is not prime number")
            break
        else:
         print("number is prime number")
else :
    print("number is not prime number")
