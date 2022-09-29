n = int(input())

while(n != 0):
    soma = 0
    
    if(n%2 == 1):
        n += 1
    
    contador = 1
    while(contador <= 5):
        soma += n
        n += 2
        contador += 1
        
    print(soma)
    n = int(input())