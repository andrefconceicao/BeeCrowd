contador = 0
positivos = 0
while(contador < 6):
    valor = float(input())
    if (valor > 0):
        positivos += 1
    contador += 1
        
print(positivos, "valores positivos")