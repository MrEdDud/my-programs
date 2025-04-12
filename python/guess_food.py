import random
words = ["biscuits","cookies","cake","cheese","eggs"]

def word():
    randomWord = random.choice(words)
    print("_" * len(randomWord))
    return randomWord

def wordList(y):
    wordLetters = []
    for x in range(len(wordChoice)):
        wordLetters.append("_")
    return wordLetters

wordChoice = word()
word_list = wordList(wordChoice)

game = input("Enter a letter ")

if game in wordChoice:
    print("Correct!")