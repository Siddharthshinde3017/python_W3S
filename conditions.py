age = int( input( "enter age :"))
nationality = input("enter nationality :")
print(age)
if age >= 18 and nationality == 'indian' :
    print("you are an vote")
elif age == 18 and nationality != "indian":
    print("vote carefully")

else: 
    print("you cannot vote")