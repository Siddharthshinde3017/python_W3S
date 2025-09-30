'''
identity operator is used to compare the memory locstion of the two operator

is - return true if the memory location is same

is not-return true if the memory location is not same
'''

a = [1,2,3,4]
b=a
c= [1,2,3,4]

print(a is b)

print(a is c)

print(a is not b)

print(a is not c)
