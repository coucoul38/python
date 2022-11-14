#v0.4

#on admet une fonction random() qui permet de choisir une option aléatoirement
#on admet une fonction input() qui permet de récupérer l'entrée d'un joueur

#DEBUT
    #fontion end() : finit la partie (nombreDeManches=manche)

    #on crée la fonction play(nombreDeManches)
        #manche = 0
        #tant que manche <= nombreDeManches
            #le joueur entre son choix grace à input() : on assigne le retour à la variable choix
                #si choix = p
                    #alors choixNb = 1
                #si choix = f
                    #alors choixNb = 2
                #si choix = c
                    #alors choixNb = 3

            #on génère un résultat aléatoire entre 1,2,3 avec la fonction random() et on l'assigne à choixBot

            #si choixNb = choixBot
                #alors dire qu'il y a eu égalité

            #sinon si choixNb = 1
                #alors si choixBot = 2
                    #dire que le joueur à perdu
                    #ajouter 1 au score du bot
                #alors si choixBot = 3
                    #dire que le joueur à gagné
                    #ajouter 1 au score du joueur

            #sinon si choixNb = 2
                #alors si choixBot = 1
                    #dire que le joueur à gangé
                    #ajouter 1 au score du joueur
                #alors si choixBot = 3
                    #dire que le joueur à perdu
                    #ajouter 1 au score du bot

            #sinon si choixNb = 3
                #alors si choixBot = 1
                    #dire que le joueur à perdu
                    #ajouter 1 au score du bot
                #alors si choixBot = 2
                    #dire que le joueur à gagné
                    #ajouter 1 au score du joueur

            #ajouter 1 à manche
            #donner le score total

        #après toutes les manches, donner le gagnant


    #executer la fonction play()
#FIN

import random

def pfc(rounds):
    global playerChoice
    manche=0
    botScore=0
    playerScore=0

    while manche<rounds:
        askPLayer=input("Faites votre choix : p,f,c : ")
        print("",end="\n")
        botChoice = random.randint(1,3)
        if(askPLayer=="p"):
            playerChoice=1
        elif(askPLayer=="f"):
            playerChoice=2
        elif(askPLayer=="c"):
            playerChoice=3
        else:
            print("Erreur")

        if playerChoice==botChoice:
            print("Egalité")
        elif playerChoice==1:
            if botChoice ==2:
                print("Le bot joue feuille: Perdu!")
                botScore = botScore + 1
            elif botChoice == 3:
                print("Le bot joue ciseaux: Gagné!")
                playerScore=playerScore+1
        elif playerChoice==2:
            if botChoice==1:
                print("Le bot joue pierre: Gagné!")
                playerScore=playerScore+1
            elif botChoice==3:
                print("Le bot joue ciseaux: Perdu!")
                botScore=botScore+1
        elif playerChoice==3:
            if botChoice==1:
                print("Le bot joue pierre: Perdu!")
                botScore=botScore+1
            elif botChoice==2:
                print("Le bot joue feuille: Gagné!")
                playerScore=playerScore+1
        
        print("",end="\n")
        print("Score du joueur : ", playerScore)
        print("Score du bot : ", botScore)
        print("",end="\n")
        manche=manche+1

    if playerScore==botScore:
        print("Résultat de la partie : Egalité")
    elif playerScore>botScore:
        print("Résultat de la partie : Victoire du Joueur")
    else :
        print("Résultat de la partie : Victoire du Bot")
    

pfc(10)