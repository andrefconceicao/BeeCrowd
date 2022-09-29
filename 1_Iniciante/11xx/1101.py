m = 1
n = 1
m, n = input().split()
m = int(m)
n = int(n)

while(m > 0 and n > 0):  
    if(n < m):
        aux = m
        m = n
        n = aux
    
    contador = m
    soma = 0
    
    while(contador <= n):
        print(contador, end=' ')
        soma += contador
        contador += 1
        
    print("Sum=", soma, sep='')
    m, n = input().split()
    m = int(m)
    n = int(n)