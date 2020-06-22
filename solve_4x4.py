#!/usr/bin/env python3

# Solve mini 4x4 version of Sudoku using the backtrack algorithm

import solve_sudoku as ss

# Starting puzzles
BOARD_1 = [
    [2, 1, 0, 0],
    [0, 3, 2, 0],
    [0, 0, 0, 4],
    [1, 0, 0, 0]
]

BOARD_2 = [
    [1, 0, 3, 4],
    [0, 3, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 1]
]

BOARD_3 = [
    [0, 0, 1, 2],
    [0, 1, 0, 3],
    [0, 0, 0, 0],
    [4, 0, 2, 0]
]

BOARD_4 = [
    [0, 2, 3, 0],
    [0, 3, 0, 0],
    [0, 0, 0, 1],
    [2, 0, 4, 0]
]

BOARD_5 = [
    [4, 2, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 2, 0],
    [0, 0, 0, 3]
]

BOARD_6 = [
    [0, 0, 0, 3],
    [4, 0, 0, 0],
    [0, 1, 3, 0],
    [3, 0, 2, 0]
]

BOARD_7 = [
    [4, 0, 0, 0],
    [0, 0, 4, 0],
    [0, 1, 2, 0],
    [2, 0, 0, 3]
]

BOARD_8 = [
    [3, 0, 0, 0],
    [0, 0, 0, 2],
    [0, 1, 0, 3],
    [0, 0, 2, 1]
]

BOARD_9 = [
    [0, 0, 1, 0],
    [0, 2, 0, 0],
    [4, 0, 2, 0],
    [2, 0, 0, 4]
]

BOARD_10 = [
    [0, 3, 0, 0],
    [4, 1, 0, 0],
    [1, 2, 3, 0],
    [3, 0, 0, 0]
]

BOARD_11 = [
    [0, 0, 4, 0],
    [1, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 0, 3]
]

BOARD_12 = [
    [2, 0, 0, 0],
    [0, 0, 0, 3],
    [0, 0, 0, 0],
    [0, 4, 1, 0]
]

BOARD_13 = [
    [0, 4, 0, 0],
    [0, 0, 0, 2],
    [0, 0, 0, 0],
    [0, 0, 2, 3]
]

BOARD_14 = [
    [0, 4, 0, 0],
    [3, 0, 0, 0],
    [0, 0, 1, 4],
    [0, 0, 2, 0]
]

BOARD_15 = [
    [0, 0, 0, 3],
    [0, 0, 0, 4],
    [3, 0, 0, 0],
    [2, 0, 0, 0]
]

BOARD_16 = [
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 4, 0, 0],
    [0, 0, 2, 0]
]

BOARD_17 = [
    [0, 0, 0, 0],
    [4, 3, 0, 2],
    [2, 0, 0, 4],
    [0, 0, 0, 0]
]

BOARD_18 = [
    [0, 1, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 3],
    [4, 0, 0, 0]
]

BOARD_19 = [
    [0, 0, 0, 4],
    [4, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 2, 0, 0]
]

BOARD_20 = [
    [0, 0, 1, 0],
    [3, 0, 0, 0],
    [0, 3, 0, 0],
    [0, 0, 0, 2]
]

EASY_BOARDS = [BOARD_1, BOARD_2, BOARD_3, BOARD_4, BOARD_5, BOARD_6, BOARD_7, BOARD_8, BOARD_9, BOARD_10]
HARD_BOARDS = [BOARD_11, BOARD_12, BOARD_13, BOARD_14, BOARD_15, BOARD_16, BOARD_17, BOARD_18, BOARD_19, BOARD_20]
BOARD_SIZE = 4
SUBGRID_HEIGHT = 2
SUBGRID_WIDTH = 2


# All possible numbers that can appear in the puzzle
available_nums = list(range(BOARD_SIZE + 1))


if __name__ == "__main__":
    ss.main(EASY_BOARDS, available_nums, SUBGRID_HEIGHT, SUBGRID_WIDTH)
    ss.main(HARD_BOARDS, available_nums, SUBGRID_HEIGHT, SUBGRID_WIDTH)
