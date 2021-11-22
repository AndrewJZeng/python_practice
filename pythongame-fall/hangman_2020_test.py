from hangman_2020 import *
from hangman_pictures import HANGMANPICS

print(choose_word())
print(choose_word())

ans = is_word_guessed('beer', 'bre')
assert ans==True, 'fail'

ans = is_word_guessed('ant', 'an')
assert ans == False, 'fail'

ans = get_guessed_word('banana', 'a')
assert ans == '_a_a_a', 'fail in get_guessed_word'

##guess_loop('dog', 3)

#hangman_2(HANGMANPICS)

print(HANGMANPICS[1])

