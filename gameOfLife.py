#tableau tabA len(x)
#dans tabA, nombre x de tableaux de longueur x

#tabA[0][1] --> valeur
#ensuite retourner toutes les cases adjacentes 

import random
import time

tabA=[]
def createGrid(x):
    global tabA
    #on crée x colonnes
    for i in range(x):
        #on crée une ligne de longueur x
        tabB=[]
        for o in range(x):
            #on met un nombre aléatoire dans chaque case de la ligne
            tabB.append(random.randint(0,1))
        #on insère la ligne dans le tableau, créant une colonne
        tabA.append(tabB)


# Interface graphique du jeu
def displayGrid():
    global tabA
    for i in range(len(tabA)):
        for o in range(len(tabA)):
            #si la cellule est morte, afficher un carré noir
            if(tabA[i][o]==0):
                print("⬛", end='')
            #si la cellule est morte, afficher un carré blanc
            else :
                print("⬜", end='')
        #on met une ligne vide, pour mieux différencier chaque grille
        print("", end='\n')


#Calcule le nombre de case vivantes adjacentes à un case
def touchingCells(column, row):
    global tabA
    #si la case choisie est en vie, cette fonction va la compter, c'est pourquoi je soustrait son état(vivante=1, morte=0) au nombre de case en vie
    alive=0-tabA[column][row]
    for C in range(column-1,column+2):
        for R in range(row-1,row+2):
            #Ne pas séléctionner de cases en dehors de la grille
            if C >= 0 and C < len(tabA) and R>=0 and R<len(tabA):
                #On ajoute l'état de la case adjacente aux cases en vie (vivante=1, morte=0)
                alive = alive + tabA[C][R]
    #On renvoie le nombre de cases adjacentes en vie
    return alive

#Cette fonction update la grille
def cellUpdate():
    global tabA
    #On crée une nouvelle grille, pour modifier toutes les cellules à la fois
    newGrid = []
    for column in range(0,len(tabA)):
        newRow=[]
        #On crée une nouvelle ligne
        for row in range(0,len(tabA)):
            #Si la cellule a 3 voisines en vie, elle est forcemment en vie
            if touchingCells(column,row)==3:
                newRow.append(1)
            #Si la cellule a 2 voisines en vie, elle ne change pas d'état
            elif touchingCells(column,row)==2:
                #on copie donc la valeur de la case de l'ancien tableau vers le nouveau
                newRow.append(tabA[column][row])
            #Sinon, la cellule est morte (moins de 2 voisines en vie, ou plus de 3)
            else:
                newRow.append(0)
        #On insère la ligne dans le nouveau tableau, créant une colonne
        newGrid.append(newRow)
    #Finalemment, on remplace l'ancien tableau par le nouveau pour le mettre à jour
    tabA=newGrid


#Cette fonction va update la grille x fois avec un temps d'attente entre chaque update
def update(iterations, timer):
    for i in range(iterations):
        #Pour chaque update, on met à jours les cellules, affiche la nouvelle grille et attends avant la prochaine update
        cellUpdate()
        displayGrid()
        print("")
        time.sleep(timer)
        

#Lancement du jeu
createGrid(30)
update(1000,.5)


#Pour savoir le nombre de cellules en vie autour d'une cellule précise
#print(touchingCells(3,3))