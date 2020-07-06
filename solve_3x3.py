#!/usr/bin/env python3

# Solve mini 3x3 version of Sudoku using the backtrack algorithm

import solve_sudoku as ss
from boards import boards_3

# Import puzzles
BOARDS = boards_3
BOARD_SIZE = 3

# All possible numbers that can appear in the puzzle
available_nums = list(range(BOARD_SIZE + 1))


if __name__ == "__main__":
    for BOARD in BOARDS:
        ss.main(BOARD, available_nums)
