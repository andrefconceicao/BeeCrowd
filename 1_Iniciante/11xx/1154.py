n = 0
soma = 0
contador = 0
while(n >= 0):
    n = int(input())
    if(n>=0):
        soma += n
        contador += 1

soma /= contador

print("%.2f" % round(soma,2))