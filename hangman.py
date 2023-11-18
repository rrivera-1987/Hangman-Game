import random
from words import easy_difficulty, intermediate_difficulty, advance_difficulty

HANGMAN = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+  
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
    ]


# Before starting the game, choose a diffilculty level. It will give you a random word, based on what level you chose.
def choose_word(difficulty):
    if difficulty == "easy":
        return random.choice(easy_difficulty).lower()
    elif difficulty == "intermediate":
        return random.choice(intermediate_difficulty).lower()
    elif difficulty == "advance":
        return random.choice(advance_difficulty).lower()
    else:
        print(f"Invalid difficulty level'{difficulty}'. Please choose a difficulty level: ")
        return None

def play_hangman(): # Main game function
    # Choosing a difficulty level.
    difficulty = input("Choose your difficulty level: Easy, Intermediate, Advance: ").lower()
    word = choose_word(difficulty)
    if word is None:
        return
    
    guesses = set()
    max_guesses = 6
    current_guesses = 0
    # This variable will help with keeping a scoring system for the player.
    points = 0

    while current_guesses < max_guesses:  # Looping through the game until the player wins or loses.
        print("\n" + ''.join([letter if letter in guesses else "_" for letter in word])) 
        # Displaying the current state of the game
        # This will help me display the hangman with each incorrect guess.
        print(HANGMAN[current_guesses])
        print("Failed Tries: ",current_guesses)

    # The player will start the game, trying to guess the correct letters.
        guess = input("Guess a letter or word: ").lower()

        if guess in guesses:
            print("You already guessed that letter!")
            continue
        guesses.add(guess)

        if len(guess) == len(word) and guess == word: # Check if you guessed the correct word, get your points doubled.
            points += len(word) ** 2
            print(f"You guessed the correct word: '{word}'!")
            print(f"You win! Your score is {points}!") # Exit the while loop because the game was won.
            return # The player guessed the correct word.
    # Check for if the guessed letter is in the word, and gives you 1 point for the letter.
        elif len(guess) == 1 and guess in word:
            print("Correct")
            points += 1
            if all(letter in guesses for letter in word): # Checks if all the letters guessed are in the word.
                print(f"You win! The correct word was: '{word}'.")
                print(f"Your score is: {points}!")
                return
        else:
            current_guesses += 1
            print("Incorrect")
            if len(guess) == len(word): #When the player tries to guess the correct word, but is incorrect.
                print(HANGMAN[max_guesses])
                print(f"You are HANGED! The correct word was: '{word}'.")
                print("Score: 0")
                return
    
    if current_guesses == max_guesses:
        print(HANGMAN[current_guesses])
        print(f"You are HANGED! The correct word was: '{word}'")
        print("Score: 0")

play_hangman()
