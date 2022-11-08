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