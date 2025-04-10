import random

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[tries]


def get_word():
    #Selects a random word from a predefined list.
    words = ["python", "hangman", "programming", "developer", "keyboard"]
    return random.choice(words).lower()


def play_hangman():
    
    word = get_word()
    word_letters = set(word)  # Unique letters in the word
    guessed_letters = set()  # Letters guessed by the player
    tries = 6  # Number of incorrect tries allowed

    print("Welcome to Hangman!")
    print(display_hangman(tries))

    while tries > 0 and word_letters:
        print("Word: ", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print(f"Wrong guess! {guess} is not in the word.")
        
        print(display_hangman(tries))
    
    if not word_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")


play_hangman()
