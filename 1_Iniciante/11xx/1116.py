contador = int(input())

while (contador > 0):
    x, y = input().split()
    x = float(x)
    y = float(y)
    
    if(y != 0):
        result = x/y
        print(result)
    else:
        print("divisao impossivel")
        
    contador -= 1