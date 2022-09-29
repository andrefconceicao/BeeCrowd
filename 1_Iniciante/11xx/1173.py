n = []
contador = 0

n.append(int(input()))
print("N[", contador, "] = ", n[contador], sep='')

contador = 1
while(contador<10):
    n.append(n[contador-1]*2)
    print("N[", contador, "] = ", n[contador], sep='')
    
    contador += 1