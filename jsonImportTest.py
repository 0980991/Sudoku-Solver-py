import time, keyboard, os, sys
dots = 0
pE = "Press enter to continue"

while not keyboard.is_pressed("enter"):
    os.system('cls')       
    flag = print(pE + (dots%5*"."))
    dots += 1
    time.sleep(1) 
    
    

