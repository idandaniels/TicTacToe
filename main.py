from IPython.display import clear_output
import random

board = ['undefine', 'O', 'O','O', 'X', 'X', 'X', 'O', 'O', 'O']

#define functions
def print_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def player_input():
    marker = ' '
    while not( marker == 'X' or marker =='O'):
        marker = input('Do you want it to be x or o?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return('O', 'X')
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or
    (board[4] == marker and board[5] == marker and board[6] == marker) or
    (board[1] == marker and board[2] == marker and board[3] == marker) or
    (board[7] == marker and board[5] == marker and board[3] == marker) or
    (board[9] == marker and board[5] == marker and board[1] == marker) or
    (board[1] == marker and board[4] == marker and board[7] == marker) or
    (board[9] == marker and board[6] == marker and board[3] == marker))

def choose_first():
    if random.randint(0,1) ==0:
        return('Player 1')
    else:
        return('Player 2')





#player_input()
#print_board(board)
print(choose_first())




