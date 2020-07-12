#!/usr/bin/env python3

""" Sudoku Solver """

import sudoku_gui
import solve_sudoku
import boards
import sys
import random

from PyQt5.QtWidgets import QApplication


class SudokuCtrl:
    def __init__(self, view, model):
        self._view = view
        self._solver = model

        self._create_boards_lists()
        self._connect_signals()

    def _create_boards_lists(self):
        self.boards_lists = {
            3: boards.boards_3,
            4: boards.boards_4,
            6: boards.boards_6,
            9: boards.boards_9
        }

    def pick_random_board(self, board_size):
        self.board_list = self.boards_lists[board_size]
        self.random_board = random.choice(self.board_list[0])
        self._view.create_grid(board_size, self.random_board)
        self._view.solve_button.setDisabled(False)

    def solve_puzzle(self):
        self.result = self._solver.main(BOARD=self.random_board,
            available_nums=self.board_list[1],
            subgrid_height=self.board_list[2],
            subgrid_width=self.board_list[3])

    def update_grid(self):
        pass

    def _connect_signals(self):
        self._view.button3.clicked.connect(lambda: self.pick_random_board(3))
        self._view.button4.clicked.connect(lambda: self.pick_random_board(4))
        self._view.button6.clicked.connect(lambda: self.pick_random_board(6))
        self._view.button9.clicked.connect(lambda: self.pick_random_board(9))

        self._view.solve_button.clicked.connect(self.solve_puzzle)



def main():
    backtrack_sudoku = QApplication(sys.argv)

    view = sudoku_gui.SudokuUI()
    view.show()

    model = solve_sudoku

    SudokuCtrl(view=view, model=model)

    sys.exit(backtrack_sudoku.exec_())


if __name__ == "__main__":
    main()


# TODO:
# Update grid with solved puzzle