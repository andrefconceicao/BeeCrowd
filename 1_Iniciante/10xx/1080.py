contador = 1
numeros = []

while(contador <= 100):
    n = int(input())
    numeros.append(n)
    
    contador += 1

print(max(numeros))
print(numeros.index(max(numeros)) + 1)