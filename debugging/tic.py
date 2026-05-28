#!/usr/bin/python3

def print_board(board):
    """
    Function Description:
        Displays the Tic-Tac-Toe board.

    Parameters:
        board (list): 2D list representing the game board.

    Returns:
        None
    """

    for i, row in enumerate(board):
        print(" | ".join(row))

        if i < 2:
            print("-" * 9)


def check_winner(board):
    """
    Function Description:
        Checks whether a player has won the game.

    Parameters:
        board (list): 2D list representing the game board.

    Returns:
        bool: True if a player has won, otherwise False.
    """

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if (
            board[0][col] ==
            board[1][col] ==
            board[2][col] != " "
        ):
            return True

    # Check diagonals
    if (
        board[0][0] ==
        board[1][1] ==
        board[2][2] != " "
    ):
        return True

    if (
        board[0][2] ==
        board[1][1] ==
        board[2][0] != " "
    ):
        return True

    return False


def is_draw(board):
    """
    Function Description:
        Checks whether the game ended in a draw.

    Parameters:
        board (list): 2D list representing the game board.

    Returns:
        bool: True if the board is full and no winner exists.
    """

    for row in board:
        if " " in row:
            return False

    return True


def get_valid_input(player):
    """
    Function Description:
        Safely gets valid row and column input from the user.

    Parameters:
        player (str): Current player symbol.

    Returns:
        tuple: Valid row and column integers.
    """

    while True:
        try:
            row = int(
                input(
                    f"Enter row (0, 1, or 2) for player {player}: "
                )
            )

            col = int(
                input(
                    f"Enter column (0, 1, or 2) for player {player}: "
                )
            )

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Row and column must be 0, 1, or 2.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter numbers only.")


def tic_tac_toe():
    """
    Function Description:
        Runs the Tic-Tac-Toe game loop.

    Parameters:
        None

    Returns:
        None
    """

    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row, col = get_valid_input(player)

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for draw
        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


tic_tac_toe()