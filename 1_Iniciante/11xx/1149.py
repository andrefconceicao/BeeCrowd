valores = input().split()
a = valores[0]
n = valores[-1]
a = int(a)
n = int(n)
    
i = 0
soma = 0
while(i < n):
    soma += (a+i)
    
    i -= 1
    
print(soma)