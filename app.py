# Importing Random Module that always guesses a different word from the List
import random

def hangman():
  # List of words for the game - I chose Fruits (but can be anything)
  game_words = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
  ]
  
  # Selects a random word from the Words Array
  word = random.choice(game_words).lower()

  # Creating a List to store the Users guessed Letters
  letters_tried = []

  # User has maximum 6 Tries to guess the Word (can be changed)
  attempts = 6

  while True:
    # Display The Hangman Figure
    display_hangman(attempts)

    # Display the Game Word with Correct & Incorrect Letters
    display_word(word, letters_tried)

    # Checks to see if the Word has been completely guessed
    if guessed_word(word, letters_tried):
      print("Congratulations! You won!")
      break

    # Checks to see if the User has anymore attempts
    if attempts == 0:
      print("Game over!")
      print("The Word was:", word)
      print("Better Luck next time.")
      break

    # Tells the User to guess a Letter
    attempt = input("Enter a letter: ").lower()

    # Checks if the Users Input is Valid
    if not attempt.isalpha() or len(attempt) != 1:
      print("You can't use that. Please enter a single letter.")
      continue

    # Checks if the Users Input has already been entered
    if attempt in letters_tried:
      print("You've already tried that. Try again.")
      continue

    # Adds the Guessed Letter to the List
    letters_tried.append(attempt)

    # Check if the Users Letter is in the Game's Word
    if attempt not in word:
      attempts -= 1
  
def display_hangman(attempts):
  # Hangman Figure for every failed attempt
  stages = [
    """
      --------
      |      |
      |      O
      |     \|/
      |      |
      |     / \\
      -
    """,
    """
      --------
      |      |
      |      O
      |     \|/
      |      |
      |     / 
      -
    """,
    """
      --------
      |      |
      |      O
      |     \|/
      |      |
      |      
      -
    """,
    """
      --------
      |      |
      |      O
      |     \|
      |      |
      |     
      -
    """,
    """
      --------
      |      |
      |      O
      |      |
      |      |
      |     
      -
    """,
    """
      --------
      |      |
      |      O
      |    
      |      
      |     
      -
    """,
    """
      --------
      |      |
      |      
      |    
      |      
      |     
      -
    """
  ]
  print(stages[attempts])

# Display the games word with all Letters (Correct & Attempted)
def display_word(word, letters_tried):
  masked_word = ""

  for letter in word:
    if letter in letters_tried:
      masked_word += letter
    else:
      masked_word += "_"
  print(masked_word)

# Check if all the Users attempted Letters have been guessed
def guessed_word(word, letters_tried):
  for letter in word:
    if letter not in letters_tried:
      return False
  return True

# Launch Game
hangman()
