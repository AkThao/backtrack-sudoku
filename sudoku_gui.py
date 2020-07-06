# !/usr/bin/env python3

import sys
from PyQt5 import sip
import boards
import random

# Import QApplication and required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QLineEdit, QLabel, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt


class Sudoku(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Sudoku"
        self.width = 800
        self.height = 800
        self.init_UI()
        self.create_boards_lists()

    def create_boards_lists(self):
        self.boards_lists = {
            3: boards.boards_3,
            4: boards.boards_4,
            6: boards.boards_6,
            9: boards.boards_9
        }

    def init_UI(self):
        # Set some main window properties
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.create_main_window()

    def create_main_window(self):
        self.main_window = QMainWindow()
        self.grid_container = QFrame()
        self.grid_container.setFixedWidth(400)
        self.grid_container.setFixedHeight(400)
        self.grid_container.setStyleSheet("border: 2px solid black")
        self.grid_layout = QGridLayout()
        self.placeholder_text = QLabel("Select a board size")
        self.placeholder_text.setAlignment(Qt.AlignCenter)
        self.placeholder_text.setStyleSheet("border: none")
        self.placeholder_font = self.placeholder_text.font()
        self.placeholder_font.setPointSize(40)
        self.placeholder_text.setFont(self.placeholder_font)
        self.grid_layout.addWidget(self.placeholder_text)
        self.grid_container.setLayout(self.grid_layout)

        self.left_side = QVBoxLayout()
        self.left_side.addWidget(QLabel("Sudoku Game and Solver"))

        self.create_button_group()
        self.left_side.addWidget(self.board_size_choice)
        self.left_side.addWidget(self.grid_container)

        self.setLayout(self.left_side)

    def pick_random_board(self, board_size):
        board_list = self.boards_lists[board_size]
        random_board = random.choice(board_list)
        self.create_grid(board_size, random_board)

    def create_button_group(self):
        self.board_size_choice = QWidget()
        self.board_size_choice.setFixedWidth(360)
        self.board_size_choice.setFixedHeight(100)
        self.board_sizes = QWidget()

        self.button_layout = QVBoxLayout()
        self.button_group = QHBoxLayout()

        button3 = QPushButton("3x3", self)
        button3.setToolTip("Pick a random 3x3 grid")
        button3.clicked.connect(lambda: self.pick_random_board(3))
        button4 = QPushButton("4x4", self)
        button4.setToolTip("Pick a random 4x4 grid")
        button4.clicked.connect(lambda: self.pick_random_board(4))
        button6 = QPushButton("6x6", self)
        button6.setToolTip("Pick a random 6x6 grid")
        button6.clicked.connect(lambda: self.pick_random_board(6))
        button9 = QPushButton("9x9", self)
        button9.setToolTip("Pick a random 9x9 grid")
        button9.clicked.connect(lambda: self.pick_random_board(9))

        self.button_group.addWidget(button3)
        self.button_group.addWidget(button4)
        self.button_group.addWidget(button6)
        self.button_group.addWidget(button9)

        self.board_sizes.setLayout(self.button_group)

        self.button_layout.addWidget(QLabel("Board size:"))
        self.button_layout.addWidget(self.board_sizes)

        self.board_size_choice.setLayout(self.button_layout)

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clear_layout(child.layout())
        sip.delete(layout)

    def create_grid(self, board_size, starting_board):
        self.clear_layout(self.grid_layout)

        self.grid_layout = QGridLayout()

        for i in range(board_size):
            for j in range(board_size):
                cell = QLineEdit(str(starting_board[i][j]))
                cell.setFixedWidth(360/board_size)
                cell.setFixedHeight(360/board_size)
                cell.setAlignment(Qt.AlignCenter)
                cell.setStyleSheet(
                    "padding: 0; margin: 0; border: 1px solid black")
                if (starting_board[i][j] != 0):
                    cell.setStyleSheet("background-color: rgb(255, 107, 107)")
                cell_font = cell.font()
                cell_font.setPointSize(cell.frameGeometry().width() / 2)
                cell.setFont(cell_font)
                self.grid_layout.addWidget(cell, i, j)

        self.grid_layout.setSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_container.setLayout(self.grid_layout)


def main():
    """Main function"""
    # Create an instance of QApplication
    sudoku_gui = QApplication(sys.argv)
    sudoku = Sudoku()
    sudoku.show()

    # Execute main loop
    sys.exit(sudoku_gui.exec_())


if __name__ == "__main__":
    main()
