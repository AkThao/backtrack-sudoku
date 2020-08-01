# !/usr/bin/env python3

from PyQt5 import sip

# Import QApplication and required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QLineEdit, QLabel, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt


class SudokuUI(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Sudoku"
        self.width = 800
        self.height = 800
        self.init_UI()

    def init_UI(self):
        # Set some main window properties
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.add_stylesheet()
        self.create_main_window()

    def create_main_window(self):
        self.main_window = QMainWindow()
        self.grid_container = QFrame()
        self.grid_container.setFixedWidth(400)
        self.grid_container.setFixedHeight(400)
        self.grid_container.setObjectName("grid_container")
        self.grid_container.setStyleSheet(self.styles)
        self.grid_layout = QGridLayout()
        self.placeholder_text = QLabel("Select a board size")
        self.placeholder_text.setAlignment(Qt.AlignCenter)
        self.placeholder_text.setObjectName("placeholder_text")
        self.placeholder_text.setStyleSheet(self.styles)
        self.placeholder_font = self.placeholder_text.font()
        self.placeholder_font.setPointSize(40)
        self.placeholder_text.setFont(self.placeholder_font)
        self.grid_layout.addWidget(self.placeholder_text)
        self.grid_container.setLayout(self.grid_layout)

        # Create left side of GUI
        self.left_side = QWidget()
        self.left_side_layout = QVBoxLayout()
        self.left_side.setLayout(self.left_side_layout)

        # Create right side of GUI
        self.right_side = QWidget()
        self.right_side_layout = QVBoxLayout()
        self.right_side.setLayout(self.right_side_layout)

        # Add left and right side to complete GUI
        self.full_app = QHBoxLayout()
        self.full_app.addWidget(self.left_side)
        self.full_app.addWidget(self.right_side)

        # Create and style title label and add to left side
        self.title = QLabel("Sudoku Game and Solver")
        self.title.setFixedWidth(400)
        self.title.setWordWrap(True)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setObjectName("title")
        self.title.setStyleSheet(self.styles)
        self.left_side_layout.addWidget(self.title)

        # Add board size buttons and grid to left side
        self.create_board_size_button_group()
        self.left_side_layout.addWidget(self.board_size_choice)
        self.left_side_layout.addWidget(self.grid_container)

        # Create solve button
        self.create_check_and_solve_buttons()

        self.setLayout(self.full_app)

    def add_stylesheet(self):
        with open("styles.css") as file:
            self.styles = file.read()

    def create_check_and_solve_buttons(self):
        self.solve_button = QPushButton("SOLVE", self)
        self.check_button = QPushButton("CHECK SOLUTION", self)
        self.playthrough_button = QPushButton("PLAYTHROUGH", self)

        self.solve_button.setDisabled(True)
        self.check_button.setDisabled(True)
        self.playthrough_button.setDisabled(True)

        self.right_side_layout.addWidget(self.solve_button)
        self.right_side_layout.addWidget(self.check_button)
        self.right_side_layout.addWidget(self.playthrough_button)

    def create_board_size_button_group(self):
        self.board_size_choice = QWidget()
        self.board_size_choice.setFixedWidth(360)
        self.board_size_choice.setFixedHeight(120)
        self.board_sizes = QWidget()

        self.button_layout = QVBoxLayout()
        self.button_group = QHBoxLayout()

        self.button3 = QPushButton("3x3", self)
        self.button3.setToolTip("Pick a random 3x3 grid")
        self.button3.setObjectName("board_size_button")
        self.button3.setStyleSheet(self.styles)

        self.button4 = QPushButton("4x4", self)
        self.button4.setToolTip("Pick a random 4x4 grid")
        self.button4.setObjectName("board_size_button")
        self.button4.setStyleSheet(self.styles)

        self.button6 = QPushButton("6x6", self)
        self.button6.setToolTip("Pick a random 6x6 grid")
        self.button6.setObjectName("board_size_button")
        self.button6.setStyleSheet(self.styles)

        self.button9 = QPushButton("9x9", self)
        self.button9.setToolTip("Pick a random 9x9 grid")
        self.button9.setObjectName("board_size_button")
        self.button9.setStyleSheet(self.styles)

        self.button_group.addWidget(self.button3)
        self.button_group.addWidget(self.button4)
        self.button_group.addWidget(self.button6)
        self.button_group.addWidget(self.button9)

        self.board_sizes.setLayout(self.button_group)

        self.board_size_label = QLabel("Board size:")
        self.board_size_label.setObjectName("board_size_label")
        self.board_size_label.setStyleSheet(self.styles)
        self.button_layout.addWidget(self.board_size_label)
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
                cell.setObjectName("empty_cell")
                cell.setStyleSheet(self.styles)
                if (starting_board[i][j] != 0):
                    cell.setObjectName("prefilled_cell")
                    cell.setEnabled(False)
                cell_font = cell.font()
                cell_font.setPointSize(cell.frameGeometry().width() / 2)
                cell.setFont(cell_font)
                self.grid_layout.addWidget(cell, i, j)

        self.grid_layout.setSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_container.setLayout(self.grid_layout)
