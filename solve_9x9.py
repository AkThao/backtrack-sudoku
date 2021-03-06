#!/usr/bin/env python3

# Solve 9x9 version of Sudoku using the backtrack algorithm

import solve_sudoku as ss
import solve_sudoku_recursive as ssr
from boards import boards_9

# Import puzzles
BOARDS = boards_9[0]
BOARD_SIZE = 9
SUBGRID_HEIGHT = boards_9[2]
SUBGRID_WIDTH = boards_9[3]

# All possible numbers that can appear in the puzzle
available_nums = list(range(BOARD_SIZE + 1))


if __name__ == "__main__":
    # Write results to file
    with open("9x9_answers.txt", "w") as results_file:
        results_file.write("# Answers to 9x9 puzzles\n\n")
        # Test for new recursive solver
        for BOARD in BOARDS:
            results_file.write(str(ssr.main(BOARD, BOARD_SIZE, SUBGRID_HEIGHT, SUBGRID_WIDTH)) + "\n")

