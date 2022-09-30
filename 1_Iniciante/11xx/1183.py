o = input()
matriz = []

coluna = 0
linha = 0

while(coluna < 12):
    linhaV = []
    while(linha < 12):
        valor = float(input())
        linhaV.append(valor)
        linha += 1
    linha = 0
    matriz.append(linhaV)
    coluna += 1

coluna = 0
linha = 0
soma = 0

while(coluna<12):
    while(linha<12):
        if(coluna < linha):
            soma += matriz[coluna][linha]
        linha += 1
    coluna += 1
    linha = 0
    
if(o == 'S'):
    print("%.1f" % soma)
elif(o == 'M'):
    soma /= 12
    print("%.1f" % soma)