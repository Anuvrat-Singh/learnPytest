from IPython.display import clear_output
import random


def display_board(board):

    print(board[7]+ '|' + board[8] + '|' + board[9])
    print("------")
    print(board[4]+ '|' + board[5] + '|' + board[6])
    print("------")
    print(board[1]+ '|' + board[2] + '|' + board[3])


testBoard = ['#','1','2','3','4','5','6','7','8','9']
display_board(testBoard)


def player_input():
    marker = ''
    while marker != 'x' and marker != 'o':
        marker=input("Enter x or o: ")


    player1 = marker

    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'

    return player1, player2


# player1, player2 = player_input()


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (
            (board[1] == board[2] == board[3] == mark)          #1st row
            or (board[4] == board[5] == board[6] == mark)       #2nd row
            or (board[7] == board[8] == board[9] == mark)       #3rd row
            or (board[1] == board [4] == board[9] == mark)      #1st column
            or (board[2] == board[5] == board[8] == mark)       #2nd column
            or (board[3] == board[6] == board[9] == mark)       #3rd column
            or (board[1] == board[5] == board[9] == mark)       #1st diag
            or (board[3] == board[5] == board[7] == mark)       #2nd diag
            )


win_check(testBoard, 'X')


def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def check_space(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def full_board_check(board):
    for i in range(1,10):
        if check_space(board, i):
            return False

    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5,6 ,7,8,9] or not check_space(board, position):
        position = int(input("Choose Position between 1-9 : "))

    return position


def replay():
    choice = input("Do you want to play again: 'Yes' or 'No'")
    return  choice == 'Yes'


print("Welcome to tic tac toe game:")

while True:

    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()

    print(turn + " will go first")

    play_game = input('Ready to Play? y or n ?')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                print("Player 1 has won")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tied")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            if turn == 'Player 2':
                display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                print("Player 2 has won")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tied")
                    game_on = False
                else:
                    turn = 'Player 1'


    if not replay():
        break


