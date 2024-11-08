#!/usr/bin/python3
""" Solves the N queens problem. """

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board cell

    Args:
        board (List[List[int]]): The current state of the chessboard
        row (int): The row to check
        col (int): The column to check
        n (int): The size of the board

    Returns:
        bool: True if it's safe to place a queen, False otherwise
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem

    Args:
        n (int): The size of the chessboard and the number of queens

    Returns:
        List[List[List[int]]]: A list of all possible solutions
    """

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(col):
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return True

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

    solve(0)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
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

    solutions = solve_nqueens(n)
    print_solutions(solutions)
