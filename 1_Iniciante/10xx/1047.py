horaInicial, minutoInicial, horaFinal, minutoFinal = input().split()

horaInicial = int(horaInicial)
minutoInicial = int(minutoInicial)
horaFinal = int(horaFinal)
minutoFinal = int(minutoFinal)
resultadoHora = 0
resultadoMinuto = 0

if(horaFinal < horaInicial):
    if(minutoFinal < minutoInicial):
        resultadoHora = 23 - horaInicial + horaFinal
        resultadoMinuto = 60 - minutoInicial + minutoFinal
    else:
        resultadoHora = 24 - horaInicial + horaFinal
        resultadoMinuto = minutoFinal - minutoFinal
elif(horaFinal == horaInicial):
    if(minutoFinal == minutoInicial):
        resultadoHora = 24
        resultadoMinuto = 0
    elif(minutoFinal < minutoInicial):
        resultadoHora = 23
        resultadoMinuto = 60 - minutoInicial + minutoFinal
    else:
        resultadoHora = 0
        resultadoMinuto = minutoFinal - minutoInicial
else:
    resultadoHora = horaFinal - horaInicial
    if(minutoFinal < minutoInicial):
        resultadoHora = horaFinal - horaInicial - 1
        resultadoMinuto = 60 - minutoInicial + minutoFinal
    else:
        resultadoMinuto = minutoFinal - minutoInicial
    
    
print("O JOGO DUROU", resultadoHora, "HORA(S) E", resultadoMinuto, "MINUTO(S)")