# Functions for solving Sudoku puzzles of any size

# NumPy makes it easier to work with 2D arrays
import numpy as np


def find_empty_cells(board):
    """Traverse the board and return a tuple of positions of empty cells"""
    return [(i, j) for i in range(len(board)) for j in range(len(board[i]))
            if board[i][j] == 0]


def check_rows_cols(board, cell, test_value):
    """Return True if the given number is legal
        i.e. does not appear in the current row or column
    Return False if the given number is illegal
    """
    if test_value not in board[cell[0], :] and test_value not in board[:, cell[1]]:
        return True
    return False


def check_subgrid(board, cell, test_value, subgrid_size):
    """Return True if the given number is legal
        i.e. does not appear in the current subgrid
    Return False if the given number is illegal
    """
    # Find subgrid coordinates
    subgrid_coords = ((cell[0] // subgrid_size) * subgrid_size,
                      (cell[1] // subgrid_size) * subgrid_size)

    # Define subgrid
    subgrid = board[subgrid_coords[0]:subgrid_coords[0]+subgrid_size,
                    subgrid_coords[1]:subgrid_coords[1]+subgrid_size]

    if test_value not in subgrid:
        return True
    return False


def update_cell(board, cell, available_nums, subgrid_size):
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

    if subgrid_size == 0:  # Don't call check_subgrid if there aren't subgrids (e.g. 3x3 board)
        # Check all numbers from the value of the current cell (the earlier numbers have already been checked)
        for num in available_nums[cell_value_index + 1:]:
            # If the number is legal, update the cell and move on
            if check_rows_cols(board, cell, num):
                board[cell[0], cell[1]] = num
                return (True, board)
            # Otherwise, none of the numbers worked and we need to backtrack
            elif available_nums.index(num) == len(available_nums) - 1:
                board[cell[0], cell[1]] = 0
                return (False, board)
    else:  # Call check_subgrid otherwise
        for num in available_nums[cell_value_index + 1:]:
            if check_rows_cols(board, cell, num) and check_subgrid(board, cell, num, subgrid_size):
                board[cell[0], cell[1]] = num
                return (True, board)
            elif available_nums.index(num) == len(available_nums) - 1:
                board[cell[0], cell[1]] = 0
                return (False, board)


def solve(board, empty_cells, available_nums, subgrid_size):
    """Perform the backtrack algorithm"""
    count = 0
    while count != len(empty_cells):
        result = update_cell(board, empty_cells[count], available_nums, subgrid_size)
        if result[0] is False:  # Cell was not updated, so backtrack
            count -= 1
        else:  # Cell was updated, so carry on to the next cell
            count += 1

    return result[1]


def main(BOARDS, available_nums, subgrid_size=0):
    for b in BOARDS:
        board = np.array(b)  # Make a copy of the original board
        empty_cells = find_empty_cells(board)
        board = solve(board, empty_cells, available_nums, subgrid_size)
        print(f"Solution:\n{board}\n")  # Solved puzzle
