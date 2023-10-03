#!/usr/bin/python3
"""
Rectangle Module
"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at position (row, col) on the board.

    Args:
        board (List[int]): The current state of the board.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(n):
    """Solve the N Queens puzzle and print all possible solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        None
    """
    board = [-1] * n  # Initialize an empty board

    def place_queen(row):
        """Recursively place a queen in each row of the board.

        Args:
            row (int): The current row to place the queen.

        Returns:
            None
        """
        if row == n:
            # All queens have been successfully placed
            print([[i, board[i]] for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # Place the queen at (row, col)
                place_queen(row + 1)  # Recur for the next row
                board[row] = -1  # Undo the queen placement

    place_queen(0)  # Start placing queens from the first row


def main():
    """Entry point of the program."""
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line arguments
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check the value of N
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(n)


if __name__ == "__main__":
    main()
