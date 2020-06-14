#!/usr/bin/env python3

# Solve mini 3x3 version of Sudoku using the backtrack algorithm

# NumPy makes it easier to work with 2D array
import numpy as np


# Starting puzzle
BOARD = [
    [0, 0, 3],
    [2, 0, 0],
    [0, 0, 0]
]

# All possible numbers that can appear in the puzzle
available_nums = [0, 1, 2, 3]


def find_empty_cells(board):
    """Traverse the board and return a tuple of positions of empty cells"""
    return [(i, j) for i in range(len(board)) for j in range(len(board[i]))
            if board[i][j] == 0]


def check_cell_value(board, cell, test_value):
    """Return True if the given number is legal
        i.e. does not appear in the current row or column
    Return False if the given number is illegal"""
    # print(board[cell[0],:], board[:,cell[1]]) TESTING
    if test_value not in board[cell[0],:] and test_value not in board[:,cell[1]]:
        # print(f"Value: {test_value} - True") TESTING
        return True
    # print(f"Value: {test_value} - False") TESTING
    return False


def update_cell(board, cell):
    """Try the available numbers from the current cell value + 1
    Return the board if the current cell was successfully updated
    Otherwise, if all available numbers are illegal, return False"""
    # print(f"\nCurrent cell: {cell}") TESTING
    cell_value = board[cell[0],cell[1]]
    cell_value_index = available_nums.index(board[cell[0],cell[1]])
    for num in available_nums[cell_value_index + 1:]:
        # if available_nums.index(num) == len(available_nums) - 1: TESTING
            # print(f"Last value: {board[cell[0],cell[1]]}") TESTING
        if check_cell_value(board, cell, num):
            board[cell[0],cell[1]] = num
            # print(f"Value changed to: {board[cell[0],cell[1]]}") TESTING
            return (True, board)
        elif available_nums.index(num) == len(available_nums) - 1:
            return (False, board)
    # print(board) TESTING


def solve(board, empty_cells):
    count = 0
    while count != len(empty_cells):
        result = update_cell(board, empty_cells[count])
        if result[0] == False:
            count -= 1
        else:
            count += 1


    return result[1]  # change this to board later


def main():
    board = np.array(BOARD)  # make a copy of the original board
    empty_cells = find_empty_cells(board)
    board = solve(board, empty_cells)
    print(board)


if __name__ == "__main__":
    main()


# Notes:
# Write solving algorithm:
    # Fill an empty cell with a number from available_nums
    # Check that the number is legal
    # Otherwise, try next number
    # If all numbers in available_nums have tried and failed, backtrack:
        # Go back to previous cell
        # Try next number in available_nums