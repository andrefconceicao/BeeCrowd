n = int(input())

inicio = 1
fib = 0
soma = 0

while(n > 0):
    if(n > 1):
        print(fib, end=' ')
    else:
        print(fib)
        
    soma = fib+inicio
    inicio = fib
    fib = soma
    
    n -= 1