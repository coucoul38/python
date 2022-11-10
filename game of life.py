#tableau tabA len(x)
#dans tabA, nombre x de tableaux de longueur x

#tabA[0][1] --> valeur
#ensuite retourner toutes les cases adjacentes 

import random
import time

tabA=[]
def createGrid(x):
    #initialisation de la liste contenant chaque colonne
    
    #on crée x lignes
    for i in range(x):
        #on crée une ligne de longueur x 
        tabB=[]
        for o in range(x):
            #on met un nombre aléatoire dans chaque case
            tabB.append(random.randint(0,1))
        #on insère la ligne aux colonnes
        tabA.append(tabB)
    
    #for p in range(len(tabA)):
     #   print(tabA[p])
    #print()


def displayGrid():
    for i in range(len(tabA)):
        for o in range(len(tabA)):
            if(tabA[i][o]==0):
                print("🟥", end='')
            else :
                print("⬜", end='')
            #print(tabA[p])
        print("", end='\n')
    #print("", end='\n')


def touchingCells(column, row):
    #trouve toutes les cases adjacentes à celle séléctionée
    display = [
        [tabA[column-1][row-1],tabA[column-1][row],tabA[column-1][row+1]],
        [tabA[column][row-1],tabA[column][row], tabA[column][row+1]],
        [tabA[column+1][row-1],tabA[column+1][row],tabA[column+1][row+1]]
    ]
    return(display)


def showTouchingCells(column, row):
    #display le tableau de la fonction touchingCells
    for p in range(3):
        print(touchingCells(column,row)[p])
    print()


def countTouchingCells(column,row):
    adjacents=0
    for i in range(3):
        for o in range(3):
            if(touchingCells(column,row)[i][o]):
                adjacents=adjacents+1
    return(adjacents)


def cellUpdate(iterations, timer):
    for i in range(iterations):
        column = 0
        row=0
        for o in range(len(tabA)):
            for p in range(len(tabA)):
                row = row + 1
                if countTouchingCells(column, row)==3 :
                    tabA[column][row]=1
                elif countTouchingCells(column, row)>3 :
                    tabA[column][row]=0
                elif countTouchingCells(column, row) < 2:
                    tabA[column][row]=0
                time.sleep(timer)
                displayGrid()
                print()
            column = column + 1
            row = 0


createGrid(10)
displayGrid()
showTouchingCells(1,1)
print(countTouchingCells(1,1))

cellUpdate(100,1)