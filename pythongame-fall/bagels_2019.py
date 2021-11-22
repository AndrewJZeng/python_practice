# Zhihong Zeng
# 11/23/2019

import random

NUM_DIGIT = 3
MAX_GUESS = 10

def get_random_number(size):
    nums = list(range(1, 10))
    random.shuffle(nums)
    ans = ''
    for x in nums[:size]:
        ans += str(x)
    return ans

def get_player_input(size):
    ans = ''
    while len(ans) != size or not ans.isdigit():
        ans = input(f'Make a guess ({size} digits): \n')
    return ans

def get_clue(guess, secrete_number):
    if guess == secrete_number:
        return 'Won'

    clue = []
    for i, x in enumerate(guess):
        if x == secrete_number[i]:
            clue.append('Fermi')
        elif x in secrete_number:
            clue.append('Pico')

    if not clue:
        return 'Bagels'
    else:
        return ' '.join(clue)

def introduction():
    intro = f'''
    I am thinking of a {NUM_DIGIT}-digit number. Try to guess what it is.
    The clues I give are...
    When I say:    That means:
    Bagels       None of the digits is correct.
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    I have thought up a number. You have {MAX_GUESS} guesses to get it.
    '''
    
    print(intro)

def bagels_game():
    introduction()
    secrete = get_random_number(NUM_DIGIT)

    for i in range(MAX_GUESS):
        print(f'\n#{i+1}:')
        ans = get_player_input(NUM_DIGIT)
        clue = get_clue(ans, secrete)
        if clue == 'Won':
            print('Congrats! You got it.')
            return
        else:
            print(clue)

    print('You ran out of guesses. The answer was {}'.format(secrete))
        
if __name__ == '__main__':
    bagels_game()

    


