a, b, c = input().split()

valores = []
a = float(a)
b = float(b)
c = float(c)

valores.append(a)
valores.append(b)
valores.append(c)

valores.sort(reverse=True)

a = valores[0]
b = valores[1]
c = valores[2]

if(a >= (b+c)):
    print("NAO FORMA TRIANGULO")
else:
    if(a*a == (b*b+c*c)):
        print("TRIANGULO RETANGULO")
    if(a*a > (b*b+c*c)):
        print("TRIANGULO OBTUSANGULO")
    if(a*a < (b*b+c*c)):
        print("TRIANGULO ACUTANGULO")
    if(a == b and b == c):
        print("TRIANGULO EQUILATERO")
    if((a == b and b != c) or (a == c and b != c) or (b == c and a!= b)):
        print("TRIANGULO ISOSCELES")