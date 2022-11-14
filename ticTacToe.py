

def play(player):
    input("")

tabA=[]
def createGrid():
    global tabA
    #on crée x colonnes
    for i in range(3):
        #on crée une ligne de longueur x
        tabB=[]
        for o in range(3):
            #on met un nombre aléatoire dans chaque case de la ligne (0=morte, 1=vivante)
            tabB.append("-")
        #on insère la ligne dans le tableau, créant une colonne
        tabA.append(tabB)

def displayGrid():
    global tabA
    for i in range(3):
        for o in range(3):
            #si la cellule est morte, afficher un carré noir
            if tabA[i][o]==1:
                print("⭕️", end='')
            #si la cellule est morte, afficher un carré blanc
            elif tabA[i][o]==2:
                print("❌",end='')
            else :
                print("⬜", end='')
        #on met une ligne vide, pour mieux différencier chaque grille
        print("", end='\n')

def checkForWin():
    global tabA

def ticTacToe():
    global tabA
    print("Pour jouer, utilisez les touches du pavé numérique")
    player1Score=0
    player2Score=0
    winner=False
    displayGrid
    while winner == False:
        entry=input("Joueur 1: ")
        if entry=="7":
            tabA[0][0]=1
        elif entry=="8":
            tabA[0][1]=1
        elif entry=="9":
            tabA[0][2]=1
        elif entry=="4":
            tabA[1][0]=1
        elif entry=="5":
            tabA[1][1]=1
        elif entry=="6":
            tabA[1][2]=1
        elif entry=="1":
            tabA[2][0]=1
        elif entry=="2":
            tabA[2][1]=1
        elif entry=="3":
            tabA[2][2]=1
        displayGrid()
        checkForWin()
        entry=input("Joueur 2: ")
        if entry=="7":
            tabA[0][0]=2
        elif entry=="8":
            tabA[0][1]=2
        elif entry=="9":
            tabA[0][2]=2
        elif entry=="4":
            tabA[1][0]=2
        elif entry=="5":
            tabA[1][1]=2
        elif entry=="6":
            tabA[1][2]=2
        elif entry=="1":
            tabA[2][0]=2
        elif entry=="2":
            tabA[2][1]=2
        elif entry=="3":
            tabA[2][2]=2
        displayGrid()
    
createGrid()
ticTacToe()