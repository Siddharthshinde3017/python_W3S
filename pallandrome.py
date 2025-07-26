# x = input("enter the word")
# def reverse(x):
#     return x[::-1]
# if x == reverse(x):
#     print("pallandrome")
# else:
#     print("not pallandrome")


word = input("enter the word")
vowel = ('a','e','i','o','u')
count=0
def count_vowel(char):
    return char in vowel
for char in word:
    if count_vowel(char):
        count+= 1
        print(f"{char} this is vowel")
print(f"number of vowel in {word}"is {count})
