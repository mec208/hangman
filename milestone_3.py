

# Imports needed for this script
import random


# Set up example word list
word_list = ["apple", "banana", "orange", "mango", "pineapple"]
print(word_list)


# Select a word at random from the list
word = random.choice(word_list)
print(word) # #RESOLVE -> this needs to be removed in the final version!


# Check if guess is in the word

def check_guess(guess):

    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")


# Ask for User Input

def ask_for_input():   # calls check_guess

    while True:
        guess = input("Enter a single letter > ")
        if len(guess)==1 and guess.isalpha():
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")

    print(f"Guess: {guess}")

    check_guess(guess)    # call check_guess within the ask for input function


# call ask for input function
ask_for_input()