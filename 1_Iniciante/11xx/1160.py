from math import floor


t = int(input())

while(t > 0):
    pa, pb, ta, tb = input().split()

    pa = int(pa)
    pb = int(pb)

    ta = float(ta)
    tb = float(tb)
    
    anos = 0
    while(pa <= pb and anos <= 100):
        pa *= 1+(ta/100)
        pa = floor(pa)
        pb *= 1+(tb/100)
        pb = floor(pb)
        anos += 1
    if(anos > 100):
        print("Mais de 1 seculo.")
    else:
        print(anos, "anos.")
        
    t -= 1