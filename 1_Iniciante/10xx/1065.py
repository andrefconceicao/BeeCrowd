contador = 0
pares = 0
while(contador < 5):
    valor = float(input())
    if (valor%2 == 0):
        pares += 1
    contador += 1
        
print(pares, "valores pares")