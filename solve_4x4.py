#!/usr/bin/env python3

# Solve mini 4x4 version of Sudoku using the backtrack algorithm

import solve_sudoku as ss
from boards import boards_4

# Import puzzles
BOARDS = boards_4
BOARD_SIZE = 4
SUBGRID_HEIGHT = 2
SUBGRID_WIDTH = 2

# All possible numbers that can appear in the puzzle
available_nums = list(range(BOARD_SIZE + 1))


if __name__ == "__main__":
    for BOARD in BOARDS:
        ss.main(BOARD, available_nums, SUBGRID_HEIGHT, SUBGRID_WIDTH)
