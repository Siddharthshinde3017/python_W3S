
x = float(input("num 1 :"))
y= float(input("num 2 :"))
operation = input("operation  "  )
result = 0

if operation == "+" :
    result = x + y

elif operation == "-" :
    result = x - y

elif operation == "*" :
    result = x * y

elif operation == "/" :
    result = x / y

else :
    print("Invalid operation")
print(result)    

