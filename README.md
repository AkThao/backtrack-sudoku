# backtrack-sudoku
## Sudoku Solver Using The Backtrack Algorithm

This project is about building an app that allows the user to try their hand at solving a range of sudoku puzzles of various sizes.

---

solve_sudoku.py contains all the functions necessary to solve a given board.

solve_sudoku_recursive.py is a newer and faster backtrack algorithm that uses recursion.

sudoku_gui.py contains all the code necessary to produce the GUI.

main.py is the controller that connects the model (solver) and the view (GUI).

There are programs to test both algorithms on 3x3, 4x4, 6x6 and 9x9 boards, but can generalise to solve any size board.
