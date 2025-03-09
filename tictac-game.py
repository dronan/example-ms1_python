from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7] + '|'+board[8] + '|'+board[9])
    print(board[4] + '|'+board[5] + '|'+board[6])
    print(board[1] + '|'+board[2] + '|'+board[3])

# test_board = [' ']*10
# test_board = ['#', 'X', 'X', 'X', 'O', ' ', 'O ', ' ', ' ', ' ']  # X's nas posições 1, 2 e 3
# display_board(test_board)


def player_input():

    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# player1_marker, player2_marker = player_input()

def place_marker(board, marker, position):
    board[position] = marker

# test_board

# place_marker(test_board, '$', 8)
# display_board(test_board)

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))

# print(win_check(test_board, 'X'))

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        try:
            position = int(input('Choose a position (1-9): '))
            if position not in range(1,10):
                print("Please, choose a position between 1 and 9! ")
            elif not space_check(board, position):
                print("This position is already in use!")
        except ValueError:
            print("Please, insert a valid value!")
    return position

def replay():
    choice = input("Play again? Enter Y or N: ")
    return choice == 'Y'

#While loop to run the game
print('Welcome to TIC TAC TOE')

while True:

    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? Y or N? ')

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':

            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has Won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("There is a TIE!")
                    game_on = False
                    break
                else:
                    turn = 'Player 2'

        else:

            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has Won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("There is a TIE!")
                    game_on = False
                    break
                else:
                    turn = 'Player 1'            

    if not replay():
        break