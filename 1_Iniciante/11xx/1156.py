contador = 3
s = 1
expoente = 1

while(contador <= 39):
    adicionar = contador / (2**expoente)

    s += adicionar
    
    contador += 2
    expoente += 1
    
print("%.2f" % round(s, 2))