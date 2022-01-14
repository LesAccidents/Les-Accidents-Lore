#import sys;print(sys.version)
from basics import screenClear, pressEnter, confirm, slowType
import colours as c
import chapters as chap
import players as p
from players import save
import time, os, sys, json
from bigText import bigText
#import sound #MUSIC

if p.savefile() == False:
    p.characterSelection()

while True:
    screenClear()
    chapSel = input("What chapter would you like to play? (1 - 5, 'si' or 'menu')\n") #asks what chapter they would like to play
    match chapSel: #depending on their choice, the correct chapter function will be called
        case '1':
            c.cyan("\nYou chose chapter 1: The Birth of a Mistake")
            time.sleep(1)
            if confirm() == True:
                chap.c1()
        case '2':
            c.cyan("\nYou chose chapter 2: The Attack of the Virus")
            time.sleep(1)
            if confirm() == True:
                chap.c2()
        case '3':
            c.cyan("\nYou chose chapter 3: Hussein's Trial")
            time.sleep(1)
            if confirm() == True:
                chap.c3()
        case '4':
            c.cyan("\nYou chose chapter 4: The Civil War")
            time.sleep(1)
            if confirm() == True:
                chap.c4()
        case '5':
            c.cyan("\nYou chose chapter 5: Mathieu's ASCENT")
            time.sleep(1)
            if confirm() == True:
                chap.c5()
        case 'si':
            c.cyan("\nYou chose the special issue: Cerial vs Milk")
            time.sleep(1)
            if confirm() == True:
                chap.csi()
        case 'menu':
            os.execl(sys.executable, sys.executable, *sys.argv)
        case _:
            c.red("\nPlease input a valid chapter.")
            time.sleep(1)