#v0.1
#on admet une fonction random() qui permet de choisir une option aléatoirement
#on admet une fonction input(key) qui permet de récupérer l'entrée d'un joueur

#le joueur entre le nombre de manches
#pour chaque manche
    #le joueur entre son choix (p,f,s)
        #0 = pierre
        #1 = feuille
        #2 = ciseaux
        
        #on choisi un résultat aléatoir entre p,f,c: ce que va jouer le bot

        #si le joueur à joué pierre
            #si le bot à joué ciseau, victoire du joueur
                #+1 point au joueur
            #se le bot à joué feuille, le joueur perds
                #+1 point au bot
            #sinon égalité

        #si le joueur à joué feuille
            #si le bot à joué ciseaux, victoire du bot
                #+1 point au bot
            #si le bot à joué pierre, victoire du joueur
                #+1 point au joueur
            #sinon égalité

        #si le joueur à joué ciseaux
            #si le bot à joué pierre, victoire du bot
                #+1 point au bot
            #si le bot à joué feuille, victoire du joueur
                #+1 point au joueur
            #sinon égalité

