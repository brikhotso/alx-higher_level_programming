#!/usr/bin/python3
""" Solve N-queens puzzel """
import sys


def is_safe(board, row, col):
    """
    Assess queens placement at specified row and column.

    Parameters:
    - board: Current placement of queens on the board.
    - row: The current row to check for queen placement.
    - col: The column to check for queen placement.

    Returns:
    - True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    """
    Print the chessboard representation of the queen placements.

    Parameters:
    - board: List representing the column position of queens in each row.
    """
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)


def solve_nqueens(n):
    """
    Solve the N-Queens problem for a given board size.

    Parameters:
    - n: The size of the chessboard.

    Raises:
    - ValueError: If N is not a valid integer.
    - SystemExit: If N is less than 4.

    Prints:
    - The solutions to the N-Queens problem.
    """
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve(board, 0)


def solve(board, row):
    """
    Recursively solve the N-Queens problem using backtracking.

    Parameters:
    - board: Current placement of queens on the board.
    - row: The current row being considered.

    Prints:
    - The solutions to the N-Queens problem.
    """
    n = len(board)

    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1)
            board[row] = -1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
