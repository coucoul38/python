


def fibo(iterations):
    #on initialise les 1ers chiffres
    n1, n2 = 0, 1
    #on execute le nombre de fois demandé
    for i in range(iterations):
        n3 = n2 + n1
        print(n1)
        n1 = n2
        n2 = n3

fibo(69)    
