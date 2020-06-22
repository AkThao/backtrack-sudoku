#!/usr/bin/env python3

# Solve mini 3x3 version of Sudoku using the backtrack algorithm

import solve_sudoku as ss

# Starting puzzles
BOARD_1 = [
    [0, 5, 0, 0, 0, 1],
    [0, 0, 4, 6, 0, 0],
    [4, 0, 0, 0, 5, 0],
    [1, 0, 0, 0, 0, 4],
    [0, 4, 3, 0, 0, 0],
    [0, 6, 0, 2, 4, 0]
]


EASY_BOARDS = [BOARD_1]
BOARD_SIZE = 6
SUBGRID_HEIGHT = 2
SUBGRID_WIDTH = 3


# All possible numbers that can appear in the puzzle
available_nums = list(range(BOARD_SIZE + 1))


if __name__ == "__main__":
    ss.main(EASY_BOARDS, available_nums, SUBGRID_HEIGHT, SUBGRID_WIDTH)
