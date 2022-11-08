def add(x, y):
    return(x+y)

def sub(x,y):
    return(x-y)

def multiply(x, y):
    return(x*y)

def divide(x,y):
    # empecher la division par 0
    if(y == 0):
        return("Y ne peux pas être égal à 0")
    return(x/y)  # éxécuté seulement si y n'est pas 0

def modulo(x,y):
    return(x%y)


def calcSalaireSec(salaireH, heureJourOuvrable, JOparAn):
    salaireAnnuel = (salaireH*heureJourOuvrable*JOparAn)       
    nbSecondesParAn = (365 * 24 * 60 * 60)
    return(salaireAnnuel / nbSecondesParAn)
    

def calcNet(salaireBrut, fonctionPublique):
    if fonctionPublique :
        return(salaireBrut-(0.15*salaireBrut)) # 15% de taxes pour le public
    # Si pas dans la fonction publique, alors taxes privé
    else :
        return(salaireBrut-(0.23*salaireBrut))  # 23% de taxes pour le reste



import random
import string

#la lettre à trouver (minuscule)
chara = 'o' 

def input():
        #renvoie une lettre minuscule de type string au hasard
        letter=(random.choice(string.ascii_lowercase)) 
        print(letter)
        if letter == chara :
            return("C'est la bonne lettre !")
    
#CORRECTION
def miniGame(winCondition):
    #création variable char
    chara = input()
    tries = 1
    while(chara!= winCondition):
        chara = input()
        tries = tries + 1
    print(tries)
    
    
tableau = [0, 10, 15, 5, 14, 7, 102]
#pour récupérer 15 dans le tableau je prends l'index 2 - 1 (penser à l'index 0)
#print(tableau[2])
len(tableau) #nombre éléments du tableau

prenom = "Alexandre"
nom = "Delaistre"

nomPrenom = nom + prenom #renvoie DelaistreAlexandre
nomPrenom2 = nom + " " + prenom #renvoie Delaistre Alexandre
intValue = 342
strIntValue = str(342) #renvoie 342 sous forme de string

tableauMultiType = ["Alexandre", True, tableau, 4 > 2, None]
tableauDim = [0,1,2,3]
tableauDim2 = [0,1,21,3]
tableauMultiDim = [tableauDim, tableauDim2]
tableauMultiDim[1][2] #renvoie 21

tableauCleVal = {"clé" : "valeur", "clé2" : "valeur2"}
tableauCleVal["clé"] #renvoie valeur



# Exercice 1:
# Fonction qui concaténe 2 chaines de caractéres en les séparant avec une virgule
chaine1 = "VSauce, Michael here"
chaine2 = "do chairs really exist ?"
def concat(para1, para2):
    # ajoute une virgule entre les 2 chaines
    return(str(para1) + ", " + str(para2))

#Exercice 2 : 
#Faire une fonction qui itére sur tous les indexs du tableau renvoyant une chaine de charactères
#avec l'ensemble des occurations d'un chiffre :
# POur tableau [0,1,1,1,0,1,1,0,1]
# la fonction (tableau, 0) doit renvoyer "0, 4, 7" n'hésitez pas a implementer la 1ere fonction


amog = [1,2,1,2,2,2,1,4,2,4,4,2,1]

def find(table, number):
    before = ""
    for i in range (len(table)-1):
        if(table[i]==number):
            if(before == ""):
                before=i
            else :
                before = concat(before,i)
    return before


print(find(amog, 2))

#Exercice 3
# faire une fonction Afficher un message
#tel que
listeUtilisateur = {
    "Alexandre" :"motdepasse",
    "Michel" : "amogus",
    "Toto" : "1234"
}


#Exercice 4
#Fonction login(usernam, password, listUser) pour afficher un message de connexion si le combo est bon