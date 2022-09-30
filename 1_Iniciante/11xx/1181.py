l = int(input())
t = input()

coluna = 0
linha = 0

matriz = []

while(coluna < 3):
    linhaV = []
    linha = 0
    while(linha < 3):
        linhaV.append(float(input()))
        linha += 1

    matriz.append(linhaV)
    coluna += 1

contador = 0
soma = 0

while(contador < 3):
    soma += matriz[l][contador]
    contador += 1
if(t == 'S'):
    print("%.1f" % soma)
elif(t == 'M'):
    print("¨%.1f" % soma/12)
