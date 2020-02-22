def check3inRow(board, symbol):
    for row in board:
        # row[0], row[1], row[2]
        if row[0] == row[1] == row[2] == symbol:
            print("you won!")
            return True


def check3inColumn(board, symbol):
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            print("you won!")
            return True


def checkDiagonal1(board, symbol):
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        print("you won!")
        return True


def checkDiagonal2(board, symbol):
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        print("you won!")
        return True


def pretty_print(board):
    for row in board:
        print(row)


def TicTacToe():
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

    # your code goes here

    row = 0
    column = 0
    count = 0
    loop = True
    while loop and count < 9:
        symbol = input("are you X or O: ")
        row = int(input("row: "))
        column = int(input("column: "))
        row_chosen = board[row]
        if row_chosen[column] == '-':
            row_chosen[column] = symbol

            won = check3inRow(board, symbol) or check3inColumn(board, symbol) or checkDiagonal1(board,
                                                                                                symbol) or checkDiagonal2(
                board, symbol)

            if won:
                loop = False


        else:
            print("choose another position: ")

        count += 1
        pretty_print(board)

    return board


TicTacToe()


def check3inColumn(board, symbol):
    for column in board:
        # [0], row[1], row[2]
        if column[0] == column[1] == column[2] == symbol:
            print("won")
# board = TicTacToe()
# check3XinRow()



