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

prenom = "Joe"
nom = "M"

nomPrenom = nom + prenom #renvoie DJoe
nomPrenom2 = nom + " " + prenom #renvoie D Joe
intValue = 342
strIntValue = str(342) #renvoie 342 sous forme de string

tableauMultiType = ["Joe", True, tableau, 4 > 2, None]
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
    # initialisation de la variable qui sera retournée
    before = ""
    # éxecute pour chaquye élément de la liste
    for i in range (len(table)-1):
        # si l'élément i de la table table est le nombre que l'on cherche :
        if(table[i]==number):
            #pour eviter de concaténer avec une chaine de chara vide
            if(before == ""): #ou alors si i==1 
                before=i
            else :
                # on concaténe l'index du nombre voulu dans before
                before = concat(before,i)
    return before

print(find(amog, 2))

#Exercice 3
# faire une fonction Afficher un message
# tel que
def afficher(msg):
    print(msg)


#Exercice 4
#Fonction login(username, password, listUser) pour afficher un message de connexion si le combo est bon
listeUtilisateur = {
    "Joe" :"motdepasse",
    "Michel" : "amogus",
    "Toto" : "1234"
}

def login(user,password, list):
    #si le mdp donné est égal au mdp qui correspond à la clé User dans la liste List, alors bon login
    if(password==list[user]):
        print("Yay")
    #sinon, l'utilisateur s'est trompé sur le mdp ou l'Username
    else :
        print("Mauvais mdp ou login")

login("Toto", "1234",listeUtilisateur)

#correction ex 2
def find(table, number):
    # initialisation de la variable qui sera retournée
    i=0
    #def
    chaineResultat = ""
    while i<len(tableau):
        if tableau[i]==number:
            firstTurn = True
            if firstTurn: 
                chaineResultat = str(i)
                firstTurn=False
            chaineResultat = concat(chaineResultat, str(i))
        i=i+1
