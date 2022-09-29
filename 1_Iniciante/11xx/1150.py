x = int(input())
z = int(input())
while(z<=x):
    z = int(input())

contador = 0
soma = 0
while(soma <= z):
    soma += x
    contador+=1
    x += 1
    
print(contador)