#v0.4

#on admet une fonction random() qui permet de choisir une option aléatoirement
#on admet une fonction input() qui permet de récupérer l'entrée d'un joueur


#fontion end() : finit la partie (manche=nombreDeManches)

#foncion du jeu (play())
#on récupère le nombre de manche grace à input() et on l'assigne à nombreDeManches
    #tant que manche <= nombreDeManches
        #le joueur entre son choix grace à input() : variable choix
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