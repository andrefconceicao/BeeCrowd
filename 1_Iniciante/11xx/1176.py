t = int(input())

contador = 1
while(contador <= t):
    valor = int(input())
    contador2 = 1
    
    inicio = 1
    fib = 0
    soma = 0
    
    while(contador2 <= valor):
        
        soma = fib+inicio
        inicio = fib
        fib = soma
        
        contador2 += 1
    
    print("Fib(", valor, ") = ", soma, sep='')    
    contador += 1