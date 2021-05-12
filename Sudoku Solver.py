
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import numpy as np


class sudokuSquare:
    sudoku_square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

class sudokuGrid:
    def getNewGrid(self):
        sudoku_square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        sudoku_grid   = [sudoku_square, sudoku_square, sudoku_square]
        sudoku_size   = [sudoku_grid,   sudoku_grid,   sudoku_grid  ]
        for bigrow in sudoku_size:
            for row in sudoku_grid:
                for elem in row:
                     
                    print(elem, end=' || ')
                    
                if len(elem) % 3 == 0: 
                    print("\n")    
            print("======================================")
    #def getSudoku(self.sudoku_grid):


sudokuGrid.getNewGrid()

    
        
#def digitalizeSudoku():