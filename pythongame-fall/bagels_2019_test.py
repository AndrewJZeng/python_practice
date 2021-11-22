from bagels_2019 import *

def test_get_random_number():
    print('--------test get_random_number')
    print(get_random_number(2))
    print(get_random_number(2))
    print(get_random_number(3))
    print(get_random_number(3))
    print(get_random_number(3))
    print('-------done------\n')

def test_get_player_input():
    print('--------test get_player_input')
    ans = get_player_input(3)
    print('Your guess is {}'.format(ans))
    print('--------done-----\n')

def test_get_clue():
    print('--------test get_clue------')
    data = {
        ('123', '123'): 'Won',
        ('123', '213'): 'Pico Pico Fermi',
        ('123', '230'): 'Pico Pico',
        ('123', '456'): 'Bagels'
    }
    for (guess, secrete), value in data.items():
        ans = get_clue(guess, secrete)
        if ans != value:
            print('Failure: get_clue({}, {}) is expected to be {}, \
                but got {}'.format(guess, secrete, value, ans))
            return
    print('--------Success------\n')

test_get_random_number()
test_get_player_input()
test_get_clue()
