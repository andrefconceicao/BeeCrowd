def calculaMedia(opcao):

    media = 0.0
    contador = 0

    while(contador < 2):
        nota = float(input())
        
        if(nota < 0.0 or nota > 10.0):
            print("nota invalida")
        else:
            contador += 1
            media += nota
            
    media /= 2

    print("media = %.2f" % round(media, 2))
    
    opcao = int(input("novo calculo (1-sim 2-nao)\n"))
    while(opcao != 1 and opcao != 2):
        opcao = int(input("novo calculo (1-sim 2-nao)\n"))
        
    return opcao

opcao = 1        
while(opcao == 1):
    opcao = calculaMedia(opcao)