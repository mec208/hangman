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


