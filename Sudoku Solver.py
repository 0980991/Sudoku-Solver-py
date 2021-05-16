
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import numpy as np

class MenUI:
    def __init__(self):
        
        while(True):
            choice = input((25 * "-") + "\nWelcome to SUDOKU SOLVER 9000\n" + (25 * "-") + "\n\nWhat would you like to do today?\n" + (25 * "-") + "\n1. Load Sudoku\n2. Play Sudoku\n3. Solve Sudoku\n4. Get on with your day\n")
            
            if choice == "1":
                Sudoku9x9.LoadSudoku()
            elif choice == "2":
                return
            elif choice == "3":
                Sudoku9x9.SolveSudoku()
            elif choice == "4":
                quit() 

        
class Row:
    def __init__(self, cols):
        self.Row = [cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], cols[6], cols[7], cols[8]]
    
    


class Sudoku9x9:
    def __init__(self):
        self.sudok =     ([[1,0,0,  0,0,2,  4,0,9],
                           [7,0,0,  0,0,4,  0,0,0],
                           [0,4,0,  7,6,8,  0,0,0],
                           
                           [4,0,1,  0,2,9,  0,3,5],
                           [3,0,0,  0,0,5,  0,0,7],
                           [0,8,5,  3,0,0,  2,0,4],

                           [0,0,0,  0,4,0,  0,0,3],
                           [0,1,0,  0,5,0,  0,4,0],
                           [8,3,4,  1,9,0,  6,0,0]])

        self.allValues = ([[1,0,0,  0,0,2,  4,0,9],
                           [7,0,0,  0,0,4,  0,0,0],
                           [0,4,0,  7,6,8,  0,0,0],
                           
                           [4,0,1,  0,2,9,  0,3,5],
                           [3,0,0,  0,0,5,  0,0,7],
                           [0,8,5,  3,0,0,  2,0,4],

                           [0,0,0,  0,4,0,  0,0,3],
                           [0,1,0,  0,5,0,  0,4,0],
                           [8,3,4,  1,9,0,  6,0,0]])

        MenUI()
        while True:
            
            self.PrintGrid()
            self.EnterValue()

        
    def LoadSudoku(self):
        pass
    
    def SolveSudoku(self):
        pass

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
        row, col, nr = input("Enter the row nr, col nr and number you want to add or type 'quit 0 0' to return to the menu: ").split()

        if row == "quit":
            row = 0 #If I dont have this line 99 will give me an error
            MenUI()

        row, col, nr = int(row), int(col), int(nr)

        if self.IsPossible(row, col, nr):
            self.allValues[int(row)][int(col)] = int(nr)
        else: 
            print("No way josé")

    def IsPossible(self, row, col, nr):
        for n in range(9):
            if self.allValues[row][n] == nr:
                return False

        for n in range(9):
            if self.allValues[col][n] == nr:
                return False

        #To calculate the top left corner of the square you are placing the number in.
        x0 = (col // 3) * 3
        y0 = (row // 3) * 3        
        for i in range(3):
            for j in range(3):
                if self.allValues[x0 + i][y0 + j] == nr:
                    return False
        return True

                


grid = Sudoku9x9()


    
        
#def digitalizeSudoku():