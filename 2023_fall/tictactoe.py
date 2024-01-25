import numpy as np
import random

def create_board(size, value=''):
    board = np.full((size, size), value)
    return board

def input_player_selection():
    letter = ''
    while letter not in ['X', 'O']:
        letter = input('Do you want to be X, or O? ')
        letter = letter.upper()
    
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
def who_go_first():
    ans = random.randint(0, 1)
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
            if board[y,x] != letter:
                won = False
                break

        if won:
            return True
    return False

def row_won(board, letter):
    height, width = board.shape

    for x in range(height):
        won = True

        for y in range(width):
            if board[y,x] != letter:
                won = False
                break

        if won:
            return True
    return False

def diagonal_won(board, letter):
    height, width = board.shape

    won = True
    for x in range(height):
        if board[x,x] != letter:
            won = False
            break
    if won:
        return True

    won = True
    for x in range(height):
        if board[x,height - 1 - x] != letter:
            won = False
            break
    if won:
        return True
    return False

def game_won(board, letter):
    return diagonal_won(board, letter) or row_won(board, letter) or column_won(board, letter)

def get_available_move(board):
    height, width = board.shape
    move = []

    for y in range(height):
        for x in range(width):
            if (board[y,x] == ''):
                move.append([y,x])

    return move

def get_player_move(board, letter):
    available_move = get_available_move(board)
    move = [-1,-1]

    while move not in available_move:
        ans = input(f'What is you next move (0-2),(0-2)? ')
        move = ans.split(',')
        move = [int(move[0]), int(move[1])]

    make_move(board, letter, move)

def tictactoe():
    print("Welcome to tic-tac-toe")
    player, computer = input_player_selection()
    first = who_go_first()
    print(f'{first} go first')

    board = create_board(3, '')
    turn = first

    while get_available_move(board):
        if turn == 'player':
            get_player_move(board, player)
            print(board)
            turn = 'computer'
            if game_won(board, player):
                print("player1 won")
                break

        
        if turn == 'computer':
            get_player_move(board, computer)
            print(board)
            turn = 'player'
            if game_won(board, computer):
                print("player2 won")
                break

if __name__ == '__main__':
    tictactoe()