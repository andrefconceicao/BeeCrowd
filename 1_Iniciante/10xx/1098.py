i = 0.0
j = 1.0

while(i<=2):
    fim = j + 2
    
    while(j<=fim):
        if(round((i/0.2)%5, 2) == 0):
            if(round((j/0.2)%5, 2) == 0):
                print("I=%.0f" %i, "J=%.0f" % j)
            else:
                print("I=%.0f" %i, "J=%.1f" % j)
        else:
            print("I=%.1f" %i, "J=%.1f" % j)
        j += 1
    
    i += 0.2
    i = round(i, 1)
    j = 1+i