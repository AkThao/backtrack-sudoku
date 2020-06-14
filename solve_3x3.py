#!/usr/bin/env python3

# Solve mini 3x3 version of Sudoku using the backtrack algorithm

# NumPy makes it easier to work with 2D arrays
import numpy as np

# Starting puzzles
BOARD_1 = [
    [0, 0, 3],
    [2, 0, 0],
    [0, 0, 0]
]

BOARD_2 = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 3]
]

BOARD_3 = [
    [0, 2, 0],
    [0, 0, 0],
    [1, 0, 0]
]

BOARD_4 = [
    [0, 0, 0],
    [0, 0, 2],
    [1, 0, 0]
]

BOARD_5 = [
    [3, 0, 0],
    [0, 0, 0],
    [0, 2, 0]
]

BOARD_6 = [
    [2, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]

BOARD_7 = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 3, 0]
]

BOARD_8 = [
    [0, 0, 1],
    [0, 2, 0],
    [0, 0, 0]
]

BOARD_9 = [
    [0, 0, 1],
    [0, 0, 0],
    [2, 0, 0]
]

BOARD_10 = [
    [2, 0, 0],
    [0, 0, 1],
    [0, 0, 0]
]

BOARDS = [BOARD_1, BOARD_2, BOARD_3, BOARD_4, BOARD_5, BOARD_6, BOARD_7, BOARD_8, BOARD_9, BOARD_10]
BOARD_SIZE = 3

# All possible numbers that can appear in the puzzle
available_nums = list(range(BOARD_SIZE + 1))


def find_empty_cells(board):
    """Traverse the board and return a tuple of positions of empty cells"""
    return [(i, j) for i in range(len(board)) for j in range(len(board[i]))
            if board[i][j] == 0]


def check_cell_value(board, cell, test_value):
    """Return True if the given number is legal
        i.e. does not appear in the current row or column
    Return False if the given number is illegal
    """
    if test_value not in board[cell[0], :] and test_value not in board[:, cell[1]]:
        return True
    return False


def update_cell(board, cell):
    """Try to update the current cell
    Return a two-tuple, with second element as the board
    First element is True if the cell was successfully updated
    First element is False otherwise
    """
    # Get current cell value and index
    cell_value = board[cell[0], cell[1]]
    cell_value_index = available_nums.index(cell_value)

    # If we backtracked and the current cell has no more options, reset it and go to the previous cell
    if cell_value_index == len(available_nums) - 1:
        board[cell[0], cell[1]] = 0
        return (False, board)

    # Check all numbers from the value of the current cell (the earlier numbers have already been checked)
    for num in available_nums[cell_value_index + 1:]:
        # If the number is legal, update the cell and move on
        if check_cell_value(board, cell, num):
            board[cell[0], cell[1]] = num
            return (True, board)
        # Otherwise, none of the numbers worked and we need to backtrack
        elif available_nums.index(num) == len(available_nums) - 1:
            board[cell[0], cell[1]] = 0
            return (False, board)


def solve(board, empty_cells):
    """Perform the backtrack algorithm"""
    count = 0
    while count != len(empty_cells):
        result = update_cell(board, empty_cells[count])
        if result[0] is False:  # Cell was not updated, so backtrack
            count -= 1
        else:  # Cell was updated, so carry on to the next cell
            count += 1

    return result[1]


def main():
    for b in BOARDS:
        board = np.array(b)  # Make a copy of the original board
        empty_cells = find_empty_cells(board)
        board = solve(board, empty_cells)
        print(f"Solution:\n{board}\n")  # Solved puzzle


if __name__ == "__main__":
    main()
