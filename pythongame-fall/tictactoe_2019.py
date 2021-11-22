# Zhihong Zeng
# 10/26/2019

import random
import numpy as np
import copy

def create_board(size, value=' '):
    board = np.full((size,size), value)
    return board

def input_player_selection():
    letter = ''
    while letter not in ['X', 'O']:
        letter = input('Do you want to be X or O?')
        letter = letter.upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def who_go_first():
    ans = random.randint(0,1)
    if ans:
        return 'computer'
    else:
        return 'player'

def make_move(board, letter, position):
    board[position[0], position[1]] = letter

def column_won(board, letter):
    height, width = board.shape
    for x in range(width):
        won = True
        for y in range(height):
            if board[y, x] != letter:
                won = False
                break
        if won:
            return True
    return False

def row_won(board, letter):
    height, width = board.shape
    for y in range(height):
        won = True
        for x in range(width):
            if board[y, x] != letter:
                won = False
                break
        if won:
            return True
    return False
 
def column_row_won(board, letter, flag):
    height, width = board.shape
    if flag == 'column':
        list1, list2 = range(width), range(height)
    else:
        list1, list2 = range(height), range(width)

    for i in list1:
        won = True
        for j in list2:
            if flag == 'column':
                v = board[j, i]
            else:
                v = board[i, j]

            if v != letter:
                won = False
                break
        if won:
            return True
    return False
    
       
def diag_won(board, letter):
    height, width = board.shape
    won = True
    for y in range(height):
        if board[y, y] != letter:
            won = False
            break
    if won:
        return True

    won = True
    for y in range(height):
        if board[y, height-1-y] != letter:
            won = False
            break

    return won

def game_won(board, letter):
##    print(column_won(board, letter), row_won(board, letter), diag_won(board, letter))
    return column_won(board, letter) \
           or row_won(board, letter) \
           or diag_won(board, letter)

def get_available_move(board):
    height, width = board.shape
    move = []
    for y in range(height):
        for x in range(width):
            if board[y, x] == ' ':
                move.append([y, x])
    return move
    
def get_player_move(board, letter):
    height, width = board.shape
    available_move = get_available_move(board)
    move = (-1, -1)
    while move not in available_move:
        ans = input('What is your next move ? (row (0-{}), column(0-{})) '.format(height-1, width-1))
        move = ans.split(',')
        move = [int(move[0]), int(move[1])]
##        move = list(map(int, move))
    make_move(board, letter, move)

def get_random_move(board, letter):
    available_move = get_available_move(board)
    move = random.choice(available_move)
    make_move(board, letter, move)

def get_prefered_random_move(board, letter):
    available_move = get_available_move(board)
    height, width = board.shape
    prefered_move = [[int(height/2), int(width/2)], [0, 0], \
                     [0, width-1], [height-1, 0], [height-1, width-1]]
    print(available_move)
    move = None
    for p in prefered_move:
        if p in available_move:
            move = p
            break
    if move is None:
        move = random.choice(available_move)
    make_move(board, letter, move)

def get_smart_move(board, letter):
    available_move = get_available_move(board)
    win_move = get_win_defense_move(board, letter, available_move, True)
    if win_move:
        return True
    return get_win_defense_move(board, letter, available_move, False)

def get_win_defense_move(board, letter, available_move, win_defense_flag):
    if win_defense_flag: # win check
        target = letter
    else:               # defense check
        if letter == 'O':
            target = 'X'
        else:
            target = 'O'
    for move in available_move:
        board_clone = copy.deepcopy(board)
        make_move(board_clone, target, move)
        if game_won(board_clone, target):
            make_move(board, letter, move)
            return True
    return False

def tictactoe():
    print('Welcom to Tic-Tac-Toe!')
    player, computer = input_player_selection()
    print('You are {}, and computer is {}'.format(player, computer))
    first = who_go_first()
    print('{} go first'.format(first))
    board = create_board(3)
    turn = first
    while get_available_move(board):
        if turn == 'player':
            get_player_move(board, player)
            print(board)
            turn = 'computer'
            if game_won(board, player):
                print('Congratulations. You won the game')
                return
        else:
            #if not get_smart_move(board, computer):
            get_random_move(board, computer)
            print(board)
            turn = 'player'
            if game_won(board, computer):
                print('The computer won the game')
                return
    print('The game is a tie')

def tictactoe_smart():
    print('Welcom to Tic-Tac-Toe!')
    player, computer = input_player_selection()
    print('You are {}, and computer is {}'.format(player, computer))
    first = who_go_first()
    print('{} go first'.format(first))
    board = create_board(3)
    turn = first
    while get_available_move(board):
        if turn == 'player':
            get_player_move(board, player)
            print(board)
            turn = 'computer'
            if game_won(board, player):
                print('Congratulations. You won the game')
                return
        else:
            if not get_smart_move(board, computer):
                get_prefered_random_move(board, computer)
            print(board)
            turn = 'player'
            if game_won(board, computer):
                print('The computer won the game')
                return
    print('The game is a tie')
        
if __name__ == '__main__':
    tictactoe_smart()    
    


        
        
            





