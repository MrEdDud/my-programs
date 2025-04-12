import random

flag = 0
letters_guessed = ""

#A function to store a visual seperator
def seperator():
    print("------------------------------------------------------------")

#A function for the menu
def game_menu():
    print("Would you like to start a game?\n")
    inp = ""
    while inp != "yes" and inp != "no":
        x = input("")
        inp = x.lower()
        if inp != "yes" and inp != "no":
            print("Error: You must type yes or no")
        else:
            return inp

#Dictionary of words
some_words = '''apple banana mango strawberry orange grape 
pineapple apricot lemon coconut watermelon cherry peach'''
#Turns the dictionary into a list
some_words = some_words.split(" ")

seperator()
print("Welcome to Hangman!")
seperator()

#Main menu
main_menu = game_menu()
#Starts the game
if main_menu == "yes":
    seperator()
    if __name__ == "__main__":
        print("Guess the word!")
        word = random.choice(some_words)
        for x in word:
            print("_", end=" ")
        print()
        chances = len(word) + 2
        try:
            while (chances != 0) and flag == 0:
                print()
                chances -= 1

                try:
                    guess = input("Enter a letter: ")
                except:
                    print("Only 1 letter!")
                    continue
                
                #Checks if the input is a letter  
                if not guess.isalpha():
                    print("Only alphabetical letters!")
                    continue
                #Checks if the input is more than 1 letter
                elif len(guess) > 1:
                    print("Only 1 letter!")
                    continue
                #Checks if you already guessed that letter
                elif guess in letters_guessed:
                    print("You have already guess that letter!")
                    continue
                
                #If the letter is correctly guessed
                if guess in word:
                    #Variable k stores how many times the guessed letter appears in the word
                    k = word.count(guess) 
                    for _ in range(k):
                        letters_guessed += guess
                
                for char in word:
                    if char in letters_guessed and (letters_guessed) != (word):
                        print(char, end=" ")
                    elif (letters_guessed) == (word):
                        print("The word is: ", end=' ') 
                        print(word) 
                        flag = 1
                        print('Congratulations, You won!') 
                        print("Play Again?")
                        
                    else:
                        print("_",end=" ")

            if chances <= 0 and (letters_guessed) != (word):
                print()
                print("You lost! Try again..")
                print("The word was {}".format(word))

        except KeyboardInterrupt:
            print()
            print("Bye!")
    

#Closes the game
else:
    print("Goodbye!")
    exit