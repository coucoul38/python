import math

def play(player):
    input("")

tabA=[]
pos=[tabA]
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

    #check en bias de gauche à droite
    if tabA[0][0]==tabA[1][1]==tabA[2][2]:
        if tabA[0][0]==1:
            winner="player1"
        elif tabA[0][0]==2:
            winner="player2"
    #check en bias de droite à gauche
    if tabA[0][2]==tabA[1][1]==tabA[2][0]:
        if tabA[0][2]==1:
            winner="player1"
        elif tabA[0][2]==2:
            winner="player2"
    check1 = 0
    check2 = 0

    #check pour egalité
    checkTie = 0
    for i in range(3):
        for o in range(3):
            if tabA[i][o] != 0:
                checkTie = checkTie + 1
    if checkTie==9:
        winner="tie"
    return winner

def play(player):
    print("----------")
    print("Joueur ",player,end="")
    if player==1:
        print("⭕️",end="\n")
    if player==2:
        print("❌",end="\n")

    entry=input()
    if entry=="7":
        if(tabA[0][0]==0):
            tabA[0][0]=player
        else:
            print("Vous ne pouvez pas faire cette action")
            play(player)
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


def minimax(position, depth, maximizingPlayer):
    if depth==0 #or game over in position
        return None
    if maximizingPlayer:
        maxEval = -math.inf
        #for each child of the current position :
        for i in range(childs of pos):
            eval=minimax(child, depth-1, False)
            maxEval= max(maxEval,eval)
        return maxEval
    else :
        minEval = math.inf
        for i in range(childs of pos):
            eval=minimax(child, depth-1, False)
            minEval= max(minEval,eval)
        return minEval

def botMinimax():
    global pos
    pos=tabA
    currentPos=pos[0]
    minimax(currentPos, depth,True)
    # USE LINKED LISTS FOR CHILD MANAGEMENT

def botPlay():
    #win=False
    #possibleCases=0
    ##while win==False:
    #for i in range(3):
    #    for o in range(3):
    #        if tabA[i][o]==0:
    #            possibleCases=possibleCases+1
    #for case in range(possibleCases):
    #    allCases=[]
    #    for i in range():
    #        for o in range(3):
    #        if tabA[i][o]==0:
    #print(possibleCases)

    check1=0
    check2=0

    #horizontal counter
    played=False
    for col in range(3):
        for row in range(3):
            if tabA[col-1][row-1]==1:
                check1=check1+1
            if check1==2:
                for i in range(3):
                    if tabA[col-1][i]==0 and played==False:
                        tabA[col-1][i]=2
                        played=True
                check1=0
        check1=0
    #vertical counter
    for row in range(3):
        for col in range(3):
            if tabA[col-1][row-1]==1:
                check1=check1+1
            if check1==2:
                for i in range(3):
                    if tabA[i][row-1]==0 and played==False:
                        tabA[i][row-1]=2
                        played=True
                check1=0
        check1=0
    #diagonal counter
    for a in range(3):
        if tabA[a][a]==1:
            check1=check1+1
        if check1==2:
            for b in range(3):
                if tabA[b][b]==0 and played==False:
                    tabA[b][b]=2
                    played=True
            check1=0
    for a in range(3):
        if tabA[a][2-a]==1:
            check1=check1+1
        if check1==2:
            for b in range(3):
                if tabA[b][2-b]==0 and played==False:
                    tabA[b][2-b]=2
                    played=True
            check1=0
    if played==False :
        for i in range(3):
            for o in range(3):
                if tabA[i][o]==0 and played==False:
                    tabA[i][o]=2
                    played=True

def ticTacToe(bot=False):
    global tabA
    print("Pour jouer, utilisez les touches du pavé numérique")
    displayGrid()
    while True:
        for i in range(1,3):
            if bot==True and i==2:
                botPlay()
            else:
                play(i)

            displayGrid()
            if checkForWin()=="player1":
                print("LE JOUEUR 1 GAGNE! ⭕️")
                print("====================")
                return
            elif checkForWin()=="player2":
                print("LE JOUEUR 2 GAGNE! ❌")
                print("====================")
                return
            elif checkForWin()=="tie":
                print("EGALITE!")
                print("====================")
                return

createGrid()
ticTacToe(True)


#Algo bot
#Si le joueur aligne 2 points, le bloquer
#Sinon essayer de cap 3 coins : victoire lol
