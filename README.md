# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

&nbsp;
# Milestone 1

The template repository was cloned to the local machine, and the GitHub bot was installed.

&nbsp;
# Milestone 2

Initial code was written for the task, in Python.  This includes: 

- import of modules needed for the script (`random`, `string`)
- set up of an example list of candidate words
- developing code to randomly select one of the words as the 'answer', using the `random.choice` method.
- asking for user input of a single letter as a guess. To avoid issues with case, the guess is converted to lowercase.
- checks to confirm that user input is alphabetical (i.e. within `string.ascii_lowercase`), and that only a single character is entered.
- returning different messages to the user according to whether these checks are passed


&nbsp;
# Milestone 3

Code was revised to ask for user input, confirm validity of user guess (allowing input to be re-entered if invalid), and subsequently check if user guess is in the randomly-selected word.  This was done by creation of two functions:

- `ask_for_input` function checks input is valid (using `.isalpha()` method), and uses a `while` loop to ask user for a valid input if input is not valid.

- `check_guess` function created to assess whether user guess is in the selected word (printing different messages accordingly).  This function is called by the `ask_for_input` function.


&nbsp;
# Milestone 4

A class was defined which contains attributes and methods necessary for the game.  The class requires one argument, `word_list`: the list of words from which a word will be selected. There is also an optional argument, `num_lives` for the number of lives the player has at the start of the game (this defaults to 5 if unspecified).

Starting attributes include a list of blank characters representing each of the letters of the randomly selected word, the number of lives of the player, and an (empty) list of the guesses made so far.

The methods defined in milestone 3 were included as class methods, with some updates/ additions:
- the `ask_for_input` function refers each guess to a list of previous guesses, and updates this list after each guess is made. Valid guesses are single letter alphabetical characters that haven't been guessed previously.

for valid guesses, the `check_guess` function is called.
- if the guess is in the word, the blank placeholders are replaced accordingly. 
- if the guess is not in the word, the player loses one life.


