def novoGrenal(opcao):

    golsInter, golsGremio = input().split()
    golsGremio = int(golsGremio)
    golsInter = int(golsInter)
    
    if(golsInter > golsGremio):
        resultado = "i"
    elif(golsInter < golsGremio):
        resultado = "g"
    else:
        resultado = "e"
    
    opcao = int(input("Novo grenal (1-sim 2-nao)\n"))
    while(opcao != 1 and opcao != 2):
        opcao = int(input("Novo grenal (1-sim 2-nao)\n"))
        
    return opcao, resultado

opcao = 1
contador = 0
vitoriasGremio = 0
vitoriasInter = 0
empates = 0
while(opcao == 1):
    opcao, result = novoGrenal(opcao)
    contador += 1
    if(result == "g"):
        vitoriasGremio += 1
    elif(result == "i"):
        vitoriasInter += 1
    else:
        empates += 1
        
print(contador, "grenais")
print("Inter:", vitoriasInter, sep='')
print("Gremio:", vitoriasGremio, sep='')
print("Empates:", empates, sep='')
if(vitoriasGremio > vitoriasInter):
    print("Gremio venceu mais")
elif(vitoriasGremio < vitoriasInter):
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")