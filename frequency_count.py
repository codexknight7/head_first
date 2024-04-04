# =============================================================================
# This application takes a string from user input and prints
# the unique vowels it founds, with associated frequency
# *****
# author: Konstantin Pankratov
# date: 2024-04-04
# =============================================================================

vowels = ['a','e','i','o','u']
found = {}

word = input("Provide a word to search for vowels: ")

# check if a vowel from the list of vowels exists in word
# add this vowel to the dictionalry, with initial value 0
# then increment its value in dictionary by 1
# setdefault() method checks if the key is in dictionary
# and if not, creates it with default value provided
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

# itirate through dictionary's key/value pair, and print 
# key and associated value
# as Python doesn't store dictionary items in any particular order
# we use sorted() to order the keys ASC, for better visual presentation
for k,v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')

