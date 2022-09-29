x = float(input())

n = []
n.append(x)

contador = 1
while(contador < 100):
    n.append(n[contador-1]/2)
    contador += 1
    
contador = 0
while(contador<len(n)):
    print("N[", contador, "] = %.4f" % n[contador], sep='')
    
    contador += 1