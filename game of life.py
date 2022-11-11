#tableau tabA len(x)
#dans tabA, nombre x de tableaux de longueur x

#tabA[0][1] --> valeur
#ensuite retourner toutes les cases adjacentes 

import random
import time

tabA=[]
def createGrid(x):
    global tabA
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
    alive=0-tabA[column][row]
    for C in range(column-1,column+2):
        for R in range(row-1,row+2):
            #print("C,R : ",C,R)
            if C >= 0 and C < len(tabA) and R>=0 and R<len(tabA):
                alive = alive + tabA[C][R]
                #print("Tab C,R : ",tabA[C][R])
            
    return alive
    #trouve toutes les cases adjacentes à celle séléctionée


#PAS UTILE
#def countTouchingCells(column,row):
#    adjacents=0
#    for i in range(3):
#        for o in range(3):
#            if(touchingCells(column,row)[i][o]):
#                adjacents=adjacents+1
#    return(adjacents)


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
                if touchingCells(i,o)==3 :
                    newB.append(1)
                elif touchingCells(i,o)>3 | touchingCells(i,o)<2:
                    newB.append(0)
            #on insère la ligne aux colonnes
            newGrid.append(newB)
        time.sleep(timer)
        tabA=newGrid

def cellUpdate3(iterations, timer):
    global tabA
    newGrid = []
    for ite in range(iterations):
        for column in range(0,len(tabA)-1):
            newRow=[]
            for row in range(0,len(tabA)-1):
                if touchingCells(column,row)==3:
                    newRow.append(1)
                elif touchingCells(column,row)==2:
                    newRow.append(tabA[column][row])
                else:
                    newRow.append(0)
            newGrid.append(newRow)
        tabA=newGrid
        time.sleep(timer)


createGrid(4)
displayGrid()
#showTouchingCells(1,1)
print(touchingCells(3,3))

cellUpdate3(10,1)