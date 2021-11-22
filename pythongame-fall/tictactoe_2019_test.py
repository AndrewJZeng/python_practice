from tictactoe_2019 import *

print('\n-----Test create_board\n')
print(create_board(3))
print(create_board(5))

print('\n-----test input_player_letter\n')
print(input_player_selection())

print('\n-----test who_go_first\n')
print(who_go_first())
print(who_go_first())
print(who_go_first())

print('\n-----test make_move\n')
board = create_board(3)
make_move(board, 'X', (0, 0))
print(board)
make_move(board, 'O', (2, 2))
print(board)

print('\n-----test column_won\n')
board = create_board(3)
print(board)
ans = column_won(board, 'X')
assert not ans, 'Fail'
board[0, 0] = 'X'
board[1, 0] = 'X'
board[2, 0] = 'X'
print(board)
ans = column_won(board, 'X')
assert ans, 'Fail'
ans = column_row_won(board, 'X', 'column')
assert ans, 'Fail'
                     

print('\n-----test row_won\n')
board = create_board(3)
print(board)
ans = row_won(board, 'X')
assert not ans, 'Fail'
board[1, 0] = 'X'
board[1, 1] = 'X'
board[1, 2] = 'X'
print(board)
ans = row_won(board, 'X')
assert ans, 'Fail'
ans = column_row_won(board, 'X', 'row')
assert ans, 'Fail'

print('\n-----test diag_won\n')
board = create_board(3)
print(board)
ans = diag_won(board, 'X')
assert not ans, 'Fail'
board[0, 0] = 'X'
board[1, 1] = 'X'
board[2, 2] = 'X'
print(board)
ans = diag_won(board, 'X')
assert ans, 'Fail'

board = create_board(3)
print(board)
ans = diag_won(board, 'X')
assert not ans, 'Fail'
board[0, 2] = 'X'
board[1, 1] = 'X'
board[2, 0] = 'X'
print(board)
ans = diag_won(board, 'X')
assert ans, 'Fail'

print('\n------test game_won\n')
board = create_board(3)
ans = game_won(board, 'X')
assert not ans, 'Fail'
board[0, 2] = 'X'
board[1, 2] = 'X'
board[2, 2] = 'X'
ans = game_won(board, 'X')
assert ans, 'Fail'
print('\n==== Success====\n')

print('\n-----test get_available_move\n')
board = create_board(3)
board[0, 0] = 'X'
board[1, 1] = 'O'
board[2, 2] = 'O'
ans = get_available_move(board)
print(board)
print('available_move: {}'.format(ans))

print('\n-----test get_player_move\n')
board = create_board(3)
print(board)
get_player_move(board, 'X')
print(board)

print('\n--------test get_random_move\n')
board = create_board(3)
get_random_move(board, 'O')
print(board)
board = create_board(3)
get_random_move(board, 'O')
print(board)
print('\n==== Success====\n')

print('\n--------test get_smart_move\n')
board = create_board(3)
board[1, 0:2] = ['X', 'X']
print(board)
get_smart_move(board, 'X')
print(board)
assert game_won(board, 'X'), 'Fail'
board = create_board(3)
board[1, 0:2] = ['O', 'O']
print(board)
get_smart_move(board, 'X')
print(board)
assert not game_won(board, 'X'), 'Fail'
print('\n==== Success====\n')

    

      


