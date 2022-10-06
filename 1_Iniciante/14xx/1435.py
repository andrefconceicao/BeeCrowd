from tkinter import N


n = int(input())

matriz = []
linha = 0
coluna = 0
numDaVez = 1

while(linha < n):
    linhaV = [None]*n
    matriz.append(linhaV)
    linha += 1

linha = 0
while(linha < n):
    coluna = 0
    while(coluna < n):
        if(coluna == 0 or linha == 0 or coluna == n-1 or linha == n-1):
            matriz[linha][coluna] = 1
        else:
            matriz[linha][coluna] = 0
        coluna += 1
    linha += 1
    
linha = 0

""" ## Consertar
while(linha < n):
    coluna = 0
    while(coluna < n):
        if(coluna == 0 or linha == 0 or coluna == n-1 or linha == n-1):
            continue
        else:
            if(matriz[linha][coluna-1] == matriz[linha-1][coluna]):
                matriz[linha][coluna] = matriz[linha][coluna-1]+1
        coluna += 1
    linha += 1
"""
    
linha = 0
coluna = 0
while(linha < n):
    coluna = 0
    while(coluna < n):
        print(matriz[linha][coluna], end=' ')
        coluna += 1
    print("\n")
    linha += 1