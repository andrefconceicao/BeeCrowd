contador = 1
s = 0

while(contador <= 100):
    s += (1/contador)
    
    contador += 1
    
print("%.2f" % round(s, 2))