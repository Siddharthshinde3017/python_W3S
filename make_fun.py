# def greet(name):
#     print("good afternoon", name)
# greet("aj")
# greet("ar")
# def add_num(a, b):
#     return a + b
# print(add_num(a,b=2))



# x = int(input("Enter a number: "))  # Example input: 5
# def square(x):
#     return x*x
# print("the square of ", x ,"is",square(x))


# write function for to find max of three numbers
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))
def max(a,b,c):
    if a>b and a>c:
        return  
    elif b>a and b > c:
        return b
    else:
        return c
print("the maximum of three number is ",max(a,b,c))    