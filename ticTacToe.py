

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
            tabB.append(0)
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
    col=0
    row=0
    check1=0
    check2=0
    winner = "none"
    #check for horizontal win
    for col in range(3):
        for row in range(3):
            if tabA[col-1][row-1]==1:
                check1=check1+1
            elif tabA[col-1][row-1]==2:
                check2=check2+1
            if check1==3:
                winner="player1"
            elif check2==3:
                winner="player2"
        check1=0
        check2=0
    #check for vertical wins
    for row in range(3):
        for col in range(3):
            if tabA[col-1][row-1]==1:
                check1=check1+1
            elif tabA[col-1][row-1]==2:
                check2=check2+1
            if check1==3:
                winner="player1"
            elif check2==3:
                winner="player2"
        check1=0
        check2=0

    #
    for case in range(3):
        if tabA[case-1][case-1]==1:
            check1=check1+1
        elif tabA[case-1][case-1]==2:
            check2=check2+1
        if check1==3:
            winner="player1"
        elif check2==3:
            winner="player2"
    
    if tabA[0][2]==tabA[1][1]==tabA[2][0]:
        if tabA[0][2]==1:
            winner="player1"
        elif tabA[0][2]==2:
            winner="player2"
    
        
    
    check1 = 0
    check2 = 0

    print(winner)
    return winner

def play(player):
    print("Joueur ",player," :")
    entry=input()
    if entry=="7":
        if(tabA[0][0]==0):
            tabA[0][0]=player
    elif entry=="8":
        if(tabA[0][1]==0):
            tabA[0][1]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="9":
        if(tabA[0][2]==0):
            tabA[0][2]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="4":
        if(tabA[1][0]==0):
            tabA[1][0]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="5":
        if(tabA[1][1]==0):
            tabA[1][1]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="6":
        if(tabA[1][2]==0):
            tabA[1][2]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="1":
        if(tabA[2][0]==0):
            tabA[2][0]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="2":
        if(tabA[2][1]==0):
            tabA[2][1]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    elif entry=="3":
        if(tabA[2][2]==0):
            tabA[2][2]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
    else:
        print("Erreur")
        play(player)

def ticTacToe():
    global tabA
    print("Pour jouer, utilisez les touches du pavé numérique")
    player1Score=0
    player2Score=0
    winner=False
    displayGrid
    while winner == False:
        play(1)
        displayGrid()
        if checkForWin()!="none":
            return
        play(2)
        displayGrid()
        if checkForWin()!="none":
            return
    
createGrid()
ticTacToe()