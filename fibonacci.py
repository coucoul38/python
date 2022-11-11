#n2 = second number
def fibo(iterations, n2):
    #on initialise les 1ers chiffres
    n1= 0
    #on execute le nombre de fois demandé
    for i in range(iterations):
        n3 = n2 + n1
        print(n1)
        n1 = n2
        n2 = n3

fibo(69,3)