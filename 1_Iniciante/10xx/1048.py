salario = float(input())

if(salario >= 0 and salario <= 400.00):
    percentual = 15
elif(salario >= 400.00 and salario <= 800.00):
    percentual = 12
elif(salario >= 800.00 and salario <= 1200.00):
    percentual = 10
elif(salario >= 1200.00 and salario <= 2000.00):
    percentual = 7
elif(salario > 2000.00):
    percentual = 4
    
novoSalario = salario*(1 + percentual/100)
    
print("Novo salario:", "%.2f" % round(novoSalario, 3))
print("Reajuste ganho:", "%.2f" % round(novoSalario - salario, 3))
print("Em percentual:", percentual, "%")
