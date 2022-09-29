n = int(input())

while(n>0):
    x = int(input())
    contador = 1
    soma = 0
    
    while(contador < x):
        if(x%contador == 0):
            soma += contador
        
        contador += 1
        
    if(soma == x):
        print(x, "eh perfeito")
    else:
        print(x, "nao eh perfeito")
        
    n -= 1