# !/usr/bin/env python3

import sys
from PyQt5 import sip

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
        self.gridLayout = None
        self.initUI()

    def initUI(self):
        # Set some main window properties
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.createMainWindow()

    def createMainWindow(self):
        self.mainWindow = QMainWindow()
        self.gridContainer = QFrame()
        self.gridContainer.setFixedWidth(360)
        self.gridContainer.setFixedHeight(360)
        self.gridContainer.setStyleSheet("border: 1px solid black")

        self.leftSide = QVBoxLayout()
        self.leftSide.addWidget(QLabel("Sudoku Game and Solver"))

        self.createRadioGroup()
        self.leftSide.addWidget(self.boardSizeChoice)
        self.leftSide.addWidget(self.gridContainer)

        self.setLayout(self.leftSide)

    def createRadioGroup(self):
        self.boardSizeChoice = QWidget()
        self.boardSizeChoice.setFixedWidth(360)
        self.boardSizeChoice.setFixedHeight(100)
        self.boardSizeChoice.setStyleSheet("border: 1px dashed green")
        self.boardSizes = QWidget()

        self.radioLayout = QVBoxLayout()
        self.radioGroup = QHBoxLayout()

        button3 = QRadioButton("3x3")
        button3.toggled.connect(lambda: self.createGrid(3))
        button4 = QRadioButton("4x4")
        button4.toggled.connect(lambda: self.createGrid(4))
        button6 = QRadioButton("6x6")
        button6.toggled.connect(lambda: self.createGrid(6))
        button9 = QRadioButton("9x9")
        button9.toggled.connect(lambda: self.createGrid(9))

        self.radioGroup.addWidget(button3)
        self.radioGroup.addWidget(button4)
        self.radioGroup.addWidget(button6)
        self.radioGroup.addWidget(button9)

        self.boardSizes.setLayout(self.radioGroup)

        self.radioLayout.addWidget(QLabel("Board size:"))
        self.radioLayout.addWidget(self.boardSizes)

        self.boardSizeChoice.setLayout(self.radioLayout)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())
        sip.delete(layout)

    def createGrid(self, board_size):
        if self.gridLayout is not None:
            self.clearLayout(self.gridLayout)

        self.gridLayout = QGridLayout()

        for i in range(board_size):
            for j in range(board_size):
                self.gridLayout.addWidget(QLineEdit("0"), i, j)
        self.gridContainer.setLayout(self.gridLayout)


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
