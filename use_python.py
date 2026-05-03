"""
Tic-Tac-Toe — Python visual edition
=================================================
Board state  : numpy 3x3 int matrix  (0 = empty, 1 = X, -1 = O)
Player input: Terminal prompts (Row 1-3, Col 1-3)
"""

# -------------------------------
# CREATE A BOARD
# -------------------------------

def create_board():
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

# ------------------------------------------
# SHOW THE BOARD (which is aligned properly)
# ------------------------------------------
#print coloumn and row labels, with lines
def show_board(board):
    print("\n       Col 1   Col 2   Col 3")
    print("      +-------+-------+-------+")

    for i in range(3):
        print("Row", i+1, "|  {:^3}  |  {:^3}  |  {:^3}  |".format(
            board[i][0], board[i][1], board[i][2]
        ))
        print("      +-------+-------+-------+")


# -------------------------------
# CHOOSE X OR O
# -------------------------------

def choose():
    while True:
        choice = input("Player 1 choose X or O: ").upper()

        if choice == "X": #Player 1 is X, Player 2 is O
            return "X", "O"  
        elif choice == "O":
            return "O", "X" #Player 1 is O, Player 2 is X
        else: #invalid input
            print("Enter only X or O !")


# -------------------------------
# GET MOVE (Safe input ,no crash)
# -------------------------------
def get_move(player_name, mark,board):
    while True:
        try:
            #shows whose turn it is
            print("\n", player_name, "(", mark, ") turn")

            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            
            #check if row and coloumn are within range
            if row in range(3) and col in range(3):

                #check if the position is empty
                if board[row][col] == " ":
                    return row, col #valid
                    
                else:
                    print("That place is already filled")
            else:
                print("Enter numbers between 1 and 3")

        except: #if you use the wrong datatype, anyhting other than number
            print("Wrong input, enter numbers only")


# -------------------------------
# CHECK WHETHER SOMEONE WON
# -------------------------------
def check_win(board,mark): #if true , game ends
    # Check for Rows
    for row in board:
        if row[0] == row[1] == row[2] == mark:
            return True

    # Check for Columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True

    # Check for Diagonals
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    #if there is no win
    return False


# -------------------------------
# MAIN GAME
# -------------------------------
def play(): #runs one full game

    board = create_board()
    
    p1 = "Player 1"
    p2 = "Player 2"

    mark1, mark2 = choose() #chooses which player gets which mark

    current_name = p1 #start with player 1
    current_mark = mark1

    for turn in range(9): #as the board is 3x3
        #shows current board
        show_board(board)

        #gets and places the mark on the board
        row,col = get_move(current_name, current_mark,board)
        board[row][col] = current_mark

        #check whether player won
        if check_win(board,current_mark):
            show_board(board)
            print(current_name, "wins!")
            if current_name == "Player 1":
                return 1
            else:
                return 2
            #ends the game

        # Switch player
        if current_name == p1:
            current_name = p2
            current_mark = mark2
        else:
            current_name = p1
            current_mark = mark1

    #if all nine moves are made and there is no winner
    show_board(board)
    print("Draw game")
    return 0


# -------------------------------
# REPLAY LOOP
# -------------------------------

p1_score = 0
p2_score = 0
while True:
    result = play()

    # updates the scores
    if result == 1:
        p1_score += 1
    elif result == 2:
        p2_score += 1

    # shows the scores
    print("\nScore:")
    print("Player 1:", p1_score)
    print("Player 2:", p2_score)

    choice = input("Play again? (yes/no): ").lower()

    if choice != "yes":
        print("Game ended.")
        break
