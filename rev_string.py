
# reverse string using slicing method
# string = input("Enter a string: ")  # Example input: "hello"
# def rev_str(string):
#     return string[::-1]
# print("Reversed string is:", rev_str(string))


# with for loop and logic
# string = "sid"
# lem = len(string)
#
# for i in range(lem-1,-1,-1):
#     print(string[i], end=" ")

# with function
string= input("Enter the string")
def rev(s):
    lem = len(s)
    for i in range(lem-1, -1,-1):
        print(s[i], end=" ")
print(rev(string))
# print(f"the reverse steing is {rev()}")






