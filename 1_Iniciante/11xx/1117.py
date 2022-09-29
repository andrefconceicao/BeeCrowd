media = 0.0
contador = 0

while(contador < 2):
    nota = float(input())
    
    if(nota < 0.0 or nota > 10.0):
        print("nota invalida")
    else:
        contador += 1
        media += nota
        
media /= 2

print("media =", media)