import random
def choose_word():
    """choose word from a list    
    Returns:
        string -- selected word
    """
    wordlist = 'ant bear cat dog beer'.split()
    print(wordlist)
    w = random.choice(wordlist)
    return w

def is_word_guessed(secrete_word, letters_guessed):
    """check whether all of letters of secrete word have been guessed    
    Arguments:
        secrete_word {string} -- secrete word
        letters_guessed {string} -- guessed letters
    Returns:
        Boolean -- True if all letters of the word are found in the letter_guessed.
                    Otherwise False.
    """
    for x in secrete_word:
        if x not in letters_guessed:
            return False
    return True

def get_guessed_word(secrete_word, letter_guessed):
    """Get the word with guessed letters
    Arguments:
        secrete_word {string} -- secrete word
        letter_guessed {string} -- guessed letters
    
    Returns:
        string -- word with guessed letters
    """
    word = ''
    for x in secrete_word:
        if x in letter_guessed:
            word += x
        else:
            word += '_'

    return word

import string
def get_available_letters(letter_guessed):
    """get available lower case alphabet letters
    Arguments:
        letter_guessed {string} -- guessed letters
    Returns:
        string -- available lower case alphabet letters excluding guessed letter
    """
    letters = string.ascii_lowercase
    remaining = ''
    for x in letters:
        if x not in letter_guessed:
            remaining += x
    return remaining

def guess_loop(secrete_word, max_guess):    
    """loop when the remaining guess is larger than zero:
            1) the user inputs a letter.
            2) If the letter is not in the secrete word, remaining guess descreases and continue
               Otherwise the letter is added guessed_letter. 
                If the all letters of the secrete word, the game is over and user won
            3) when the remaining guess is zero, exit the loop
        4) the game is over and user lost
    Arguments:
        secrete_word {string} -- secrete word
        max_guess {integer} -- maximum of guesses
    """
    remaining_guess = max_guess
    guessed = ''
    while remaining_guess > 0:
        print('You have {} guesses left'.format(remaining_guess))
        print('Available letters: {}'.format(get_available_letters(guessed)))
        letter = input('Please guess a letter: ')
        letter = letter.lower()
        if letter in secrete_word:
            guessed += letter
            print('Good guess: {}'.format(get_guessed_word(secrete_word, guessed)))
            if is_word_guessed(secrete_word, guessed):
                print('Congratulations, You won!\n')
                return
        else:
            print('Oops! That letter is not in my word: {}'.format(get_guessed_word(secrete_word, guessed)))
            remaining_guess -= 1

    print('Sorry, you ran out of guesses. The word was {}\n'.format(secrete_word))

def hangman(max_guess):
    secrete_word = choose_word()

    print('''Welcome to the game Hangman!
    I am thinking of a word that is {} letters long.
    '''.format(len(secrete_word)))
    
    guess_loop(secrete_word, max_guess)

if __name__ == '__main__':
    hangman(4)
