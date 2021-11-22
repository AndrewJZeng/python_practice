import random
import time

def displayIntro():
    print('Game start')

def chooseCave():
    cave = ''
    while cave not in ['1', '2']:
        cave = input('Which cave will go into? (1 or 2)')
    return cave

def checkCave(chosenCave):
    print('A large dragon jumps out')
    time.sleep(2)
    number = random.randint(1,2)
    if number == int(chosenCave):
        print('Gives you his treasure')
    else:
        print('Gobbles you down in one bite')

if __name__ == '__main__':
    playAgain = 'yes'
    while 
