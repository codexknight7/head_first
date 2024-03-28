# =============================================================================
# This application takes a word from user input and prints
# the unique vowels it found
# *****
# author: Konstantin Pankratov
# date: 2024-03-27
# =============================================================================

vowels = ['a','e','i','o','u','y']
found = []

word = input("Provide a word to search for vowels: ")

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print("Here is the list of unique vowels found in the word: " + word)
for vowel in found:
    print(vowel)
