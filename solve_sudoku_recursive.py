import numpy as np


def solve(board, board_size, subgrid_height, subgrid_width):
    empty_cell_found = find_empty_cell(board)
    # If algorithm has reached the end and the board is full, it must be solved
    if not empty_cell_found:
        return True
    else:
        row, col = empty_cell_found

    for i in range(1, board_size + 1):  # Available nums (1-9)
        if is_valid(board, i, row, col, subgrid_height, subgrid_width):
            board[row][col] = i  # If a number works, put it in the board

            if solve(board, board_size, subgrid_height, subgrid_width):  # Try to solve with the new board
                return True

            board[row][col] = 0

    return False



def return_list_of_empty_cells(board):
    """Traverse the board and return a tuple of positions of empty cells
        Not used in the solving algorithm, but useful for the GUI
    """
    return [(i, j) for i in range(len(board)) for j in range(len(board[i]))
            if board[i][j] == 0]


def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)

    return False


def is_valid(board, test_value, row, col, subgrid_height, subgrid_width):
    # Check row
    for i in range(len(board)):
        if board[row][i] == test_value and i != col:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][col] == test_value and i != row:
            return False

    # Check subgrid
    if subgrid_height != 0:
        subgrid_x = (row // subgrid_height) * subgrid_height
        subgrid_y = (col // subgrid_width) * subgrid_width
        for i in range(subgrid_x, subgrid_x + subgrid_height):
            for j in range(subgrid_y, subgrid_y + subgrid_width):
                if board[i][j] == test_value and (i, j) != (row, col):
                    return False

    # All checks passed
    return True


def main(BOARD, board_size, subgrid_height=0, subgrid_width=0):
    board = BOARD
    solve(board, board_size, subgrid_height, subgrid_width)
    return board

if __name__ == "__main__":
    main()
