contador = 1

n = []
while(contador <= 20):
    n.append(int(input()))
    
    contador += 1
    
contador = 0
contadorReverso = 19
aux = 0
while(contador <= 9 and contadorReverso >= 10):
    aux = n[contador]
    n[contador] = n[contadorReverso]
    n[contadorReverso] = aux
    
    contador += 1
    contadorReverso -= 1
    
contador = 0
while(contador<=len(n)-1):
    print("N[", contador, "] = ", n[contador], sep='')
    contador += 1