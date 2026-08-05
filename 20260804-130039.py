import random

# List of predefined words
words = ["python", "apple", "house", "table", "ocean"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=== Welcome to Hangman Game ===")

while wrong_guesses < max_wrong_guesses:
    # Display the word
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the player has guessed the word
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", max_wrong_guesses - wrong_guesses)

# Game over
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print("The correct word was:", word)