def ehPrimo(x):
    contador = 2
    soma = 0
    
    while(contador < x):
        if(x%contador == 0):
            soma = 1
            return False
        
        contador += 1
        
    return True

n = int(input())

while(n>0):
    x = int(input())
    if(ehPrimo(x)):
        print(x, "eh primo")
    else:
        print(x, "nao eh primo")
        
    n -= 1