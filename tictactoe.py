"""
Tic-Tac-Toe Game
A two-player terminal game where Player 1 is X and Player 2 is O.
"""


# ---------------------------------------------------------------------------
# Board display
# ---------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

def display_board(board: list[list[str]]) -> None:
    """
    Print the current 3×3 board with labeled rows and columns so both
    players always know the grid coordinates.

    Example output:
           Col 1   Col 2   Col 3
         +-------+-------+-------+
    Row 1 |   X   |       |   O   |
         +-------+-------+-------+
    Row 2 |       |   X   |       |
         +-------+-------+-------+
    Row 3 |       |       |       |
         +-------+-------+-------+
    """
    print()
    print("          Col 1   Col 2   Col 3")
    print("        +-------+-------+-------+")
    for row_idx, row in enumerate(board):
        cells = "|".join(f"   {cell}   " for cell in row)
        print(f"  Row {row_idx + 1} |{cells}|")
        print("        +-------+-------+-------+")
    print()


# ---------------------------------------------------------------------------
# Game-state checks
# ---------------------------------------------------------------------------

def check_winner(board: list[list[str]], symbol: str) -> bool:
    """
    Return True if *symbol* occupies a complete row, column, or diagonal.

    Args:
        board:  The current 3×3 board.
        symbol: The player symbol to test ('X' or 'O').
    """
    # Three rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Three columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # Top-left → bottom-right diagonal
    if all(board[i][i] == symbol for i in range(3)):
        return True

    # Top-right → bottom-left diagonal
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False


def check_draw(board: list[list[str]]) -> bool:
    """
    Return True when every cell is filled (called only after check_winner
    returns False, so a full board with no winner is always a draw).

    Args:
        board: The current 3×3 board.
    """
    return all(cell != " " for row in board for cell in row)


# ---------------------------------------------------------------------------
# Move input
# ---------------------------------------------------------------------------

def get_player_move(
    board: list[list[str]],
    player_name: str,
    symbol: str,
) -> tuple[int, int]:
    """
    Prompt the active player for a valid move and return its 0-based indices.

    The player enters a row number and a column number on separate prompts,
    each in the range 1–3.  Invalid input (non-integer, out-of-range, or an
    already-occupied cell) is rejected with a descriptive error message, and
    the player is asked again.

    Args:
        board:       The current 3×3 board.
        player_name: Human-readable name, e.g. "Player 1".
        symbol:      The player's mark ('X' or 'O').

    Returns:
        A ``(row, col)`` tuple of 0-based indices.
    """
    print(f"  {player_name} ({symbol}) — it's your turn.")

    while True:
        try:
            row_raw = input("    Enter Row    (1, 2, or 3): ").strip()
            row = int(row_raw)
            if not (1 <= row <= 3):
                print("    ✗  Row must be 1, 2, or 3. Try again.\n")
                continue

            col_raw = input("    Enter Column  (1, 2, or 3): ").strip()
            col = int(col_raw)
            if not (1 <= col <= 3):
                print("    ✗  Column must be 1, 2, or 3. Try again.\n")
                continue

        except ValueError:
            print("    ✗  Please enter a whole number (1, 2, or 3). Try again.\n")
            continue

        # Convert to 0-based indices
        r, c = row - 1, col - 1

        if board[r][c] != " ":
            occupant = "X" if board[r][c] == "X" else "O"
            print(
                f"    ✗  Row {row}, Col {col} is already occupied by {occupant}. "
                "Pick an empty cell.\n"
            )
            continue

        return r, c


# ---------------------------------------------------------------------------
# Single-game loop
# ---------------------------------------------------------------------------

def play_game() -> None:
    """
    Run one complete game of Tic-Tac-Toe.

    Player 1 always goes first as X; Player 2 is O.  The board is shown
    before the first move and after every subsequent move.  When the game
    ends the result is announced using the player's full name and symbol.
    """
    board: list[list[str]] = [[" "] * 3 for _ in range(3)]

    # Map turn index → (display name, symbol)
    players: list[tuple[str, str]] = [
        ("Player 1", "X"),
        ("Player 2", "O"),
    ]
    current = 0  # 0 → Player 1, 1 → Player 2

    print("\n" + "=" * 48)
    print("            🎮   NEW GAME STARTING")
    print("=" * 48)
    print("  Player 1 plays as  X")
    print("  Player 2 plays as  O")
    print("-" * 48)

    display_board(board)

    while True:
        player_name, symbol = players[current]

        r, c = get_player_move(board, player_name, symbol)
        board[r][c] = symbol

        display_board(board)

        if check_winner(board, symbol):
            print(f"  🏆  {player_name} ({symbol}) wins! Congratulations!\n")
            break

        if check_draw(board):
            print("  🤝  It's a draw! Both players played well!\n")
            break

        # Alternate turns
        current = 1 - current


# ---------------------------------------------------------------------------
# Play-again prompt
# ---------------------------------------------------------------------------

def _ask_play_again(player_name: str) -> bool:
    """
    Ask a single player whether they want another game.

    Returns:
        True if the player agrees to play again, False otherwise.
    """
    while True:
        answer = input(
            f"  {player_name}, would you like to play again? (yes / no): "
        ).strip().lower()

        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False

        print("  ✗  Please type 'yes' or 'no'.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """
    Print the welcome banner, then loop: play a game and ask both players
    whether they want another round.  The session ends only when at least
    one player declines.
    """
    print()
    print("=" * 48)
    print("       🎮  WELCOME TO TIC-TAC-TOE!  🎮")
    print("=" * 48)
    print()
    print("  HOW TO PLAY")
    print("  ───────────")
    print("  • The board has 3 rows and 3 columns,")
    print("    each numbered 1 to 3.")
    print()
    print("  • When it is your turn, you will be asked")
    print("    to enter a Row number and a Column number.")
    print()
    print("  • Example: to place your mark in the middle")
    print("    cell, enter  Row: 2  then  Col: 2.")
    print()
    print("  • Player 1 is X  —  Player 2 is O.")
    print("  • Player 1 always goes first.")
    print()
    print("  • Get three of your marks in a row, column,")
    print("    or diagonal to WIN!")
    print("=" * 48)

    while True:
        play_game()

        # Both players must agree to continue
        p1_wants = _ask_play_again("Player 1")
        p2_wants = _ask_play_again("Player 2")

        if p1_wants and p2_wants:
            print("\n  Great! Starting a new game…")
        else:
            print("\n  Thanks for playing! Goodbye! 👋\n")
            break


if __name__ == "__main__":
    main()
