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
    # Display the hangman figure
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