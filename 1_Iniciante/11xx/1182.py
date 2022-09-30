c = int(input())
t = input()
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
    soma += matriz[coluna][c]
    coluna += 1
    
if(t == 'S'):
    print("%.1f" % soma)
elif(t == 'M'):
    soma /= 12
    print("%.1f" % soma)