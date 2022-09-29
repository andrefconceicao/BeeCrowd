contador = 1
a = []
while(contador<=100):
    valor = float(input())
    if(valor <= 10):
        print("A[", contador-1, "] = ", valor, sep='')
    
    contador += 1