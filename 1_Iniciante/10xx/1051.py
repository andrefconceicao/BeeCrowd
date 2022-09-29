salario = float(input())

imposto = 0.00
if (salario > 2000.00):
    if (salario <= 3000.00):
        imposto += 0.08*(salario-2000.00)
    else:
        imposto += 0.08*1000.00
        
    if (3000.00 < salario <= 4500.00):
        imposto += 0.18*(salario-3000.00)
    elif (salario > 4500.00):
        imposto += 0.18*1500.00
        imposto += 0.28*(salario-4500.00)
    
    print("R$ %.2f" % round(imposto, 2))
else:
    print("Isento")