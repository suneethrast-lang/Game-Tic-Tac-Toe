"""
Tic-Tac-Toe — NumPy + Matplotlib visual edition
=================================================
Board state  : numpy 3x3 int matrix  (0 = empty, 1 = X, -1 = O)
Rendering    : Matplotlib interactive window (plt.ion)
Player input : Terminal prompts (Row 1-3, Col 1-3)
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PLAYER_1 = 1          # X
PLAYER_2 = -1         # O
EMPTY    = 0

PLAYER_INFO: dict[int, tuple[str, str]] = {
    PLAYER_1: ("Player 1", "X"),
    PLAYER_2: ("Player 2", "O"),
}


# ---------------------------------------------------------------------------
# Board initialisation
# ---------------------------------------------------------------------------

def init_board() -> np.ndarray:
    """Return a fresh 3x3 NumPy integer matrix of zeros."""
    return np.zeros((3, 3), dtype=int)


# ---------------------------------------------------------------------------
# Matplotlib drawing helpers
# ---------------------------------------------------------------------------

def draw_x(ax: plt.Axes, row: int, col: int) -> None:
    """
    Draw an X mark inside the cell at (row, col) — both 0-indexed.

    The cell's centre in axes coordinates is (col + 0.5, 2.5 - row).
    Two diagonal lines are drawn with a small padding from the cell edges.
    """
    pad  = 0.18
    left  = col + pad
    right = col + 1 - pad
    top   = 2 - row + 1 - pad   # y increases upward; Row 0 is at top
    bot   = 2 - row + pad

    line_kw = dict(linewidth=3.5, solid_capstyle="round", zorder=3)
    ax.plot([left, right], [top, bot],  **line_kw)   # \ diagonal
    ax.plot([left, right], [bot,  top], **line_kw)   # / diagonal


def draw_o(ax: plt.Axes, row: int, col: int) -> None:
    """
    Draw an O mark (circle) inside the cell at (row, col) — both 0-indexed.
    """
    cx = col + 0.5
    cy = (2 - row) + 0.5

    circle = mpatches.Circle(
        (cx, cy),
        radius=0.30,
        fill=False,
        linewidth=3.5,
        zorder=3,
    )
    ax.add_patch(circle)


def draw_board(board: np.ndarray, title: str = "") -> None:
    """
    Clear the current figure and redraw the full board state.

    Grid layout (axes coordinates run 0-3 on both axes; y increases upward):
      • Column labels (Col 1 / 2 / 3) at the top
      • Row labels    (Row 1 / 2 / 3) on the left side
      • Grid lines at integer positions
      • Existing marks are redrawn from the board matrix

    Args:
        board: The current 3x3 NumPy board.
        title: Optional message shown as the axes title (e.g., winner text).
    """
    plt.clf()
    ax: plt.Axes = plt.gca()
    fig = plt.gcf()
    
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_aspect("equal")
    ax.axis("off")

    # --- Grid lines ---
    grid_kw = dict(linewidth=2, zorder=1)
    for i in range(4):
        ax.axhline(i, xmin=0, xmax=1, **grid_kw)
        ax.axvline(i, ymin=0, ymax=1, **grid_kw)

    # --- Column labels (above top row) ---
    for col_idx in range(3):
        ax.text(
            col_idx + 0.5, 3.18,
            f"Col {col_idx + 1}",
            ha="center", va="bottom",
            fontsize=11, fontweight="bold"
        )

    # --- Row labels (left of each row) ---
    for row_idx in range(3):
        y_center = (2 - row_idx) + 0.5   # row 0 → y≈2.5, row 2 → y≈0.5
        ax.text(
            -0.12, y_center,
            f"Row {row_idx + 1}",
            ha="right", va="center",
            fontsize=11, fontweight="bold",
        )

    # --- Marks ---
    for r in range(3):
        for c in range(3):
            if board[r, c] == PLAYER_1:
                draw_x(ax, r, c)
            elif board[r, c] == PLAYER_2:
                draw_o(ax, r, c)

    # --- Optional title (winner / draw message) ---
    if title:
        ax.set_title(title, fontsize=14, fontweight="bold",pad=16)

    plt.tight_layout()
    plt.draw()
    plt.pause(0.05)


# ---------------------------------------------------------------------------
# Win / draw detection (NumPy-based)
# ---------------------------------------------------------------------------

def check_winner(board: np.ndarray) -> int | None:
    """
    Return the winning player constant (1 or -1) or None if no winner yet.

    Win conditions checked using NumPy sums:
      • Any row sum   == ±3
      • Any column sum == ±3
      • Main diagonal sum (np.trace) == ±3
      • Anti-diagonal sum (np.trace of flipped board) == ±3
    """
    target = 3  # board size

    # Row sums
    row_sums = board.sum(axis=1)
    if  target in row_sums: return PLAYER_1
    if -target in row_sums: return PLAYER_2

    # Column sums
    col_sums = board.sum(axis=0)
    if  target in col_sums: return PLAYER_1
    if -target in col_sums: return PLAYER_2

    # Main diagonal
    diag = int(np.trace(board))
    if diag ==  target: return PLAYER_1
    if diag == -target: return PLAYER_2

    # Anti-diagonal
    anti = int(np.trace(np.fliplr(board)))
    if anti ==  target: return PLAYER_1
    if anti == -target: return PLAYER_2

    return None


def check_draw(board: np.ndarray) -> bool:
    """
    Return True when every cell is occupied and there is no winner.

    Args:
        board: The current 3x3 NumPy board.
    """
    return bool(np.all(board != EMPTY))


# ---------------------------------------------------------------------------
# Player input
# ---------------------------------------------------------------------------

def get_player_move(player: int, board: np.ndarray) -> tuple[int, int]:
    """
    Prompt the active player for a valid move and return 0-based (row, col).

    Validates:
      • Non-integer input
      • Out-of-range values (must be 1, 2, or 3)
      • Already-occupied cells

    Args:
        player: PLAYER_1 (1) or PLAYER_2 (-1).
        board:  Current 3x3 NumPy board (used for occupancy check).

    Returns:
        ``(row, col)`` tuple of 0-based indices.
    """
    name, symbol = PLAYER_INFO[player]
    print(f"\n  {name} ({symbol}) — your turn.")

    while True:
        # --- Row ---
        try:
            row = int(input("    Enter Row    (1, 2, or 3): ").strip())
        except ValueError:
            print("    ✗  Please enter a whole number (1, 2, or 3).")
            continue

        if row not in (1, 2, 3):
            print("    ✗  Row must be 1, 2, or 3.")
            continue

        # --- Column ---
        try:
            col = int(input("    Enter Column  (1, 2, or 3): ").strip())
        except ValueError:
            print("    ✗  Please enter a whole number (1, 2, or 3).")
            continue

        if col not in (1, 2, 3):
            print("    ✗  Column must be 1, 2, or 3.")
            continue

        # --- Occupancy ---
        r, c = row - 1, col - 1
        if board[r, c] != EMPTY:
            occupant_name, occupant_sym = PLAYER_INFO[board[r, c]]
            print(
                f"    ✗  Row {row}, Col {col} is already occupied "
                f"by {occupant_name} ({occupant_sym}). Pick an empty cell."
            )
            continue

        return r, c


# ---------------------------------------------------------------------------
# Main game loop
# ---------------------------------------------------------------------------

def play_game() -> None:
    """
    Run one or more complete games in a live Matplotlib window.

    Flow per game:
      1. Initialise a fresh NumPy board.
      2. Show the empty board.
      3. Alternate Player 1 / Player 2 until win or draw.
      4. Announce result in terminal and on the plot.
      5. Ask both players if they want another round; exit if either says no.
    """
    plt.ion()
    fig = plt.figure(figsize=(5, 5))
    fig.canvas.manager.set_window_title("Tic-Tac-Toe")

    while True:
        board = init_board()
        turn  = PLAYER_1          # Player 1 (X) always goes first
        draw_board(board, title="")

        while True:
            # --- Player move ---
            r, c = get_player_move(turn, board)
            board[r, c] = turn

            # --- Update visualisation ---
            draw_board(board)

            # --- Check result ---
            winner = check_winner(board)
            if winner is not None:
                name, symbol = PLAYER_INFO[winner]
                result_msg = f"🏆  {name} ({symbol}) wins!"
                print(f"\n  {result_msg}\n")
                draw_board(board, title=result_msg)
                break

            if check_draw(board):
                result_msg = "🤝  It's a draw! Well played by both!"
                print(f"\n  {result_msg}\n")
                draw_board(board, title=result_msg)
                break

            # --- Alternate turns ---
            turn = PLAYER_2 if turn == PLAYER_1 else PLAYER_1

        # --- Play-again prompt (both players must agree) ---
        p1_wants = _ask_play_again("Player 1")
        p2_wants = _ask_play_again("Player 2")

        if p1_wants and p2_wants:
            print("\n  Great! Starting a new game…\n")
        else:
            print("\n  Thanks for playing! Goodbye! 👋\n")
            plt.ioff()
            plt.close("all")
            break


def _ask_play_again(player_name: str) -> bool:
    """
    Ask *player_name* whether they want another game.

    Returns:
        True if they agree, False otherwise.
    """
    while True:
        answer = input(
            f"  {player_name}, play again? (yes / no): "
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
    Print the welcome banner explaining the rules, then start the game.
    """
    print()
    print("=" * 52)
    print("    🎮  WELCOME TO TIC-TAC-TOE (Visual Edition)  🎮")
    print("=" * 52)
    print()
    print("  RULES & HOW TO PLAY")
    print("  ────────────────────")
    print("  • A Matplotlib window shows the live 3×3 board.")
    print("  • Rows and columns are numbered 1 to 3.")
    print()
    print("  • When it is your turn, enter a Row number, then")
    print("    a Column number at the terminal prompts.")
    print()
    print("  • Example — to place your mark in the centre cell:")
    print("      Enter Row    (1, 2, or 3):  2")
    print("      Enter Column (1, 2, or 3):  2")
    print()
    print("  • Player 1 plays as  X  (goes first)")
    print("  • Player 2 plays as  O")
    print()
    print("  • Three in a row (row / column / diagonal) wins!")
    print("=" * 52)
    print()

    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\n  Game interrupted. Goodbye! 👋\n")
        plt.close("all")
        sys.exit(0)


if __name__ == "__main__":
    main()
