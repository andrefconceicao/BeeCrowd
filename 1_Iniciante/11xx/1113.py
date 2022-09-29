m, n = input().split()
m = int(m)
n = int(n)

while(m != n):
    if(m < n):
        print("Crescente")
    else:
        print("Decrescente")
    
    m, n = input().split()
    m = int(m)
    n = int(n)