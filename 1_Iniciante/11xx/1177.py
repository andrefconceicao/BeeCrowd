t = int(input())

n = []
contador = 0
aux = 0
while(contador < 1000):
    if(aux>=t):
        aux = 0
    
    n.append(aux)
    print("N[", contador, "] = ", aux, sep='')
    contador += 1
    aux += 1 