import math

def iniciaMatriz(n):
    i = 0
    matriz = []

    while(i<n):
        
        j=0
        linha = []
        
        while(j<n):
            
            linha.append(0)
            
            j += 1
        
        matriz.append(linha)
        
        i += 1
        
    return matriz

def imprimeMatriz(matriz):
    i = 0
    while(i<n):
        j = 0
        while(j<n):
            print(" ", matriz[i][j], end = '')
            j+=1
        
        print('\n')
        i+=1
    
    ##print("\n")

def fazMatriz(matriz, nivel):
    i = nivel

    while(i<len(matriz)-nivel):
        
        j=nivel
        linha = []
        
        while(j<len(matriz)-nivel):
            
            if((i == nivel) or (j == nivel) or (i == len(matriz)-nivel-1) or (j == n-nivel-1)):
                matriz[i][j] = nivel+1
                
            j += 1
        
        i += 1
        
    if(nivel <= int(math.ceil(len(matriz)/2))):
        fazMatriz(matriz, nivel+1)

n = int(input())

while(n!=0):
    
    matriz = iniciaMatriz(n)
    
    fazMatriz(matriz, 0)
    
    imprimeMatriz(matriz)
    
    n = int(input())