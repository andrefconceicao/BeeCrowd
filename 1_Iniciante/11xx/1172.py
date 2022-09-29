contador = 1
xv = []

while(contador<=10):
    x = int(input())
    xv.append(x)
    contador += 1
    
contador = 0
while(contador < 10):
    if(xv[contador] <= 0):
        xv[contador] = 1
    
    contador += 1
        
contador = 0
while(contador < 10):
    print("X[%i] =" % contador, xv[contador])
    contador += 1