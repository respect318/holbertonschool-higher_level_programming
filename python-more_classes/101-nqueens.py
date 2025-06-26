#!/usr/bin/python3
"""Solves the N Queens problem using backtracking"""

import sys

def print_solution(solution):
    """Print a single solution"""
    print(solution)

def is_safe(solution, row, col):
    """Check if a queen can be placed at (row, col)"""
    for r in range(row):
        c = solution[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_nqueens(N, row=0, solution=[], solutions=[]):
    """Backtracking recursive function to solve N Queens"""
    if row == N:
        print_solution([[i, solution[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(solution, row, col):
            solution.append(col)
            solve_nqueens(N, row + 1, solution, solutions)
            solution.pop()  # backtrack

def validate_and_solve():
    """Validate input and solve the problem"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

if __name__ == "__main__":
    validate_and_solve()
