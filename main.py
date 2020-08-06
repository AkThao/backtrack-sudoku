#!/usr/bin/env python3

""" Sudoku Solver """

import sudoku_gui
import solve_sudoku_recursive
import boards
from sys import exit as sysExit
import random
import pickle
import time

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread

__version__ = "0.2"
__author__ = "Akaash Thao"


class SudokuCtrl:
    def __init__(self, view, model):
        self._view = view
        self._solver = model

        self.animation_speed = 1
        self.temp_board_states = []
        self.is_animating = False

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
        self.board = random.choice(self.board_list[0])
        self.board_size = len(self.board)
        self._view.create_grid(board_size, self.board)
        self._view.solve_button.setDisabled(False)
        self._view.check_button.setDisabled(False)
        self._view.playthrough_button.setDisabled(False)
        self._view.pause_button.setText("PAUSE")
        self._view.pause_button.repaint()
        self._view.pause_button.clicked.disconnect()
        self._view.pause_button.clicked.connect(self.pause_animation)
        self.temp_board_states = []

    def solve_puzzle(self):
        self.get_empty_cells()
        self.result = self._solver.main(BOARD=self.board,
                                        board_size=self.board_size,
                                        subgrid_height=self.board_list[2],
                                        subgrid_width=self.board_list[3])

    def show_answer(self):
        self.solve_puzzle()
        QApplication.processEvents()
        for cell in self.empty_cells:
            self.update_cell(cell[0], cell[1], str(
                self.result[cell[0]][cell[1]]))
            self.change_cell_style(cell[0], cell[1], "solved_cell")
            QApplication.processEvents()
            QThread.msleep(self.animation_speed)

        self._view.solve_button.setDisabled(True)
        self._view.check_button.setDisabled(True)

    def update_cell(self, row, col, value):
        self._view.grid_layout.itemAtPosition(row, col).widget().setText(value)
        self._view.grid_layout.itemAtPosition(
            row, col).widget().setEnabled(False)

    def change_cell_style(self, row, col, cell_style):
        self._view.grid_layout.itemAtPosition(
            row, col).widget().setObjectName(cell_style)
        self._view.grid_layout.itemAtPosition(
            row, col).widget().setStyleSheet(self._view.styles)
        self._view.grid_layout.itemAtPosition(row, col).widget().repaint()

    def get_user_input(self):
        self.user_solution = []

        for i in range(self.board_size):
            self.user_solution.append([])
            for j in range(self.board_size):
                self.user_solution[i].append(
                    int(self._view.grid_layout.itemAtPosition(i, j).widget().text()))

    def check_answer(self):
        self.get_user_input()
        self.solve_puzzle()

        for cell in self.empty_cells:
            self._view.grid_layout.itemAtPosition(
                cell[0], cell[1]).widget().setEnabled(False)
            if (self.result[cell[0]][cell[1]] == self.user_solution[cell[0]][cell[1]]):
                self.change_cell_style(cell[0], cell[1], "correct_cell")
            else:
                self.change_cell_style(cell[0], cell[1], "incorrect_cell")

        self._view.solve_button.setDisabled(True)
        self._view.check_button.setDisabled(True)

    def get_board_states(self):
        self.solve_puzzle()
        self.board_states = []
        with open("board_states.txt", "rb") as fp:
            while True:
                try:
                    self.board_states.append(pickle.load(fp))
                except EOFError:
                    break

    def display_animation(self):
        self._view.solve_button.setDisabled(True)
        self._view.check_button.setDisabled(True)
        self._view.button3.setDisabled(True)
        self._view.button4.setDisabled(True)
        self._view.button6.setDisabled(True)
        self._view.button9.setDisabled(True)
        self.is_animating = True

        QApplication.processEvents()
        while len(self.board_states) > 0:
            state = self.board_states[0]
            del self.board_states[0]
            for cell in self.empty_cells:
                self.update_cell(cell[0], cell[1], str(
                    state[cell[0]][cell[1]]))
                self.change_cell_style(cell[0], cell[1], "solved_cell")
            QApplication.processEvents()
            QThread.msleep(self.animation_speed)

        self._view.button3.setDisabled(False)
        self._view.button4.setDisabled(False)
        self._view.button6.setDisabled(False)
        self._view.button9.setDisabled(False)
        self.is_animating = False

    def pause_animation(self):
        if self.is_animating:
            self.temp_board_states, self.board_states = self.board_states, []
            self._view.playthrough_button.setDisabled(True)
            self._view.pause_button.setText("CONTINUE")
            self._view.pause_button.repaint()
            self._view.pause_button.clicked.disconnect()
            self._view.pause_button.clicked.connect(self.continue_animation)
            QApplication.processEvents()
        else:
            self._view.error_dialog.exec_()

    def continue_animation(self):
        self.board_states = self.temp_board_states
        self._view.pause_button.setText("PAUSE")
        self._view.pause_button.repaint()
        self._view.pause_button.clicked.disconnect()
        self._view.pause_button.clicked.connect(self.pause_animation)
        QApplication.processEvents()
        self.display_animation()

    def change_speed(self):
        self.animation_speed = self._view.change_speed_slider.value()

    def get_empty_cells(self):
        self.empty_cells = self._solver.return_list_of_empty_cells(self.board)

    def quit(self):
        sysExit()

    def _connect_signals(self):
        self._view.button3.clicked.connect(lambda: self.pick_random_board(3))
        self._view.button4.clicked.connect(lambda: self.pick_random_board(4))
        self._view.button6.clicked.connect(lambda: self.pick_random_board(6))
        self._view.button9.clicked.connect(lambda: self.pick_random_board(9))

        self._view.solve_button.clicked.connect(self.show_answer)
        self._view.check_button.clicked.connect(self.check_answer)
        self._view.playthrough_button.clicked.connect(self.get_board_states)
        self._view.playthrough_button.clicked.connect(self.display_animation)
        self._view.pause_button.clicked.connect(self.pause_animation)
        self._view.quit_button.clicked.connect(self.quit)
        self._view.change_speed_slider.valueChanged.connect(self.change_speed)
        # self._view.error_dialog_button_box.accepted.connect(self.quit)


def main():
    backtrack_sudoku = QApplication([])

    view = sudoku_gui.SudokuUI()
    view.show()

    model = solve_sudoku_recursive

    SudokuCtrl(view=view, model=model)

    sysExit(backtrack_sudoku.exec_())


if __name__ == "__main__":
    main()


# TODO:
