nulo, diaInicial = input().split()
horaInicial, minutoInicial, segundoInicial = input().split(" : ")
nulo, diaFinal = input().split()
horaFinal, minutoFinal, segundoFinal = input().split(" : ")

diaInicial = int(diaInicial)
diaFinal = int(diaFinal)
minutoFinal = int(minutoFinal)
minutoInicial = int(minutoInicial)
horaInicial = int(horaInicial)
horaFinal = int(horaFinal)
segundoInicial = int(segundoInicial)
segundoFinal = int(segundoFinal)

resultadoHora = 0
resultadoMinuto = 0
resultadoSegundo = 0
resultadoDia = 0

resultadoDia = diaFinal - diaInicial

if(horaFinal < horaInicial or (horaFinal == horaInicial and minutoInicial > minutoFinal)):
    resultadoDia -= 1
    resultadoHora = 24 - horaInicial + horaFinal
else:
    resultadoHora = horaFinal - horaInicial
    
if(minutoFinal < minutoInicial):
    resultadoHora -= 1
    resultadoMinuto = 60 - minutoInicial + minutoFinal
else:
    resultadoMinuto = minutoFinal - minutoInicial
    
if(segundoFinal < segundoInicial):
    resultadoMinuto -= 1
    resultadoSegundo = 60 - segundoInicial + segundoFinal
else:
    resultadoSegundo = segundoFinal - segundoInicial
    
if(resultadoHora == -1):
    resultadoHora = 23
if(resultadoMinuto == -1):
    resultadoMinuto = 59
    
print(resultadoDia, "dia(s)")
print(resultadoHora, "hora(s)")
print(resultadoMinuto, "minuto(s)")
print(resultadoSegundo, "segundo(s)")