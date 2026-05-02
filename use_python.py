"""
Tic-Tac-Toe — Python visual edition
=================================================
Board state  : numpy 3x3 int matrix  (0 = empty, 1 = X, -1 = O)
Player input: Terminal prompts (Row 1-3, Col 1-3)
"""

# Empty board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Show board (aligned properly)
def show_board():
    print("\n      Col 1   Col 2   Col 3")
    print("    +-------+-------+-------+")

    for i in range(3):
        print("Row", i+1, "|  {:^3}  |  {:^3}  |  {:^3}  |".format(
            board[i][0], board[i][1], board[i][2]
        ))
        print("    +-------+-------+-------+")


# Choose X or O
def choose():
    while True:
        choice = input("Player 1 choose X or O: ").upper()

        if choice == "X":
            return "X", "O."
        elif choice == "O":
            return "O", "X."
        else:
            print("Enter only X or O")


# Safe input (no crash)
def get_move(player_name, mark):
    while True:
        try:
            print("\n", player_name, "(", mark, ") turn")

            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1

            if row in range(3) and col in range(3):
                if board[row][col] == " ":
                    return row, col
                else:
                    print("That place is already filled")
            else:
                print("Enter numbers between 1 and 3")

        except:
            print("Wrong input, enter numbers only")


# Check win
def check_win(mark):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] == mark:
            return True

    # Columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True

    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    return False


# Main game
def play():
    p1 = "Player 1"
    p2 = "Player 2"

    mark1, mark2 = choose()

    current_name = p1
    current_mark = mark1

    for turn in range(9):
        show_board()

        row, col = get_move(current_name, current_mark)
        board[row][col] = current_mark

        if check_win(current_mark):
            show_board()
            print(current_name, "wins!")
            return

        # Switch player
        if current_name == p1:
            current_name = p2
            current_mark = mark2
        else:
            current_name = p1
            current_mark = mark1

    show_board()
    print("Draw game")


# Start
play()
