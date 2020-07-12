#!/usr/bin/env python3

# Solve mini 3x3 version of Sudoku using the backtrack algorithm

import solve_sudoku as ss
from boards import boards_6

# Import puzzles
BOARDS = boards_6[0]
BOARD_SIZE = 6
SUBGRID_HEIGHT = 2
SUBGRID_WIDTH = 3

# All possible numbers that can appear in the puzzle
available_nums = list(range(BOARD_SIZE + 1))


if __name__ == "__main__":
    for BOARD in BOARDS:
        print(ss.main(BOARD, available_nums, SUBGRID_HEIGHT, SUBGRID_WIDTH))