import random

# ---- Word List (Simple, 5 words) ----
WORD_LIST = ["python", "program", "hangman", "developer", "intern"]

# Randomly choose a word
secret_word = random.choice(WORD_LIST)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6


# ---- Function to display current progress ----
def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display


print("===== 🎮 Welcome to Hangman Game (CodeAlpha Task 1) 🎮 =====")

# ---- Main Game Loop ----
while wrong_guesses < max_guesses:
    print("\nWord:", display_word(secret_word, guessed_letters))
    print("Wrong guesses:", wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Validate guess
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter!")
        continue

    # Duplicate guess
    if guess in guessed_letters:
        print("⚠ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✔ Correct guess!")
    else:
        print("✘ Wrong guess!")
        wrong_guesses += 1

    # Check Win Condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

# ---- Losing Condition ----
if wrong_guesses == max_guesses:
    print("\n❌ Game Over! You ran out of guesses.")
    print("The word was:", secret_word)