#!/usr/bin/env python3

# Solve 6x6 version of Sudoku using the backtrack algorithm

import solve_sudoku as ss
import solve_sudoku_recursive as ssr
from boards import boards_6

# Import puzzles
BOARDS = boards_6[0]
BOARD_SIZE = 6
SUBGRID_HEIGHT = boards_6[2]
SUBGRID_WIDTH = boards_6[3]

# All possible numbers that can appear in the puzzle
available_nums = list(range(BOARD_SIZE + 1))


if __name__ == "__main__":
    # Write results to file
    with open("6x6_answers.txt", "w") as results_file:
        results_file.write("# Answers to 6x6 puzzles\n\n")
        # Test for new recursive solver
        for BOARD in BOARDS:
            results_file.write(str(ssr.main(BOARD, BOARD_SIZE, SUBGRID_HEIGHT, SUBGRID_WIDTH)) + "\n")

