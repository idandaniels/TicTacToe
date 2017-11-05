from IPython.display import clear_output


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
        print('X', 'O')
    else:
        print('O', 'X')




player_input()
#print_board(board)





