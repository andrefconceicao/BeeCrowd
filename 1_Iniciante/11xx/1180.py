n = int(input())
vetor = input().split()

contador = 0
while(contador < len(vetor)):
    vetor[contador] = int(vetor[contador])
    contador += 1
    
print("Menor valor:", min(vetor))
print("Posicao:", vetor.index(min(vetor)))