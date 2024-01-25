from tictactoe import *

print('\n---Test Create board')
print(create_board(3, ' '))
print(create_board(2, 5))
print(create_board(4))

# print('\ntest player selection')
# print(input_player_selection())

print('\ntest who go first')
print(who_go_first())
print(who_go_first())
print(who_go_first())

print('\ntesting make move')
b = create_board(3)
print(b)
make_move(b, 'x', [0,0])
print(b)

print('\ntesting column won')
b = create_board(3)
print(b)
make_move(b, 'x', [0,0])
print(column_won(b,'x'))
make_move(b, 'x', [1,0])
make_move(b, 'x', [2,0])
print(b)
print(column_won(b,'x'))