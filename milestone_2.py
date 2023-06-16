

# Imports needed for this script
import random
import string


# Set up example word list
word_list = ["apple", "banana", "orange", "mango", "pineapple"]
print(word_list)


# Select a word at random from the list
word = random.choice(word_list)



# Ask for User Input
guess = input("Enter a single letter >").lower()

lowercase_letters = string.ascii_lowercase

if len(guess)==1 and guess in lowercase_letters:
    print("Good guess!")
else: 
    print("Oops! That is not a valid input")

