import random
              

class Hangman():

    def __init__(self, word_list, num_lives=5):
    
        self.word = random.choice(word_list)       # word to be guessed
        self.word_guessed = ['_']*len(self.word)   # list of letters of the word
        self.num_letters = len(set(self.word))     # number of UNIQUE letters in the word

        self.num_lives = num_lives                 # number of lives at start of the game
        self.word_list = word_list                 # a list of words

        self.list_of_guesses = []                  # list of guesses that have been tried

        

    def check_guess(self, guess):

        self.guess = guess.lower()                                  # convert all guesses to lowercase

        if self.guess in self.word:                                 # if correct
            print(f"Good guess! {guess} is in the word\n")            # print statement
            
            for letter_index, letter in enumerate(self.word):       # update word.guessed
                if letter == self.guess:
                    self.word_guessed[letter_index] = self.guess
            
            self.num_letters -= 1                                   # decrease number of UNIQUE (unguessed) letters by 1
            
            print(f"{'*'*(2*len(self.word)-1)}")    # not in instructions but prints letters so far   
            print(*self.word_guessed)               # wrapped with *** the length of the selected word
            print(f"{'*'*(2*len(self.word)-1)}")    #    
               

         
        else:
            self.num_lives -= 1    # reduce lives by 1
            print(f"\nSorry, {self.guess} is not in the word")
            print(f"You have {self.num_lives} lives left\n")
            
       

    def ask_for_input(self):

        while True:
            guess = input("Enter a single letter > ")
            if len(guess)!=1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")    
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")    
            else:
                self.list_of_guesses.append(guess) 
                self.check_guess(guess)
                break




def play_game(word_list):

    num_lives = 5 

    game = Hangman(word_list, num_lives)

    
    while True: 
        if game.num_lives == 0:
            print("You lost!\n\n\n")
            break
            
        if game.num_letters > 0:
            game.ask_for_input()

        if game.num_lives > 0 and game.num_letters==0:
            print("Congratulations. You won the game!\n")
            break
                



my_list = ["apple", "banana", "orange", "mango", "pineapple"]

play_game(my_list)
