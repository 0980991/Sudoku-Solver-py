
from pyautogui import *
import pyautogui, json, time, keyboard, random, os
import numpy as np


class MenUI:
    def __init__(self):

        
        sudoku = Sudoku9x9()
        while(True):
            choice = input((25 * "-") + "\nWelcome to SUDOKU SOLVER 9000\n" + (25 * "-") + "\n\nWhat would you like to do today?\n" + (25 * "-") + "\n1. Load Sudoku\n2. Play Sudoku\n3. Solve Sudoku\n4. Get on with your day\n")
            
            if choice == "1":
                sudoku.ClearTerminal()
                sudoku.LoadSudoku()
            elif choice == "2":
                sudoku.ClearTerminal()
                sudoku.PlaySudoku()
            elif choice == "3":
                sudoku.ClearTerminal()
                sudoku.SolveSudoku()
            elif choice == "4":
                sudoku.ClearTerminal()
                quit() 

        
class Row:
    def __init__(self, cols):
        self.Row = [cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], cols[6], cols[7], cols[8]]
    
class SudokuScan:
    def __init__(self, filename):
        pass


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

        self.allValues = None
        
        

    def PlaySudoku(self):
        if self.allValues != None:

            while True:
                self.PrintGrid()
                self.EnterValue()
        
        print("Please load a sudoku from a JSON file\n\n")
        self.EnterToContinue()
        self.ClearTerminal()      

    def LoadSudoku(self):
        choice = ""
        while choice not in ["1", "2"]:
            choice = input("Where would you like to load a sudoku from?\n" + (20*"-") + "\n1. Import a Json file\n2. Scan a jpg image\n")
            
            if choice == "1":
                self.ClearTerminal()
                name = input("please enter the name of the json file:_____.json\n")
                self.allValues = (json.load(open(os.path.join(sys.path[0], name + ".json"))))["values"] #sys.path[0] indicates the local directory
            elif choice == "2":
                self.ClearTerminal
                name = input("Please enter the name of the jpg file: ______.jpg\n")
                self.ScanImage()
            self.ClearTerminal()

        print(name + " has been loaded successfully!\n\n")
        self.EnterToContinue()
        self.ClearTerminal()
    
    def ScanImage(self):
        pass

    def SolveSudoku(self):  
        for row in range(9):
            for col in range(9):
                if self.allValues[row][col] == 0:
                    for nr in range(1, 10):
                        if self.IsPossible(row, col, nr):
                            self.allValues[row][col] = nr
                            self.SolveSudoku()
                            self.allValues[row][col] = 0
                    return
        self.PrintGrid()
        input("continue.....")

    def ClearTerminal(self):
        os.system("cls")
    
    def EnterToContinue(self):
        self.ClearTerminal()
        pE = "Press enter to continue..."
         
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
            self.ClearTerminal() 
        else:
            self.ClearTerminal() 
            input("-------------------------------\n| This move is not possible! |\n-------------------------------\n")

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



                

MenUI()


    
        
#def digitalizeSudoku():