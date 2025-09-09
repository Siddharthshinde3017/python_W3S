# num =8
num = int(input("Enter the num: "))
result = 1
for i in range (num,0,-1):
    result = result*i               #5*4*3*2*1
    print(f"{result}*{i}={result}")
print(f"the value of {num}! is {result}")
