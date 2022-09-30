def ehPar(valor):
    if(valor%2 == 0):
        return True
    else:
        return False

contadorEntrada = 1

par = []
impar = []

contadorPrint = 0

while(contadorEntrada <= 15):
    valor = int(input())
    
    if(ehPar(valor)):
        if(len(par) == 5):
            contadorPrint = 0
            while(contadorPrint<len(par)):
                print("par[", contadorPrint, "] = ", par[contadorPrint], sep='')
                contadorPrint += 1
            par = []
        par.append(valor)
    else:
        if(len(impar) == 5):
            contadorPrint = 0
            while(contadorPrint<len(impar)):
                print("impar[", contadorPrint, "] = ", impar[contadorPrint], sep='')
                contadorPrint += 1
            impar = []
        impar.append(valor)
        
    contadorEntrada += 1
    
contadorPrint = 0
while(contadorPrint<len(impar)):
    print("impar[", contadorPrint, "] = ", impar[contadorPrint], sep='')
    contadorPrint += 1
    
contadorPrint = 0
while(contadorPrint<len(par)):
    print("par[", contadorPrint, "] = ", par[contadorPrint], sep='')
    contadorPrint += 1