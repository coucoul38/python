#v0.3.2
#on admet une fonction random() qui permet de choisir une option aléatoirement
#on admet une fonction input(key) qui permet de récupérer l'entrée d'un joueur

#le joueur entre le nombre de manches

#fontion end() : finit la partie (manche=nombreDeManches)

#foncion du jeu (play())
    #tant que manche <= nombreDeManches
        #le joueur entre son choix
            #1 = pierre
            #2 = feuille
            #3 = ciseaux

        #on choisis un résultat aléatoire entre 1,2,3: ce que va jouer le bot

        #si le joueur à joué pareil que le bot
            #dire qu'il y a eu égalité

        #sinon si le joueur à joué pierre
            #si le bot à joué ciseau, victoire du joueur
                #+1 point au joueur
            #se le bot à joué feuille, le joueur perds
                #+1 point au bot

        #sinon si le joueur à joué feuille
            #si le bot à joué ciseaux, victoire du bot
                #+1 point au bot
            #si le bot à joué pierre, victoire du joueur
                #+1 point au joueur

        #sinon si le joueur à joué ciseaux
            #si le bot à joué pierre, victoire du bot
                #+1 point au bot
            #si le bot à joué feuille, victoire du joueur
                #+1 point au joueur

        #manche = manche + 1
        #donner le score total
    
    #après toutes les manches, donner le gagnant