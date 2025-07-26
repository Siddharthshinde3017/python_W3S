vowel = ('a', 'e', 'i', 'o', 'u')
word =  input("Enter a word: ") #"siddharth"
count = 0
for char in word :
    if char in vowel:
        count +=1
        print(f"{char} is a vowel")
print(f"Number of vowels in {word} is {count}")