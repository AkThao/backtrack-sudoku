#!/usr/bin/env python3

# Solve mini 3x3 version of Sudoku using the backtrack algorithm

import solve_sudoku as ss

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


if __name__ == "__main__":
    ss.main(BOARDS, available_nums)
