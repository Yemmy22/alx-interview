#!/usr/bin/python3
import sys
"""
A Nqueens program module
"""


def print_solution(board):
    """
    Prints the board configuration in the required format
    """
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at board[row][col]
    """
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens_util(board, row):
    """
    Uses backtracking to find all solutions
    """
    if row == len(board):
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            solve_nqueens_util(board, row + 1)  # Recurse
            board[row][col] = 0  # Backtrack


def solve_nqueens(n):
    """
    Initializes the board and starts the solving process
    """
    board = [[0] * n for _ in range(n)]
    solve_nqueens_util(board, 0)


def main():
    """
    The entry point for other options
    """
    # Check for correct usage
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
