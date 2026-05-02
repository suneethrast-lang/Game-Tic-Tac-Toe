# Collabortors->
G Yoshithaa Sree

Narbavee

ST Suneethra 

# Tic-Tac-Toe Game

A Python implementation of the classic Tic-Tac-Toe (Noughts and Crosses) game for two players.

## Overview

This project includes multiple implementations of Tic-Tac-Toe:
1. **Terminal Edition** (active): A simple 2-player terminal-based game with an intuitive interface

## Features

### Terminal Edition (Active)
- ✅ **Two-player gameplay**: Players compete as X and O
- ✅ **Simple interface**: Easy-to-use terminal display
- ✅ **Input validation**: Validates moves and prevents invalid placements
- ✅ **Win detection**: Automatically detects winners (rows, columns, diagonals)
- ✅ **Draw detection**: Identifies draw conditions
- ✅ **Multi-game support**: Play multiple consecutive games
- ✅ **Clear board display**: 3×3 grid shown after each move

### Visual Edition (Available - Currently Commented)

- Real-time board visualization
- Win/Draw messaging on plots
- Multi-round support

## Requirements

```
Python 3.7+
```

## Installation

1. Clone or download this repository

## Usage

### Running the Game

```bash
python use_numpy.py
```

## Game Rules

- **Players**: Two human players choose X or O at the start
- **Board**: 3×3 grid with positions numbered 1-9
- **Positions**: 
  ```
   1 | 2 | 3
  ---|---|---
   4 | 5 | 6
  ---|---|---
   7 | 8 | 9
  ```
- **Turn-based**: Players alternate placing their mark
- **Winning**: First to get 3 marks in a row (horizontal, vertical, or diagonal) wins
- **Draw**: If all 9 cells are filled with no winner, the game is a draw
- **Replay**: After each game, both players can choose to play again

## How to Play

1. Run the script: `python use_python.py.`
2. Choose your symbol: Enter `X` or `O`
3. Players alternate turns
4. When prompted, enter a position number (1-9) to place your mark
5. The board updates after each move
6. Game ends when someone wins, or the board is full (draw)
7. Choose whether to play again

## Project Structure

```
Tic-Tac-Toe/
├── use_python.py          # Main game file (both implementations)
└── README.md             # This file
```

## Code Components

### Key Functions (Terminal Edition)

| Function | Purpose |
|----------|---------|
| `show_board()` | Initializes an empty 3×3 board |
| `choose()` | Prompts players to choose X or O |
| `get_move(player_name, mark)` | Places a player's mark on the board, if the position is empty, else enter another position |
| `check_win(mark)` | Checks whether PlayerX or PlayerO wins or not |
| `play()` | Main game loop for one complete game |

## Example Gameplay

```
Welcome to Tic Tac Toe
Choose X or O: X

 
   |   |   
---|---|---
   |   |   
---|---|---
   |   |   
 

Player X's turn
Enter position (1-9): 5

 
   |   |   
---|---|---
   | X |   
---|---|---
   |   |   
 

Player O's turn
Enter position (1-9): 1

 
 O |   |   
---|---|---
   | X |   
---|---|---
   |   |   
 

...

 X | O | X
---|---|---
 O | X |  
---|---|---
   | O | X

Player X wins!
Enter 1, to continue: 0
```

## Win Conditions

The game checks for wins in 8 different patterns:
- **3 Rows**: `[0,1,2]`, `[3,4,5]`, `[6,7,8]`
- **3 Columns**: `[0,3,6]`, `[1,4,7]`, `[2,5,8]`
- **2 Diagonals**: `[0,4,8]`, `[2,4,6]`

## Future Enhancements

- AI opponent with difficulty levels
- Game statistics and scoring
- Network multiplayer support
- GUI with tkinter
- Web-based version

## License

This project is provided as-is for educational purposes.

## Author

Created as a Python learning project.
