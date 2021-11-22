import random
import time

def displayIntro():
    print('''
            you see two caves.
            In one cave, the dragon is friendly. 
            In the other cave, the other dragon is greedy and hungry.
            ''')

def chooseCave():
    cave = ''
    while cave not in ['1', '2']:
        cave = input('Which cave will you go into? (1 or 2) ')
    return cave

def checkCave(chosenCave):
    print('A large dragon jumps out in front of you! He opens his jaws and...\n')
    time.sleep(2)
    number = random.randint(1, 2)
    if chosenCave == str(number):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

if __name__ == '__main__':
    playAgain = 'yes'
    while playAgain.startswith('y'):
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
        print()
        playAgain = input('Do you want to play again? (yes or no)')        

