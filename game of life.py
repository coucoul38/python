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

def cellUpdate():
    global tabA
    newGrid = []
    for column in range(0,len(tabA)):
        newRow=[]
        for row in range(0,len(tabA)):
            #print("Column: ",column)
            #print("Row: ",row)
            if touchingCells(column,row)==3:
                newRow.append(1)
            elif touchingCells(column,row)==2:
                newRow.append(tabA[column][row])
            else:
                newRow.append(0)
        newGrid.append(newRow)
    tabA=newGrid

def update(iterations, timer):
    for i in range(iterations):
        cellUpdate()
        displayGrid()
        print("")
        time.sleep(timer)
        

createGrid(30)
#displayGrid()
#showTouchingCells(1,1)
#print(touchingCells(3,3))

#cellUpdate3(10,1)

update(1000,.5)