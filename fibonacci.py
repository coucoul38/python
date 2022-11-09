


def fibo(iterations):
    n1, n2 = 0, 1
    for i in range(iterations):
        n3 = n2 + n1
        print(n1)
        n1 = n2
        n2 = n3
fibo(7)    
