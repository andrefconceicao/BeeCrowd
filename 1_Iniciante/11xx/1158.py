n = int(input())

while(n > 0):
    x, y = input().split()
    x = int(x)
    y = int(y)
    soma = 0
    
    if(x%2 == 0):
        x += 1
    
    while(y>0):
        soma += x
        y -= 1
        x += 2
        
    print(soma)
    n -= 1