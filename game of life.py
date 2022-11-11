#tableau tabA len(x)
#dans tabA, nombre x de tableaux de longueur x

#tabA[0][1] --> valeur
#ensuite retourner toutes les cases adjacentes 

import random
import time

tabA=[]
def createGrid(x):
    global tabA
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
    global tabA
    for i in range(len(tabA)):
        for o in range(len(tabA)):
            if(tabA[i][o]==0):
                print("⬛", end='')
            else :
                print("⬜", end='')
            #print(tabA[p])
        print("", end='\n')
    #print("", end='\n')


def touchingCells(column, row):
    global tabA
    #trouve toutes les cases adjacentes à celle séléctionée
    #if (column>0 & column<len(tabA)-1) & (row>0 & row < len(tabA)-1):
    display = [
        [tabA[column-1][row-1],tabA[column-1][row],tabA[column-1][row+1]],
        [tabA[column][row-1],"X", tabA[column][row+1]],
        [tabA[column+1][row-1],tabA[column+1][row],tabA[column+1][row+1]]
    ]
    #elif column==0 :
    #    display = [
    #        [tabA[column][row-1],"X", tabA[column][row+1]],
    #        [tabA[column+1][row-1],tabA[column+1][row],tabA[column+1][row+1]]
    #    ]
    #elif column==len(tabA)-1 :
    #    display = [
    #        [tabA[column-1][row-1],tabA[column-1][row],tabA[column-1][row+1]],
    #        [tabA[column][row-1],"X", tabA[column][row+1]]
    #    ]
    #
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
    global tabA
    for i in range(iterations):
        column = 0
        row=0
        for o in range(len(tabA)):
            print("o")
            for p in range(len(tabA)):
                print("p")
                row = row + 1
                if countTouchingCells(column, row)==3 :
                    tabA[column][row]=1
                elif countTouchingCells(column, row)>3 :
                    tabA[column][row]=0
                elif countTouchingCells(column, row) < 2:
                    tabA[column][row]=0
                time.sleep(timer)
            row = 0
        column = column + 1
        displayGrid()
        print()
    
def cellUpdate2(iterations, timer):
    global tabA
    for a in range(iterations):
        newGrid = []
        for i in range(len(tabA)):
            #on crée une ligne de longueur x 
            newB=[]
            for o in range(len(tabA)):
                #on met un nombre aléatoire dans chaque case
                if countTouchingCells(i,o)==3 :
                    newB.append(1)
                elif countTouchingCells(i,o)>3 | countTouchingCells(i,o)<2:
                    newB.append(0)
            #on insère la ligne aux colonnes
            newGrid.append(newB)
        time.sleep(timer)
        tabA=newGrid


createGrid(4)
displayGrid()
showTouchingCells(1,1)
print(countTouchingCells(1,1))

cellUpdate2(1,1)