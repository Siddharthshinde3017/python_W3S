word = input("Enter a word: ")  # Example input: "siddharth"
vowel = ('a', 'e', 'i', 'o', 'u')
count = 0

# Step 1: Define a function to check if a character is a vowel
def count_vowel(char):  # Use 'char' as the parameter
    return char in vowel

# Step 2: Loop through each character in the word
for char in word:
    if count_vowel(char):  # Step 3: Check if it's a vowel using the function
        count += 1          # Step 4: If yes, increase the count
        print(f"{char} is a vowel")

# Step 5: Print the final count
print(f"Number of vowels in {word} is {count}")
