contador = 0
positivos = 0
media = 0
while(contador < 6):
    valor = float(input())
    if (valor > 0):
        positivos += 1
        media += valor
    contador += 1

media /= positivos
        
print(positivos, "valores positivos")
print("%.1f" % round(media, 1))