a, b = input().split()

a = int(a)
b = int(b)

if(b<a):
    print("O JOGO DUROU", 24-a+b, "HORA(S)")
elif(b-a == 0):
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU", b-a, "HORA(S)")