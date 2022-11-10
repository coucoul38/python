#tableau tabA len(x)
#dans tabA, nombre x de tableaux de longueur x

#tabA[0][1] --> valeur
#ensuite retourner toutes les cases adjacentes 

import random
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
    
    for p in range(len(tabA)):
        print(tabA[p])

def showTouchingCoordinates(column, row):
    #display toutes les cases adjacentes à celle séléctionée
    display = [
        [tabA[column-1][row-1],tabA[column-1][row],tabA[column-1][row+1]],
        [tabA[column][row-1],tabA[column][row], tabA[column][row+1]],
        [tabA[column+1][row-1],tabA[column+1][row],tabA[column+1][row+1]]
    ]
    for p in range(len(display)):
        print(display[p])


createGrid(10)
showTouchingCoordinates(1,1)
