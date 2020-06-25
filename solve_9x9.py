#!/usr/bin/env python3

# Solve mini 3x3 version of Sudoku using the backtrack algorithm

import solve_sudoku as ss

# Starting puzzles
BOARD_1 = [
    [0, 3, 0, 0, 0, 1, 0, 8, 9],
    [4, 8, 0, 0, 0, 3, 0, 5, 0],
    [6, 0, 0, 5, 9, 8, 2, 0, 4],
    [8, 0, 0, 6, 0, 0, 0, 2, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 7],
    [2, 7, 0, 0, 0, 9, 0, 0, 8],
    [7, 0, 3, 9, 5, 4, 0, 0, 2],
    [0, 4, 0, 1, 0, 0, 0, 7, 5],
    [1, 2, 0, 8, 0, 0, 0, 4, 0]
]


EASY_BOARDS = [BOARD_1]
BOARD_SIZE = 9
SUBGRID_HEIGHT = 3
SUBGRID_WIDTH = 3


# All possible numbers that can appear in the puzzle
available_nums = list(range(BOARD_SIZE + 1))


if __name__ == "__main__":
    for BOARD in EASY_BOARDS:
        ss.main(BOARD, available_nums, SUBGRID_HEIGHT, SUBGRID_WIDTH)
