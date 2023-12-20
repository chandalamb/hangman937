# Hangman

## Table of Contents
1.	Hangman Template – “hangman_template”: Provides a template of the final hangman game
2.	Milestone 2 – “milestone_2.py”: Provides a random word from a list and checks if the inputted letter valid – if it’s a single alphabetical input
3.	Milestone 3 – “milestone_3.py”: Defines the two functions from milestone 2 and also checks if the inputted letter exists within the randomly generated word.
4.	Milestone 4 – “milestone_4.py”: Initializes a game of hangman with a list of words and a specific number of lives
5.	Milestone 5 – “milestone_5.py”: A complete game of hangman

## Project Description
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.
The "Hangman" class is created to facilitate the Hangman game, initializing a word list and a specified number of lives. It selects a random word (initialising the word_guessed list) and sets up attributes (the random word, guessed word display, remaining unique letters, lives count and user input list). Attributes are initialized in the "init" method, allowing their use across various class methods.

Within the class Hangman there are two main function methods. The check_guess and ask_for_input method.

The "check_guess" method is a function that takes the user's guess as a parameter, checking if the guessed letter is in the word. It updates the guessed word and tracks remaining lives. The method converts the user's input to lowercase (with the lower() command) and if the guess is correct, it prints "good guess," reveals letter locations, and reduces remaining characters. If incorrect, it decreases lives, prints the current revealed word, notifies of a wrong guess, and displays the current life count.

The second method in the Hangman class manages user input, validates its correctness, and tracks the current state of the hidden word. It employs a while loop with conditions that the number of lives aren’t down to zero and the word hasn’t been fully revealed yet. The method prompts the user for input and checks if the users guess is valid – that it is a single, alphabetical character. If it is not valid the user is prompted to try a different input. Otherwise, if the input is valid and not previously entered, it passes the character to the "check_guess" method to determine if it is in the word, completing the class logic.

The "play_game" function, located outside the class, enables users to play Hangman using a provided word list. The function takes a word list and the initial number of lives as parameters, running the game through a while loop. The loop stops if lives reach zero or if the user correctly guesses the entire word. The function utilizes the Hangman class methods to prompt, validate, and check user input while updating the mystery word. The "if__name__ == '__main__':" block ensures that the code within it runs only when the script is executed directly, containing the word list and initiating the game.


## Installation instructions
To run this code:
- Clone repository
  * Go to GitHub.com and navigate to the main page of the repository
  * Click <>code.
  * Copy the URL for the repository
  * Open terminal
  * Change the current working directory to the location where you want the cloned directory
  * Type: git clone pasted_URL_here
  * Press Enter to create local clone
- Open file within VSCode in repository
- When making changes and updating them
  * git add
  * git commit -m “comment”
  * git push (this updates any changes to the code to the Git repository, where changes can be tracked

## Usage instructions
Once the code is running, input a letter. The game will confirm whether the letter is within the random word or not. Continue until you guess the word correctly or run out of lives. If you want to repeat the game, run the code again.

## File structure of the project
The technology stacks used in this code are Python and random.

## License information
MIT License 
Copyright (c) 2023 Chanda Lamb

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “hangman milestones”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

