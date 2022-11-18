import math
import copy

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

def checkForWin(list):
    check1=0
    check2=0
    winner = "none"
    #check for horizontal win
    for col in range(3):
        for row in range(3):
            if list[col-1][row-1]==1:
                check1=check1+1
            elif list[col-1][row-1]==2:
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
            if list[col-1][row-1]==1:
                check1=check1+1
            elif list[col-1][row-1]==2:
                check2=check2+1
            if check1==3:
                winner="player1"
            elif check2==3:
                winner="player2"
        check1=0
        check2=0

    #check en bias de gauche à droite
    if list[0][0]==list[1][1]==list[2][2]:
        if list[0][0]==1:
            winner="player1"
        elif list[0][0]==2:
            winner="player2"
    #check en bias de droite à gauche
    if list[0][2]==list[1][1]==list[2][0]:
        if list[0][2]==1:
            winner="player1"
        elif tabA[0][2]==2:
            winner="player2"
    check1 = 0
    check2 = 0

    #check pour egalité
    checkTie = 0
    for i in range(3):
        for o in range(3):
            if list[i][o] != 0 and winner=="none":
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

def minimax(maximizingPlayer):
    moves=[]
    bestMove=[-1,-1]
    if maximizingPlayer=="player2":
        minimizingPlayer="player1"
    elif maximizingPlayer=="player1":
        minimizingPlayer="player2"
    else:
        print("Error : wrong player ID")
        return()
    currentPlayer = 2 #this function is first called when the bot plays
    for row in range(3):
        for col in range(3):
            if tabA[row][col]==0:
                nextTab=copy.deepcopy(tabA)
                nextTab[row][col]=currentPlayer
                #print("Current player : ", currentPlayer)
                win=checkForWin(nextTab)
                score=0
                if win=="tie":
                    score=0
                elif win==minimizingPlayer:
                    score=-1
                    bestMove=[row, col]
                    #return(nextTab)
                result=[[row, col],score]
                moves.append(result)
    if score==0:
        print("Checking enemy possibility to win")
        currentPlayer=1
        for row in range(3):
            for col in range(3):
                if tabA[row][col]==0:
                    nextTab=copy.deepcopy(tabA)
                    nextTab[row][col]=currentPlayer
                    #print("Current player : ", currentPlayer)
                    win=checkForWin(nextTab)
                    score=0
                    if win=="tie":
                        score=0
                    elif win==maximizingPlayer:
                        score=1
                        bestMove=[row, col]
                        #return(nextTab)
                    result=[[row, col],score]
                    moves.append(result)
    else:
        print("Exploring every possible outcome")
        currentPlayer=2
        counter=0
        for row in range(3):
            for col in range(3):
                if tabA[row][col]==0:
                    counter=counter+1
        for play in range(counter):
            for row in range(3):
                for col in range(3):
                    if tabA[row][col]==0:
                        nextTab=copy.deepcopy(tabA)
                        nextTab[row][col]=currentPlayer
                        #print("Current player : ", currentPlayer)
                        win=checkForWin(nextTab)
                        score=0
                        if win=="tie":
                            score=0
                        elif win==maximizingPlayer:
                            score=1
                            bestMove=[row, col]
                            #return(nextTab)
                        result=[[row, col],score]
                        moves.append(result)
            
            if currentPlayer==2:
                currentPlayer=1
            else:
                currentPlayer=2

    #print(moves)
    print("Bestmove : ",bestMove)
    return bestMove

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
    played=False
    bestmove=minimax("player1")
    if bestmove[0]!=-1 and bestmove[1]!=-1 and played==False:
        tabA[bestmove[0]][bestmove[1]]=2
        played=True
    elif played==False :
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
            minimax("player1")
            if bot==True and i==2:
                botPlay()
            else:
                play(i)

            displayGrid()
            if checkForWin(tabA)=="player1":
                print("LE JOUEUR 1 GAGNE! ⭕️")
                print("====================")
                return
            elif checkForWin(tabA)=="player2":
                print("LE JOUEUR 2 GAGNE! ❌")
                print("====================")
                return
            elif checkForWin(tabA)=="tie":
                print("EGALITE!")
                print("====================")
                return

createGrid()
ticTacToe(True)


#Algo bot
#Si le joueur aligne 2 points, le bloquer
#Sinon essayer de cap 3 coins : victoire lol
