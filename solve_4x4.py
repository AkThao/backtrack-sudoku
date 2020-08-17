#!/usr/bin/env python3

# Solve 4x4 version of Sudoku using the backtrack algorithm

import solve_sudoku as ss
import solve_sudoku_recursive as ssr
from boards import boards_4

# Import puzzles
BOARDS = boards_4[0]
BOARD_SIZE = 4
SUBGRID_HEIGHT = boards_4[2]
SUBGRID_WIDTH = boards_4[3]

# All possible numbers that can appear in the puzzle
available_nums = list(range(BOARD_SIZE + 1))


if __name__ == "__main__":
    # Write results to file
    with open("4x4_answers.txt", "w") as results_file:
        results_file.write("# Answers to 4x4 puzzles\n\n")
        # Test for new recursive solver
        for BOARD in BOARDS:
            results_file.write(str(ssr.main(BOARD, BOARD_SIZE, SUBGRID_HEIGHT, SUBGRID_WIDTH)) + "\n")





