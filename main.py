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
from PyQt5.QtCore import QThread, QObject

__version__ = "0.3"
__author__ = "Akaash Thao"


class Worker(QObject):
    pass


class SudokuCtrl:
    def __init__(self, view, model):
        # Set up the app by adding the view and model to the GUI
        self._view = view
        self._solver = model

        # Animation variables
        self.animation_speed = 1
        self.temp_board_states = []
        self.is_animating = False

        # Import all boards and set up all controls
        self._create_boards_lists()
        self._connect_signals()

    def _create_boards_lists(self):
        """Copy the file containing all the boards into a dictionary, where key = board_size"""
        self.boards_lists = {
            3: boards.boards_3,
            4: boards.boards_4,
            6: boards.boards_6,
            9: boards.boards_9
        }

    def pick_random_board(self, board_size):
        """Choose a random board of a specified size and set the controls appropriately"""
        self.board_list = self.boards_lists[board_size]
        self.board = random.choice(self.board_list[0])
        self.board_size = len(self.board)
        self._view.create_grid(board_size, self.board)
        self._view.solve_button.setDisabled(False)
        self._view.check_button.setDisabled(False)
        self._view.playthrough_button.setDisabled(False)
        self._view.change_speed_slider.setDisabled(False)
        self._view.pause_button.setText("Pause (spacebar)")
        self._view.pause_button.repaint()
        self._view.pause_button.clicked.disconnect()
        self._view.pause_button.clicked.connect(self.pause_animation)
        self.temp_board_states = []

    def solve_puzzle(self):
        """Call the backtrack algorithm and store the result as a member variable"""
        self.get_empty_cells()
        self.result = self._solver.main(BOARD=self.board,
                                        board_size=self.board_size,
                                        subgrid_height=self.board_list[2],
                                        subgrid_width=self.board_list[3])

    def show_answer(self):
        """Solve the current puzzle and display the solution with animation"""
        self.solve_puzzle()
        self._view.solve_button.setDisabled(True)
        self._view.check_button.setDisabled(True)
        QApplication.processEvents()
        for cell in self.empty_cells:
            self.update_cell(cell[0], cell[1], str(
                self.result[cell[0]][cell[1]]))
            self.change_cell_style(cell[0], cell[1], "solved_cell")
            QApplication.processEvents()
            QThread.msleep(self.animation_speed)

    def update_cell(self, row, col, value):
        """Update cell at [row, col] to show 'value'"""
        self._view.grid_layout.itemAtPosition(row, col).widget().setText(value)
        self._view.grid_layout.itemAtPosition(
            row, col).widget().setEnabled(False)

    def change_cell_style(self, row, col, cell_style):
        """Change a cell's CSS based on its state (solved, correct, incorrect, empty....)"""
        # Setting object name allows style to be applied
        self._view.grid_layout.itemAtPosition(
            row, col).widget().setObjectName(cell_style)
        self._view.grid_layout.itemAtPosition(
            row, col).widget().setStyleSheet(self._view.styles)
        # Repaint is necessary as board won't show the new style otherwise
        self._view.grid_layout.itemAtPosition(row, col).widget().repaint()

    def get_cell(self, row, col):
        """Return the value of cell at [row, col]"""
        return int(self._view.grid_layout.itemAtPosition(row, col).widget().text())

    def get_user_input(self):
        """Store a 2D array of the current board state"""
        self.user_solution = []

        for i in range(self.board_size):
            self.user_solution.append([])
            for j in range(self.board_size):
                self.user_solution[i].append(self.get_cell(i, j))

    def check_answer(self):
        """Compare user's input to solution and colour-code cells to show correct/incorrect values"""
        self.get_user_input()
        self.solve_puzzle()

        # No need to solve/check twice
        self._view.solve_button.setDisabled(True)
        self._view.check_button.setDisabled(True)

        for cell in self.empty_cells:
            self._view.grid_layout.itemAtPosition(
                cell[0], cell[1]).widget().setEnabled(False)
            if (self.result[cell[0]][cell[1]] == self.user_solution[cell[0]][cell[1]]):
                self.change_cell_style(cell[0], cell[1], "correct_cell")
            else:
                self.change_cell_style(cell[0], cell[1], "incorrect_cell")

    def get_board_states(self):
        """Retrieve current puzzle's solution, saved to file by solver"""
        self.solve_puzzle()
        self.board_states = []
        with open("board_states.txt", "rb") as fp:
            while True:
                try:
                    self.board_states.append(pickle.load(fp))
                except EOFError:
                    break

    def run_animation(self):
        """Display animation of solving algorithm on board"""
        # Pressing these buttons during the animation can crash the app, so just disable them
        self._view.solve_button.setDisabled(True)
        self._view.check_button.setDisabled(True)
        self._view.button3.setDisabled(True)
        self._view.button4.setDisabled(True)
        self._view.button5.setDisabled(True)
        self._view.button6.setDisabled(True)
        self._view.button7.setDisabled(True)
        self._view.button8.setDisabled(True)
        self._view.button9.setDisabled(True)

        # Chosen to disable the slider during animation for now
        # Because animation and slider both run on main thread
        # So slider cannot update until main event loop progresses
        # Not an issue for fast animation, but on slow animation (e.g. 1s sleep), this wait time becomes obvious
        self._view.change_speed_slider.setDisabled(
            True)  # TEMPORARY, FIX IN FUTURE
        # Used to control pausing/resuming of the animation
        self.is_animating = True

        self._view.pause_button.setText("Pause (spacebar)")
        self._view.pause_button.repaint()
        self._view.pause_button.clicked.disconnect()
        self._view.pause_button.clicked.connect(self.pause_animation)
        QApplication.processEvents()
        while len(self.board_states) > 0:
            state = self.board_states[0]
            del self.board_states[0]
            for cell in self.empty_cells:
                previous_cell_value = self.get_cell(cell[0], cell[1])
                new_cell_value = state[cell[0]][cell[1]]
                self.update_cell(cell[0], cell[1], str(
                    state[cell[0]][cell[1]]))
                if new_cell_value == 0:
                    self.change_cell_style(cell[0], cell[1], "incorrect_cell")
                elif new_cell_value == previous_cell_value:
                    self.change_cell_style(cell[0], cell[1], "solved_cell")
                else:
                    self.change_cell_style(cell[0], cell[1], "correct_cell")
            # Return control to main event loop to display updated board
            QApplication.processEvents()
            # self.animation_speed is a delay between "frames"
            QThread.msleep(self.animation_speed)

            # Show that every cell is correct when animation has completed but not when paused
            if self.is_animating:
                for cell in self.empty_cells:
                    self.change_cell_style(cell[0], cell[1], "correct_cell")

        # Re-enable buttons now that animation has finished
        self._view.button3.setDisabled(False)
        self._view.button4.setDisabled(False)
        self._view.button5.setDisabled(False)
        self._view.button6.setDisabled(False)
        self._view.button7.setDisabled(False)
        self._view.button8.setDisabled(False)
        self._view.button9.setDisabled(False)
        self._view.change_speed_slider.setDisabled(False)
        self.is_animating = False

    def pause_animation(self):
        """Pause the backtrack algorithm solving animation"""
        if self.is_animating:
            self.is_animating = False
            self._view.change_speed_slider.setDisabled(False)
            self._view.solve_button.setDisabled(False)
            # The animation is "paused" by emptying the board_states list so the while loop in self.run_animation stops
            self.temp_board_states, self.board_states = self.board_states, []
            # Change the pause button to a continue button
            self._view.pause_button.setText("Continue (spacebar)")
            self._view.pause_button.repaint()
            self._view.pause_button.clicked.disconnect()
            self._view.pause_button.clicked.connect(self.continue_animation)
            QApplication.processEvents()
        else:
            # Can't pause something that isn't running
            self._view.error_dialog.exec_()

    def continue_animation(self):
        """Resume the backtrack algorithm solving animation"""
        # Don't need to set self.is_animating = True, as this is done in self.run_animation
        self._view.change_speed_slider.setDisabled(True)
        self._view.solve_button.setDisabled(True)
        # Refill the board_states list and "resume" the while loop in self.run_animation from where it left off
        self.board_states = self.temp_board_states
        # Change the continue button to a pause button
        self._view.pause_button.setText("Pause (spacebar)")
        self._view.pause_button.repaint()
        self._view.pause_button.clicked.disconnect()
        self._view.pause_button.clicked.connect(self.pause_animation)
        QApplication.processEvents()
        self.run_animation()

    def change_speed(self):
        """Update the animation speed to the new value on the slider"""
        self.animation_speed = self._view.change_speed_slider.value()

    def get_empty_cells(self):
        """Store a list of empty_cell coordinates, we almost never need to deal with prefilled cells"""
        self.empty_cells = self._solver.return_list_of_empty_cells(self.board)

    def quit(self):
        """Run sys.exit()"""
        sysExit()

    def _connect_signals(self):
        """Set up controller interface by connecting signals from GUI components to relevant slots"""
        self._view.button3.clicked.connect(lambda: self.pick_random_board(3))
        self._view.button4.clicked.connect(lambda: self.pick_random_board(4))
        # self._view.button5.clicked.connect(lambda: self.pick_random_board(5))
        self._view.button6.clicked.connect(lambda: self.pick_random_board(6))
        # self._view.button7.clicked.connect(lambda: self.pick_random_board(7))
        # self._view.button8.clicked.connect(lambda: self.pick_random_board(8))
        self._view.button9.clicked.connect(lambda: self.pick_random_board(9))

        self._view.solve_button.clicked.connect(self.show_answer)
        self._view.check_button.clicked.connect(self.check_answer)
        # Multiple successive connect statements for the same signal connect that signal to all specified slots
        self._view.playthrough_button.clicked.connect(self.get_board_states)
        self._view.playthrough_button.clicked.connect(self.run_animation)
        self._view.pause_button.clicked.connect(self.pause_animation)
        self._view.quit_button.clicked.connect(self.quit)
        self._view.change_speed_slider.valueChanged.connect(self.change_speed)


def main():
    # Create an instance of the app
    backtrack_sudoku = QApplication([])

    # Create GUI
    view = sudoku_gui.SudokuUI()
    view.show()

    # Create model
    model = solve_sudoku_recursive

    # Instantiate controller with model and view
    SudokuCtrl(view=view, model=model)

    # Run app
    sysExit(backtrack_sudoku.exec_())


if __name__ == "__main__":
    main()


# TODO:
# Add boards of sizes 5, 7 and 8
# Make stats box dynamic and display real-time stats during playthrough
# Add functionality for user to enter their own board - FUTURE
