inss = 0.03
fgts = 0.08
salario = float(input("Digite salário:"))
print("Salário bruto:{}".format(salario))
print("Valor INSS:{}".format(salario * inss))
print("Valor FGTS retido:{}".format(salario * fgts))
print("Salário liquido:{}".format(salario * (1 - fgts)))
