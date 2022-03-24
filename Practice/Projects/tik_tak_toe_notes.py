row0 = [" ", " ", " "]
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]


def display(row1, row2, row3):
    print(row0)
    print(row1)
    print(row2)


display(row0, row1, row2)


def user_row():
    row = "ROW"
    row_range = range(0, 3)
    valid_range = False

    while row.isdigit() == False or valid_range == False:
        row = input("Enter a row number (0-2)\n")

        # Digit Check
        if row.isdigit() == False:
            print("Not a number")

        # Range Check
        if row.isdigit() == True:
            if int(row) in row_range:
                valid_range = True
            else:
                print("Not in range")
    return int(row)


def user_col():
    col = "COLUMN"
    col_range = range(0, 3)
    valid_range = False

    while col.isdigit() == False or valid_range == False:
        col = input("Enter a column number (0-2)\n")

        # Digit Check
        if col.isdigit() == False:
            print("Not a number")

        # Range Check
        if col.isdigit() == True:
            if int(col) in col_range:
                valid_range = True
            else:
                print("Not in range")
    return int(col)


def user_shape():
    allowed_shapes = ["X", "O"]
    valid_shape = False
    while valid_shape == False:
        shape = input("Enter X or O\n").upper()
        if shape in allowed_shapes:
            valid_shape = True
        else:
            print("Not X or O")
    return shape


input_row = user_row()
input_col = user_col()
input_shape = user_shape()
print(input_row, input_col, input_shape)


def space_check(board, position):
    position = int(position)
    return board[position - 1] == "#"


def player_choice(board):
    position = "POSITION"
    position_range = range(1, 10)
    valid_range = False

    while (
        position.isdigit() == False
        or valid_range == False
        or not space_check(board, position)
    ):

        num = input("Enter a location on the board (1-9)\n")
        # Digit Check
        if num.isdigit() == False:
            print("Not a valid number")

        # Range Check
        elif int(num) not in position_range:
            print("Not in range")
        else:
            valid_range = True
            position = num

    return int(position)
