
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import numpy as np


class Row:
    def __init__(self, cols):
        self.Row = [cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], cols[6], cols[7], cols[8]]
    
    


class Sudoku9x9:
    def __init__(self):
        self.allValues = ([[1,0,0,0,0,0,0,0,0],
                           [0,1,0,0,0,0,0,0,0],
                           [0,0,1,0,0,0,0,0,0],
                           [0,0,0,1,0,0,0,0,0],
                           [0,0,0,0,1,0,0,0,0],
                           [0,0,0,0,0,1,0,0,0],
                           [0,0,0,0,0,0,1,0,0],
                           [0,0,0,0,0,0,0,1,0],
                           [0,0,0,0,0,0,0,0,1]])
        while True:
            self.PrintGrid()
            self.EnterValue()

        

    def PrintGrid(self):
        rowString = []
        rowString.append(("-------------  -------------  -------------\n| "))
        for y in range(9):
            for x in range(9):
                if (x + 1) % 3 == 0 and x != 8:
                    rowString.append(str(self.allValues[y][x]) + " |  | ")
                elif (x + 1) % 3 == 0:
                    rowString.append(str(self.allValues[y][x]) + " |\n")
                else:
                    rowString.append(str(self.allValues[y][x]) + " | ") 

            if (y + 1) % 3 == 0 and y != 8:
                rowString.append("-------------  -------------  -------------\n-------------  -------------  -------------\n| ")  
            else:
                rowString.append("-------------  -------------  -------------\n")
                rowString.append("| ")

        rowString.pop(len(rowString) - 1) #Just to remove the last '|'
        print("".join(rowString))

    def EnterValue(self):
        row, col, change = input("Enter the row nr, col nr and number you want to add: ").split()
        self.allValues[int(row)][int(col)] = int(change)


grid = Sudoku9x9()


    
        
#def digitalizeSudoku():