x = 1
while(x!=0):
    x = int(input())
    
    contador = 1
    while(contador <= x):
        if(contador < x):
            print(contador, end=' ')
        else:
            print(contador)
        contador += 1