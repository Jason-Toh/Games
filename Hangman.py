#Hangman

'''Requirements'''
#At the start of the game, let the user know how many letters the computer's word contains.
#Ask the user to supply one guess (i.e. letter) per round
#The user should receive feedback immediately after each guess about whether their guess appears in the computer's word
#After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.

'''Addtional Rules'''
#A user is allowed "twice the length of the secret word" guesses.
#For example, secret word = hero; No of guesses = 8. Make sure to remind the user of how many guesses he/she has left after each round.
#Assume that players will only ever submit one character at a time (A-Z).
#
#A user loses a guess only when he/she guesses incorrectly
#
#If the user guesses the same letter twice, do not take away a guess
#Instead, print a message letting them know they've already guessed that letter and ask them to try again.
#
#The game should end when the user constructs the full word or runs out of guesses. If the player runs of guesses (he/she "loses")
#Reveal the word to the user when the game ends

import random

def get_word_list():
    file = open("words_2.0.txt","r+")
    wordCount = 0
    wordList = []
    for line in file:
        line = line.strip()
        wordCount += 1
        wordList.append(line)
    return wordList

def get_random_word():
    random_word = random.choice(get_word_list())
    return random_word

def print_board(guesses):
    if guesses == 0:
        print("     -------")
        print("     |     |")
        print("           |")
        print("           |")
        print("           |")
        print("  ----------")
    elif guesses == 1:
        print("     -------")
        print("     |     |")
        print("     O     |")
        print("           |")
        print("           |")
        print("  ----------")
    elif guesses == 2:
        print("     -------")
        print("     |     |")
        print("     O     |")
        print("     |     |")
        print("           |")
        print("  ----------")
    elif guesses == 3:
        print("     -------")
        print("     |     |")
        print("     O     |")
        print("    /|     |")
        print("           |")
        print("  ----------")
    elif guesses == 4:
        print("     -------")
        print("     |     |")
        print("     O     |")
        print("    /|\    |")
        print("           |")
        print("  ----------")
    elif guesses == 5:
        print("     -------")
        print("     |     |")
        print("     O     |")
        print("    /|\    |")
        print("    /      |")
        print("  ----------")
    elif guesses == 6:
        print("     -------")
        print("     |     |")
        print("     O     |")
        print("    /|\    |")
        print("    / \    |")
        print("  ----------")

def get_updated_word(secretWord,alreadyGuessed):
    string = ""
    for i in range(len(secretWord)):
        if secretWord[i] in alreadyGuessed:
            string += secretWord[i]
        else:
            string += "_ "
    return string

def check_user_input(userInput,alreadyGuessed):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    if len(userInput)!= 1:
        print("ERROR: It must be a single character")
        return False
    if userInput not in alphabets:
        print("ERROR: It must be an alphabet")
        return False
    if userInput in alreadyGuessed:
        print("ERROR: That letter has already been guessed")
        return False
    return True

def hangman():
    print("WELCOME TO HANGMAN")
    print("\n")
    print("A game where you the user choose a letter and guess the word but beware if your hangman reaches full body you lose")
    print("\n")
    print("Choose one letter at a time and choose those letter wisely >:)")
    print("\n")
    guesses = 0
    secretWord = get_random_word().lower()
    alreadyGuessed = ""
    maxGuesses = 6
    display = "_ " * len(secretWord)
    while guesses < maxGuesses:
        print_board(guesses)
        print("Word: " + display)
        print("Already Guessed: " + alreadyGuessed)
        print("Current Guesses: " + str(guesses) + " out of " + str(maxGuesses))
        userInput = str(input("Please enter a letter: ")).lower()
        print(50 * "-")
        while check_user_input(userInput,alreadyGuessed) == False:
            print_board(guesses)
            print("Already Guessed: " + alreadyGuessed)
            print("Word: " + display)
            print("Current Guesses: " + str(guesses) + " out of " + str(maxGuesses))
            userInput = str(input("Please enter a letter: ")).lower()
            print(50 * "-")
        alreadyGuessed += " " + "".join(userInput) 
        if userInput not in secretWord:
            print("That letter is not in the word, try again >:)")
            guesses +=1
        else:
            print("That letter is in the word")
            display = get_updated_word(secretWord,alreadyGuessed)

        if display == secretWord:
            print_board(guesses)
            print("Congratulations, you guessed the secret word and it was '" + str(secretWord) + "'")
            userInput = str(input("Do you wish to try again? Yes or No? "))
            while userInput!= "No":
                if userInput == "Yes":
                    hangman()
                else:
                    userInput = str(input("Please enter either Yes or No? "))
                    continue
            break
    else:
        print_board(guesses)
        print("You have used up all your guesses, the secret word was '" + str(secretWord) + "'")
        userInput = str(input("Do you wish to try again? Yes or No? ")).lower()
        while userInput!= "no":
            if userInput == "yes":
                hangman()
            else:
                userInput = str(input("Please enter either Yes or No? ")).lower()
                continue
hangman()
        


