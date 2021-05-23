import time, keyboard, os, sys, numpy, cv2
from PIL import Image
import tesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR>"



def ScanImg():
    img = Image.open("Sudoku.jpg")
    text = tess.image2string(img)
    print(text)    

def Continue():
    dots = 0
    pE = "Press enter to continue"

    while not keyboard.is_pressed("enter"):
        os.system('cls')       
        flag = print(pE + (dots%5*"."))
        dots += 1
        time.sleep(1) 
    


ScanImg()