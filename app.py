import random

def hangman():
  # List of words for the game - I chose Fruits (but can be anything)
  words = [
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
  word = random.choice(words).lower()

  # Creating a List to store the Users guessed Letters
  guessed_letters = []

  # User has maximum 6 Tries to guess the Word (can be changed)
  tries = 6