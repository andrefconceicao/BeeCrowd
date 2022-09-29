x, y = input().split()
x = int(x)
y = int(y)

contador = 1
contador2 = 1
while(contador <= y):
    while(contador2 <= x and contador <= y):
        if(contador2 < x and contador != y):
            print(contador, end=' ')
        else:
            print(contador)
        contador += 1
        contador2 += 1
    contador2 = 1     