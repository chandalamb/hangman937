# The code is importing the 'random' module, which allows us to generate random numbers of make random choices.
# The code is a game where the user is asked to enter a letter and the code checks if the input is a single alphabetic character. 
# If it is, the code prints "That is a valiud input.". If not, it prints "Oops! That is not a valid input. Please enter a single alphabetical character."
import random

word_list = ["mango", "banana", "papaya", "grapes", "lychee"]
word = random.choice(word_list)
guess = input("Enter a letter.\n")
if ((guess.isalpha() == True) and (len(guess) == 1)):
  print("That is a valid input.")
else:
  print("Oops! That is not a valid input. Please enter a single alphabetical character.")
