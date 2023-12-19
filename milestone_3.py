import random

word_list = ["mango", "banana", "papaya", "grapes", "lychee"]
word = random.choice(word_list)
guess = input("Enter a letter.\n")

def ask_for_input():
  """
  The function asks the user to enter a single letter and checks if the input is valid.
  """
  while (True):
    guess = input("Enter a letter.\n")
    if ((guess.isalpha() == True) and (len(guess) ==1)):
      print("That is a valid input.")
      break
    else:
      print("Oops! That is not as valid input. Please enter a single alphabetical character.")
  check_guess()
  
def check_guess():
"""
The function checks if a guess is in a word and prints a corresponding message.
"""
if (guess in word):
  print("Good guess!", guess, "is in the word!")
else:
  print("Sorry," guess, "is not in the word. Try again.")

ask_for_input()
