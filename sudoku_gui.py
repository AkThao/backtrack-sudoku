# !/usr/bin/env python3

import sys
from PyQt5 import sip
import boards

# Import QApplication and required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QLineEdit, QLabel, QFrame, QRadioButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Sudoku(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Sudoku"
        self.width = 800
        self.height = 800
        self.grid_layout = None
        self.init_UI()

    def init_UI(self):
        # Set some main window properties
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.create_main_window()

    def create_main_window(self):
        self.main_window = QMainWindow()
        self.grid_container = QFrame()
        self.grid_container.setFixedWidth(360)
        self.grid_container.setFixedHeight(360)
        self.grid_container.setStyleSheet("border: 1px solid black")

        self.left_side = QVBoxLayout()
        self.left_side.addWidget(QLabel("Sudoku Game and Solver"))

        self.create_radio_group()
        self.left_side.addWidget(self.board_size_choice)
        self.left_side.addWidget(self.grid_container)

        self.setLayout(self.left_side)

    def pick_random_board(self, board_size):
        self.random_board

    def create_radio_group(self):
        self.board_size_choice = QWidget()
        self.board_size_choice.setFixedWidth(360)
        self.board_size_choice.setFixedHeight(100)
        self.board_size_choice.setStyleSheet("border: 1px dashed green")
        self.board_sizes = QWidget()

        self.radio_layout = QVBoxLayout()
        self.radio_group = QHBoxLayout()

        button3 = QPushButton("3x3", self)
        button3.clicked.connect(lambda: self.create_grid(3))
        button4 = QPushButton("4x4", self)
        button4.clicked.connect(lambda: self.create_grid(4))
        button6 = QPushButton("6x6", self)
        button6.clicked.connect(lambda: self.create_grid(6))
        button9 = QPushButton("9x9", self)
        button9.clicked.connect(lambda: self.create_grid(9))

        self.radio_group.addWidget(button3)
        self.radio_group.addWidget(button4)
        self.radio_group.addWidget(button6)
        self.radio_group.addWidget(button9)

        self.board_sizes.setLayout(self.radio_group)

        self.radio_layout.addWidget(QLabel("Board size:"))
        self.radio_layout.addWidget(self.board_sizes)

        self.board_size_choice.setLayout(self.radio_layout)

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clear_layout(child.layout())
        sip.delete(layout)

    def create_grid(self, board_size):
        if self.grid_layout is not None:
            self.clear_layout(self.grid_layout)

        self.grid_layout = QGridLayout()

        for i in range(board_size):
            for j in range(board_size):
                self.grid_layout.addWidget(QLineEdit("0"), i, j)
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
