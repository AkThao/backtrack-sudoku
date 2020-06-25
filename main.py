#!/usr/bin/env python3

""" Sudoku Solver """

import sudoku_gui
import solve_sudoku


BOARD = [
    [2, 0, 0],
    [0, 0, 1],
    [0, 0, 0]
]

BOARD_SIZE = 3


available_nums = list(range(BOARD_SIZE + 1))

solve_sudoku.main(BOARD, available_nums)
sudoku_gui.main()
