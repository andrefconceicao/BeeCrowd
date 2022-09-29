combustivel = int(input())

a = 0
g = 0
d = 0

while(combustivel !=4):
    if(combustivel == 1):
        a += 1
    elif(combustivel == 2):
        g += 1
    elif(combustivel == 3):
        d += 1
    combustivel = int(input())
    
print("MUITO OBRIGADO")
print("Alcool:", a)
print("Gasolina:", g)
print("Diesel:", d)