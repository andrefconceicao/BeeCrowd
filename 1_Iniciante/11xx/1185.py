o = input()
matriz = []

linha = 0
coluna = 0

while(linha < 12):
    linhaV = []
    while(coluna < 12):
        valor = float(input())
        linhaV.append(valor)
        coluna += 1
    coluna = 0
    matriz.append(linhaV)
    linha += 1

linha = 0
coluna = 0
soma = 0
qtd = 0

while(linha < 12):
    while(coluna < 12):
        if(linha+coluna <= 10):
            soma += matriz[linha][coluna]
            qtd += 1
        coluna += 1
    linha += 1
    coluna = 0
    
if(o == 'S'):
    print("%.1f" % soma)
elif(o == 'M'):
    soma /= qtd
    print("%.1f" % soma)