a = 23456
rev=0

while a>0:
    digit = a%10
    rev=rev*10+digit
    a = a//10
print(rev)

fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
print(newlist)
