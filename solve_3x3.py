#!/usr/bin/env python3

# Solve mini 3x3 version of Sudoku using the backtrack algorithm

import solve_sudoku as ss
import solve_sudoku_recursive as ssr
from boards import boards_3

# Import puzzles
BOARDS = boards_3[0]
BOARD_SIZE = 3

# All possible numbers that can appear in the puzzle
available_nums = list(range(BOARD_SIZE + 1))


if __name__ == "__main__":
    #for BOARD in BOARDS:
    #    print(ss.main(BOARD, available_nums))

    # Write results to file
    with open("3x3_answers.txt", "w") as results_file:
        results_file.write("# Answers to 3x3 puzzles\n\n")
        # Test for new recursive solver
        for BOARD in BOARDS:
            results_file.write(str(ssr.main(BOARD, BOARD_SIZE)) + "\n")

