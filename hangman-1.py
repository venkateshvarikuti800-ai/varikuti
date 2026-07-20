"""
Hangman Game
------------
A simple text-based Hangman game.

Key concepts used: random, while loop, if-else, strings, lists.
"""

import random

# A small predefined list of words to choose from
WORD_LIST = ["python", "hangman", "keyboard", "console", "wizard"]

MAX_INCORRECT_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """,
]


def choose_word(word_list):
    """Randomly select a word from the given list."""
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def is_word_guessed(word, guessed_letters):
    """Check if every letter in the word has been guessed."""
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


def get_valid_guess(guessed_letters):
    """Prompt the player until they enter a single, new, valid letter."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_hangman():
    """Main game loop."""
    word = choose_word(WORD_LIST)
    guessed_letters = []
    incorrect_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have "
          f"{MAX_INCORRECT_GUESSES} incorrect guesses allowed.")
    print("=" * 40)

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print(HANGMAN_STAGES[incorrect_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")
        if guessed_letters:
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            if is_word_guessed(word, guessed_letters):
                print(HANGMAN_STAGES[incorrect_guesses])
                print("Word: " + display_word(word, guessed_letters))
                print("\nCongratulations! You guessed the word: "
                      f"'{word}'. You win!")
                break
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        print("-" * 40)
    else:
        # Loop finished without a break -> player ran out of guesses
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"\nGame over! You've run out of guesses. "
              f"The word was: '{word}'.")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("Thanks for playing Hangman! Goodbye.")


if __name__ == "__main__":
    main()
