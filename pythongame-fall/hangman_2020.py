import random

from hangman_pictures import HANGMANPICS  ###

def choose_word():
    wordlist = 'ant bear cat dog beer'.split()
    print(wordlist)
    w = random.choice(wordlist)
    return w

def is_word_guessed(secrete_word, letters_guessed):
    for x in secrete_word:
        if x not in letters_guessed:
            return False
    return True

def get_guessed_word(secrete_word, letter_guessed):
    word = ''
    for x in secrete_word:
        if x in letter_guessed:
            word += x
        else:
            word += '_'
    return word

def guess_loop(secrete_word, max_guess):
    guessed = ''
    while max_guess > 0:
        print(f'You have {max_guess} guesses left')
        letter = input('Please guess a letter: ').lower()
        if letter in secrete_word:
            if letter in guessed:
                print('That letter has already been guessed')
                continue
            else:
                guessed += letter
                guessed_word = get_guessed_word(secrete_word, guessed)
                print(f'Good guess: {guessed_word}')
                if is_word_guessed(secrete_word, guessed):
                    print('Congrats, You won\n')
                    return                
        else:
            guessed_word = get_guessed_word(secrete_word, guessed)
            print(f'Oops. That letter is not in my word: {guessed_word}')
            max_guess -= 1

    print('Sorry, you ran out of guesses.')

def guess_loop_2(secrete_word, pictures):  ###
    guessed = ''
    max_guess = len(pictures)   ###
    while max_guess > 1: ###
        print(f'You have {max_guess-1} guesses left')
        print(pictures[-max_guess])   ###
        letter = input('Please guess a letter: ').lower()
        if letter in secrete_word:
            if letter in guessed:
                print('That letter has already been guessed')
                continue
            else:
                guessed += letter
                guessed_word = get_guessed_word(secrete_word, guessed)
                print(f'Good guess: {guessed_word}')
                if is_word_guessed(secrete_word, guessed):
                    print('Congrats, You won\n')
                    return                
        else:
            guessed_word = get_guessed_word(secrete_word, guessed)
            print(f'Oops. That letter is not in my word: {guessed_word}')
            max_guess -= 1

    print(pictures[-1]) ###
    print(f'Sorry, you ran out of guesses. My secrete word is {secrete_word}') ###


def hangman(max_guess): 
    secrete_word = choose_word()
    print("Welcome the game")
    guess_loop(secrete_word, max_guess)

def hangman_2(pictures):  ###
    secrete_word = choose_word()
    print("Welcome the game")
    guess_loop_2(secrete_word, pictures) ###


if __name__ == '__main__':
#    hangman(num_pics) ###
    hangman_2(HANGMANPICS)  ###


            
