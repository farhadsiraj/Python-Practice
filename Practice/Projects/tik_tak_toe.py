import random

# Board with numerical positions
number_board = list(range(1, 10))

# Empty board
game_board = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]

# Displays the numerical positions on the left and the game board on the right
def display_board(board):
    print(1, 2, 3, " ", board[0], board[1], board[2])
    print(4, 5, 6, " ", board[3], board[4], board[5])
    print(7, 8, 9, " ", board[6], board[7], board[8], "\n")


test_board = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
# display_board(test_board)
# display_board(number_board)
# display_board(game_board)

# Player 1 chooses marker
def player_input():
    marker = ""

    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: Do you want to be X or O?\n").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


# Places current player's maker on the chosen position
def place_marker(board, marker, position):
    board[position - 1] = marker


# place_marker(test_board, "$", 9)
# display_board(test_board)

# Checks if the given mark won
def win_check(board, mark):

    return (
        (board[0] == mark and board[1] == mark and board[2] == mark)
        or (board[3] == mark and board[4] == mark and board[5] == mark)
        or (board[6] == mark and board[7] == mark and board[8] == mark)
        or (board[0] == mark and board[3] == mark and board[6] == mark)
        or (board[1] == mark and board[4] == mark and board[7] == mark)
        or (board[2] == mark and board[5] == mark and board[8] == mark)
        or (board[2] == mark and board[4] == mark and board[6] == mark)
        or (board[0] == mark and board[4] == mark and board[8] == mark)
    )


# display_board(test_board)
# print(win_check(test_board, "X"))
# print(win_check(test_board, "O"))

# Randomly chooses which player goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 2"
    else:
        return "Player 1"


# Checks if the chosen position is available
def space_check(board, position):
    position = int(position)
    return board[position - 1] == "#"


# Checks if the board is full
def full_board_check(board):
    for i in range(0, 9):
        if space_check(board, i):
            return False
    return True


# Current player chooses numerical position on board
def player_choice(board):
    position = 0
    board_range = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    while position not in board_range or not space_check(board, position):
        position = input("Choose your next position: (1-9) ")

        # Digit Check
        if position.isdigit() == False:
            print("Not a number")

        # Range Check
        elif position not in board_range:
            print("Not in range")

        # Space Check
        elif space_check(board, position) == False:
            print("Not a valid move")
        else:
            pass
    return int(position)


def replay():

    return (
        input("Do you want to play again? Enter Yes or No: \n").lower().startswith("y")
    )


print("Welcome to Tic Tac Toe!")

while True:
    # Reset the board
    theBoard = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")

    play_game = input("Are you ready to play? Enter Yes or No.\n")

    if play_game.lower()[0] == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Congratulations! You have won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 2"

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break
