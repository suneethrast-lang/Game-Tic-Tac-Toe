# Collabortors->
G Yoshithaa Sree
Narbavee
ST Suneethra 
# Tic-Tac-Toe Game

A Python implementation of the classic Tic-Tac-Toe (Noughts and Crosses) game for two players.

## Overview

This project includes multiple implementations of Tic-Tac-Toe:

1. **Terminal Edition** (active): A simple 2-player terminal-based game

## Features

### Terminal Edition (Active)
- **Two-player gameplay**: Player X vs Player O
- **Simple interface**: Play directly in the terminal
- **Input validation**: Ensures valid moves and prevents occupied cell placement
- **Win detection**: Automatically detects winning conditions (rows, columns, diagonals)
- **Draw detection**: Identifies when the board is full with no winner

### Visual Edition (Available - Currently Commented)
- **NumPy integration**: Efficient board state representation using 3×3 integer matrix
- **Matplotlib visualization**: Interactive graphical display of the board
- **Real-time updates**: Board updates instantly as players make moves
- **Win/Draw messaging**: Results displayed both in the terminal
- **Multi-game support**: Play multiple rounds without restarting

## Requirements

```
Python 3.7+
numpy (for visual edition)
matplotlib (for visual edition)
```

## Installation

1. Clone or download this repository
2. Install required packages:
   ```bash
   pip install numpy matplotlib
   ```

## Usage

### Running the Terminal Game

```bash
python use_numpy.py
```

### Game Rules

- **Players**: Two human players (Player 1: X, Player 2: O)
- **Board**: 3×3 grid with positions numbered 1-9
- **Turn-based**: Players alternate placing their mark
- **Winning**: First to get 3 marks in a row (horizontal, vertical, or diagonal) wins
- **Draw**: If all 9 cells are filled with no winner, the game is a draw

### How to Play

1. Each player enters their move when prompted
2. Enter a position number (1-9) corresponding to the board position
3. The game alternates between players until there's a winner or a draw
4. After each game, players can choose to play again

## Project Structure

```
Tic-Tac-Toe/
├── use_numpy.py          # Main game file (contains both implementations)
├── tictactoe.py          # Alternative implementation
├── README.md             # This file
```

## Code Components

### Key Functions (Terminal Edition)

- `create_board()`: Initializes an empty 3×3 board
- `display_board(board)`: Prints the current board state to the terminal
- `player_input()`: Gets player symbol choice (X or O)
- `place_mark(board, pos, player)`: Places a player's mark on the board
- `check_win(board)`: Determines if there's a winner
- `check_draw(board)`: Determines if the game is a draw

### Key Functions (Visual Edition - Commented)

- `init_board()`: Creates a fresh NumPy 3×3 matrix
- `draw_x()` / `draw_o()`: Matplotlib rendering functions for marks
- `draw_board()`: Renders the full board with grid and labels
- `check_winner()`: NumPy-based win detection
- `get_player_move()`: Interactive input with validation
- `play_game()`: Main game loop with multiple round support

## Example Gameplay

```
Choose X or O: X

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

Player 1, enter your move (1-9): 5

 1 | 2 | 3
---|---|---
 4 | X | 6
---|---|---
 7 | 8 | 9

Player 2, enter your move (1-9): 1
```

## Future Enhancements

- AI opponent (computer player)
- Difficulty levels for AI
- Game statistics/scoring
- Network multiplayer support
- Web-based version with frontend

## License

This project is provided as-is for educational purposes.

## Author

Created as a Python learning project.
