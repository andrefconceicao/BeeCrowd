n = int(input())

contador = 0

while(contador < n):
    valor = int(input())
    
    if(valor == 0):
        print("NULL")
    elif(valor%2 == 0):
        if(valor>0):
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        if(valor>0):
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
    
    contador += 1