a = int(input("Enter Number "))
b = int(input("Enter number2"))

chose = input("enter operation + - * /" )

if chose == "+" :
    print(a+b)

elif chose =="-":
    print(a-b)

elif chose == "*" :
    print(a*b)

elif chose == "/":
    print(a/b)

else :
    print("invalid input ")