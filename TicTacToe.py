import random
#!/usr/bin/env python
# coding: utf-8

# To take input from a user:

player1 = input("Please pick a marker 'X' or 'O'")
position = int(input('Please enter a number'))


def display_board(board):
    print('\n' * 100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
        ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


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
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


def replay():
     return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    the_board = [' ']*10
    player1,player2 = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to play?, yes or no?: ')
    if play_game == 'yes':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1,position)
            if win_check(the_board,player1):
                display_board(the_board)
                print('Player 1 has won the game!')
                game_on = False
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    game_on = False
                else:
                    turn = 'Player 2'
        # Player2's turn.
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2,position)
            if win_check(the_board,player2):
                display_board(the_board)
                print('Player 2 has won the game!')
                game_on = False
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break


# ## Good Job!






