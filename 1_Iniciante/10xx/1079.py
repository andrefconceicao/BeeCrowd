n = int(input())

contador = 1

while(contador <= n):
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    
    print("%.1f" % round((a*2 + b*3 + c*5)/10, 1))
    contador += 1