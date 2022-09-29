n = int(input())

contador = 1

while(contador <= n):
    soma = 0
    x, y = input().split()
    x = int(x)
    y = int(y)
    
    if(y < x):
        aux = x
        x = y
        y = aux
        
    aux = x+1
    
    while(aux < y):
        if(aux%2 == 1):
            soma += aux
        
        aux += 1
    
    print(soma)
    contador += 1