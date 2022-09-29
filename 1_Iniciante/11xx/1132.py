x = int(input())
y = int(input())

if(x>y):
    aux = x
    x = y
    y = aux

soma = 0
while(x <= y):
    if(x%13 != 0):
        soma += x
    x += 1
    
print(soma)