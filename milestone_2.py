# The code is importing the 'random' module, which allows us to generate random numbers of make random choices.
# The code is a game where the user is asked to enter a letter and the code checks if the input is a single alphabetic character. 
# If it is, the code prints "Good guess". If not, it prints "Oops! That is not a valid input. Try again."
import random

word_list = ["mango", "banana", "papaya", "grapes", "lychee"]
word = random.choice(word_list)
guess = input("Enter a letter.\n")
if ((guess.isalpha() == True) and (len(guess) == 1)):
  print("Good guess!")
else:
  print("Oops! That is not a valid input. Try again.")
