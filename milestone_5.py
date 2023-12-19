import random
word_list = ["mango", "banana", "papaya", "grapes", "lychee", "pineapple", "coconut", "orange", "watermelon"]
num_lives = 5

# The Hangman class initializes a game of Hangman with a word list and a specified number of lives
# It keeps track of the word to be guessed, the guessed letters, and the number of letters in the word
'''
  A Hangman Game that asks the user for a letter and checks if it is in the word.
  It starts with a default number of lives and a random word from the word_list.

  Parameters:
  ------------
  word_list: list
    List of words to be used in the game
  num_lives: int
    Number of lives the player has

  Attributes:
  ------------
  word: str
    The word to be guess picked randomly from the word_list
  word_guessed: list
    A list of the letters of the word, with '_' for each letter not yet guessed
    For example, if the word is 'grapes', the work_guessed list would be ['_', '_', '_', '_', '_', '_']
    If the p[layer guesses 'g' the list would be ['g', '_', '_', '_', '_', '_']
  num_letters: int
    The number of unique letters in the word that have not been guessed yet
  num_lives: int
    The number of lives the player has
  list_letters: list
    A list of the letters that have already been tried

  Methods:
  ---------
    check_letter(letter)
      Checks if the letter is in the word.
    ask_letter()
      Asks the user for a letter.
'''
class Hangman():
  
  def_init_(self, word_list, num_lives = 5):
    self.word_list = word_list
    self.num_lives = num_lives
    self.word = random.choice(self.word_list)
    self.word_guessed = ["_" for char in self.word]
    self.list_of_guesses = []
    self.num_letters = len(set(self.word))
    print("The mystery word has,", self.num_letters, "characters")
    print(self.word_guessed)
    pass

  def check_guess(self, fuess):
    """
    The function 'check_guess' takes a guess as input, checks if the guess is in the word, updates the word_guessed list if the guess is correct,
    decreases the number of remaining letters if the guess correct, decreases the number of lives if the guess is incorrect and prints appropriate messages.

    :param guess: The 'guess' parameter is a string that represents the player's guess for a letter in the word
    """
    self.guess.lower()
    if self.guess in self.word:
      print("Good guess!", self.guess, ", is in the word!")
      for char in range(len(self.word)):
        if self.guess == self.word[char]:
          self.word_guessed[char] = self.guess
      print(self.word_guessed)
      self.num_letters -= 1
    else:
      print(self.word_guessed)
      self.num_lives -= 1
      print("Unlucky!", self.guess, ", is not in the word")
      print("You have ", self.num_lives," lives left!")
    pass

def ask_for_input(self):
  """
  The function asks the user to input a letter, checks if the input is valid, and keeps track of the guessed letters.
  """
  while (self.num_lives != 0 and self.num_letters !=0):
    self.guess = input("Please enter a letter.\n")
    if ((self.guess.isalpha() == False) or (len(self.guess) >= 2)):
      print("Invalid input. Please, enter a single alphabetical character")
    elif self.guess in self.list_of_guesses:
      print("You have already tried that letter!")
      print("Already guessed letters:", self.list_of_guesses)
    else:
      self.check_guess(self.guess)
      self.list_of_guesses.append(self.guess)
      print("Already guess letters:", self.list_of_guesses)
  pass

def play_game(word_list):
  """
  The function "play_game" allows the user to play a game of Hangman using a given word list.

  :param word_list: The word_list parameter is a list if words that the Hangman game will choose from.
  Each word in the list represents a possible word for the player to guess
  """
num_lives = 5
game = Hangman(word_list, num_lives = 5)
while (True):
  if game.num_lives == 0:
    print ("Sorry! You loose.")
    break
  elif game.num_lives != 0 and game.num_letters != 0:
    print ("Congratulations, you've won!")
    print("The word was,",game.word,".")
    break
pass

# The 'if__name__ =='__main__': block is used to ensure that the code inside it is only executed if the script is run directly and not if it is imported as module.
.f __name__ == '__main__':
    word_list = ["mango", "banana", "papaya", "grapes", "lychee", "pineapple", "coconut", "orange", "watermelon"]
play_game(word_list)



