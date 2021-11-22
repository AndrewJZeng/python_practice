#
# Topics Covered In This Chapter:
#        Dictionary
#        random.choice()
#        multiple assignment
#        

from __future__ import print_function  # input for both python 2 and 3 version
from builtins import input             # input for both python 2 and 3 version
import random
#multiple line string
HANGMANPICS = ['''
 
     +---+
     |   |
         |
         |
         |
         |
   =========''', '''
 
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''', '''
   +----+
   |    |
  [O    |
  /|\   |
  / \   |
        |
 ==========''', '''
   +----+
   |    |
  [O]   |
  /|\   |
  / \   |
        |
 ==========''']
# words = 'ant bear cat dog beer'.split()
words = {'Colors':'red orange yellow green blue white black brown'.split(),
    'Shapes':'square triangle rectangle circle ellipse '.split(),
    'Fruits':'apple orange lemon lime pear watermelon grape '.split(),
    'Animals':'bat bear beaver cat cougar crab deer dog donkey'.split()}


def getRandomWord(wordDict):
     # This function returns a random word from random chosen list which are from words dictionary.
     listKey = random.choice(list(wordDict.keys()))
     wordChosen = random.choice(wordDict[listKey])
     return [wordChosen, listKey]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
     print(HANGMANPICS[len(missedLetters)])
     print()

     print('Missed letters:', end=' ')
     for letter in missedLetters:
         print(letter, end=' ')
     print()

     blanks = '_' * len(secretWord)

     for i in range(len(secretWord)): # replace blanks with correctly guessed letters
         if secretWord[i] in correctLetters:
             blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

     for letter in blanks: # show the secret word with spaces in between each letter
         print(letter, end=' ')
     print()

def getGuess(alreadyGuessed):
     # Returns the letter the player entered. This function makes sure the player entered a single letter, 
     # and not something else.
     while True:
         print('Guess a letter.')
         guess = input()
         guess = guess.lower()
         if len(guess) != 1:
             print('Please enter a single letter.')
         elif guess in alreadyGuessed:
             print('You have already guessed that letter. Choose again.')
         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
             print('Please enter a LETTER.')
         else:
             return guess

def playAgain():
     # This function returns True if the player wants to play again, otherwise it returns False.
     print('Do you want to play again? (yes or no)')
     return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord, secreteKey = getRandomWord(words)
gameIsDone = False
while True:
     print('The secrete word is about ' + secreteKey)
     displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

     # Let the player type in a letter.
     guess = getGuess(missedLetters + correctLetters)

     if guess in secretWord:
         correctLetters = correctLetters + guess

         # Check if the player has won
         foundAllLetters = True
         for i in range(len(secretWord)):
             if secretWord[i] not in correctLetters:
                 foundAllLetters = False
                 break
         if foundAllLetters:
             print('Yes! The secret word is "' + secretWord + '"! You have won!')
             gameIsDone = True
     else:
         missedLetters = missedLetters + guess

         # Check if player has guessed too many times and lost
         if len(missedLetters) == len(HANGMANPICS) - 1:
             displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
             print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' 
                + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
             gameIsDone = True

     # Ask the player if they want to play again (but only if the game is done).
     if gameIsDone:
         if playAgain():
             missedLetters = ''
             correctLetters = ''
             gameIsDone = False
             secretWord, secreteKey = getRandomWord(words)
         else:
             break
