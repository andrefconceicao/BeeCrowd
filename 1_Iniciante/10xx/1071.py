inicio = int(input())
fim = int(input())
soma = 0

if (inicio > fim):
    aux = inicio
    inicio = fim
    fim = aux

contador = inicio+1
while(contador<fim):
    if(contador%2 == 1):
        soma += contador
    
    contador += 1
    
print(soma)