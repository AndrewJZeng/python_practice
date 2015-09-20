theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
def checkalltiles(board):
    blankspace = 9
    if not board['top-L'] == ' ':
        blankspace -= 1
    if not board['top-M'] == ' ':
        blankspace -= 1
    if not board['top-R'] == ' ':
        blankspace -= 1
    if not board['mid-L'] == ' ':
        blankspace -= 1
    if not board['mid-M'] == ' ':
        blankspace -= 1
    if not board['mid-R'] == ' ':
        blankspace -= 1
    if not board['low-L'] == ' ':
        blankspace -= 1
    if not board['low-M'] == ' ':
        blankspace -= 1
    if not board['low-R'] == ' ':
        blankspace -= 1
    return blankspace
def checkWinner():
	return
turn = 'X'
while True:
    printboard(theBoard)
    blankspace = 9
    blankspace = checkalltiles(theBoard)
    if blankspace == 0:
        break
    print(blankspace)
    move = ""
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    str(move)
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'