n = int(input())

contador = 1

while(contador <= n):
    if(contador%2 == 0):
        print(contador, "^2", " = ", contador*contador, sep='')
        
    contador += 1