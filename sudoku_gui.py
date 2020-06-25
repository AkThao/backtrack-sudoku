#!/usr/bin/env python3

import sys

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
        self.initUI()

    def initUI(self):
        # Set some main window properties
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        # self.createGrid()
        self.createMainWindow()

    def createMainWindow(self):
        self.mainWindow = QMainWindow()
        self.gridContainer = QFrame()
        self.gridContainer.setFixedWidth(360)
        self.gridContainer.setFixedHeight(360)
        self.gridContainer.setStyleSheet("border: 1px solid black")

        self.leftSide = QVBoxLayout()
        self.leftSide.addWidget(QLabel("Sudoku Game and Solver"))
        self.leftSide.addWidget(QLabel("Board size:"))

        self.createRadioGroup()
        self.leftSide.addWidget(self.boardSizeChoice)
        self.leftSide.addWidget(self.gridContainer)

        self.setLayout(self.leftSide)

    def createRadioGroup(self):
        self.boardSizeChoice = QWidget()
        self.boardSizeChoice.setFixedWidth(360)

        self.radioLayout = QHBoxLayout()

        button3 = QRadioButton("3x3")
        button3.toggled.connect(self.createGrid)
        button4 = QRadioButton("4x4")
        button4.toggled.connect(self.createGrid)
        button6 = QRadioButton("6x6")
        button6.toggled.connect(self.createGrid)
        button9 = QRadioButton("9x9")
        button9.toggled.connect(self.createGrid)

        self.radioLayout.addWidget(button3)
        self.radioLayout.addWidget(button4)
        self.radioLayout.addWidget(button6)
        self.radioLayout.addWidget(button9)

        self.boardSizeChoice.setLayout(self.radioLayout)


    def createGrid(self):
        gridLayout = QGridLayout()

        gridLayout.addWidget(QLineEdit("0"), 0, 0)
        gridLayout.addWidget(QLineEdit("0"), 0, 1)
        gridLayout.addWidget(QLineEdit("0"), 0, 2)
        gridLayout.addWidget(QLineEdit("0"), 1, 0)
        gridLayout.addWidget(QLineEdit("0"), 1, 1)
        gridLayout.addWidget(QLineEdit("0"), 1, 2)
        gridLayout.addWidget(QLineEdit("0"), 2, 0)
        gridLayout.addWidget(QLineEdit("0"), 2, 1)
        gridLayout.addWidget(QLineEdit("0"), 2, 2)

        self.gridContainer.setLayout(gridLayout)


def main():
    """Main function"""
    # Create an instance of QApplication
    sudoku_gui = QApplication(sys.argv)
    # window = QWidget()
    # window.setWindowTitle("Sudoku")
    # window.show()
    sudoku = Sudoku()
    sudoku.show()

    # Execute main loop
    sys.exit(sudoku_gui.exec_())


if __name__ == "__main__":
    main()