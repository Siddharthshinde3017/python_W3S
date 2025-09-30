def my_fun(*numbers):
    print("passed numbers are: ",numbers)

my_fun(10,20,30,40)

# keyword argument
def my_fun1(child1,child2,child3):
    print("my child is: ",child1)

my_fun1(child3="devil",child2="tobias",child1="emis")