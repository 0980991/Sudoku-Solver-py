
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import numpy as np


class Sudoku3x3:
    def __init__(self, coordinate):
        if coordinate == "a":

        self.sudoku3x3 = [[1.1, 1.2, 1.3], [2.1, 2.2, 2.3], [3.1, 3.2, 3.3]]

    def Row(self, colNr):
        rowString = []
        for index in range(0, 3):
            
            rowString.append(str(self.sudoku3x3[colNr][index]))
            rowString.append(" | ")
            if index == 2 and colNr != 2:
                rowString.append(" | ")
            
        
        return (''.join(rowString))
    
    def PrintSquare(self):
        squareString = []
        for index in range(0, 3):
            squareString.append("-------------  -------------  -------------\n| ")
            for rowNr in range(0, 3):
                
                squareString.append(self.Row(rowNr))
            squareString.append("\n")
        squareString.append("-------------  -------------  -------------")
        print(''.join(squareString))
    
    


class Sudoku9x9:
    def __init__(self):
        allValues = np.matrix([[0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0]])
        
        #self.sudoku9x9 = [Sudoku3x3(), Sudoku3x3(), Sudoku3x3()]
        

    def PrintGrid(self):
        string3x3 = []
        for index in range(0, 3):
            self.sudoku9x9[index].PrintSquare()
'''
        for bigrow in sudokuSize:
            for row in sudoku9x9:
                for elem in row:
                     
                    print(elem, end=' | ')
                    
                if len(elem) % 3 == 0: 
                    print("\n")    
            print("----------------------------------")
'''
    #def getSudoku(self.sudoku9x9):


#Sudoku9x9.GetNegetNewGrid()

grid = Sudoku9x9()
grid.PrintGrid()

    
        
#def digitalizeSudoku():