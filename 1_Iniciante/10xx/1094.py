n = int(input())

contador = 1

somaqt = 0
somaC = 0
somaR = 0
somaS = 0

while(contador <= n):
    quantia, tipo = input().split()
    
    quantia = int(quantia)
    
    somaqt += quantia
    if(tipo == 'C'):
        somaC += quantia
    if(tipo == 'R'):
        somaR += quantia
    if(tipo == 'S'):
        somaS += quantia
    
    contador += 1
    
print("Total:", somaqt, "cobaias")
print("Total de coelhos:", somaC)
print("Total de ratos:", somaR)
print("Total de sapos:", somaS)
print("Percentual de coelhos: %.2f" % round(somaC*100/somaqt, 2), " %", sep='')
print("Percentual de ratos: %.2f" % round(somaR*100/somaqt, 2), " %", sep='')
print("Percentual de sapos: %.2f" % round(somaS*100/somaqt, 2), " %", sep='')