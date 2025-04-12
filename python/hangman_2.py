import random

# List which holds all the random words
words = ["biscuits","cookies","cake","cheese","eggs"]
# List which holds all the user inputs
guessedLetters = []

# Function for the title
def welcome():
    # Outputing a design for the title of the game
    print("=-"*10, end="=\n")
    print("Hangman")
    print("=-"*10, end="=\n")
    print("Guess the word!")

# Function for finding all the letters in the word
def displayWord(random_word, guessed_letters):
    displayed_word = ''
    for letter in random_word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

# Function to check if the word has been fully guessed
def isWordGuessed(random_word, guessed_letters):
    for letter in random_word:
        if letter not in guessed_letters:
            return False
    return True

# Function for the main game
def game():
    # Calling the function for the main title
    welcome()
    # Declaring a variable which stores the amount of attempts
    randomWord = random.choice(words)
    attempts = len(randomWord) + 3

    # Starts a while loop which checks if the amount of attempts left is more than 0
    while attempts > 0:
        # Outputs the amount of letters left to guess
        print(displayWord(randomWord, guessedLetters))

        # Asks for a user input which automatically is sent to lowercase
        guess = input("> ").lower()
        print(f"You have {attempts-1} attempts left")
        
        # Checks if the input is only 1 letter
        if len(guess) != 1:
            print("Enter ONLY 1 letter!")
            print("_"*len(randomWord))
        # Checks if the user has already inputted a letter they have already guessed
        elif guess in guessedLetters:
                print("Already guessed that letter!")
        else:
            # Adds the input to a list
            guessedLetters.append(guess)

            # Checks if the user has ran out of attempts
            if attempts == 1:
                print(f"Out of attempts!\nThe word was {randomWord}.")
                break
            # Checks if the input is one of the letters in the word
            elif guess in randomWord:
                print("You guessed a letter!")
            else:
                print("Try again!")
                attempts -= 1
        
        # Checks if the word has been guessed
        if isWordGuessed(randomWord, guessedLetters):
            print(f"Well done! You guessed the mystery word {randomWord}!")
            break

# Calling the function
game()