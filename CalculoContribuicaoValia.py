#coding: utf-8


def main():
    validaUR = True
    while validaUR:
        ur = input('Informe o valor da Unidade de Referencia (padrão=\
R$ 3756,58):')
        if ur == '':
            ur = 3756.58
        try:
            ur = float(ur)
            validaUR = True
        except(ValueError):
            print ('Valor Inválido, Tente Novamente!')
        else: #Esse else mantém o programa em loop
            validaUR = False
    validaSal = True
    while validaSal:
        salario = input('Informe o salário:')
        try:
            salario = float(salario)
            validaSal = True
        except(ValueError):
            print('Informe um valor válido!')
        else:
            validaSal = False
    validaContr = True
    while validaContr:
        percContrib = input('Informe o percentual de contribuição:')
        try:
            percContrib = float(percContrib)
            validaContr = True
        except(ValueError):
            print('Informe um valor válido!')
        else:
            validaContr = False

    print ('O valor a ser descontado é: R$ ', calculaContribuicao(ur, salario,
     percContrib))


def calculaContribuicao(ur, salario, percContrib):
    return round((ur * 0.01) + ((salario - ur) * (percContrib * 0.01)), 2)

if __name__ == "__main__":
    main()