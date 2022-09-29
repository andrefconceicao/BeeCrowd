n = int(input())
dentro = 0
fora = 0

while(n>0):
    valor = int(input())
    if(10 <= valor <= 20):
        dentro += 1
    else:
        fora += 1
    
    n -= 1
        
print(dentro, "in")
print(fora, "out")