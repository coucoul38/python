def add(x, y):
    return(x+y)

def sub(x,y):
    return(x-y)

def multiply(x, y):
    return(x*y)

def divide(x,y):
    return(x/y)

def modulo(x,y):
    return(x%y)


def calcSalaireSec(salaireH, heureJourOuvrable, JOparAn):
    salaireAnnuel = (salaireH*heureJourOuvrable*JOparAn)       #Salaire annuel/secondes en 1 an
    nbSecondesParAn = (365 * 24 * 60 * 60)
    return(salaireAnnuel / nbSecondesParAn)
    

def calcNet(salaireBrut, fonctionPublique):
    if fonctionPublique == True :
        return(salaireBrut-(0.15*salaireBrut))
    else :
        return(salaireBrut-(0.23*salaireBrut))