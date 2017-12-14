# coding: utf-8

import os


def main():
    arquivo = open(os.path.expanduser(
        'amortizacao.txt'), 'w')
    valida = True
    while valida:
        try:
            valorEmprestimo = float(input('Informe o valor do Emprestimo:'))
        except(ValueError):
            print ('Valor deve ser numérico! Tente novamente!')
        else:
            valida = False
    valida = True
    while valida:
        try:
            valorJuros = float(input('Informe o valor dos juros:'))
        except(ValueError):
            print ('Valor deve ser numérico! Tente novamente!')
        else:
            valida = False
    valida = True
    while valida:
        try:
            qtdParcelas = int(input('Informe quantidade de parcelas:'))
        except(ValueError):
            print ('Valor deve ser numérico! Tente novamente!')
        else:
            valida = False
    valorJurosAbsoluto = valorJuros/100
    qtdLinhas = qtdParcelas + 1
    arquivo.write('Sistema PRICE \n')
    arquivo.write('Valor do Empréstimo: R$' + str(round(valorEmprestimo, 2)) +
                  '\n')
    arquivo.write('Valor dos juros:' + str(valorJuros)+'%\n')
    arquivo.write('Quantidade de Parcelas:' + str(qtdParcelas) + '\n')
    coeficiente = (valorJurosAbsoluto) / (1 - 1 / (1 + valorJurosAbsoluto) **
                                          qtdParcelas)
    arquivo.write('Valor do coeficiente:' + str(round(coeficiente, 4)) + '\n')
    valorParcela = valorEmprestimo*coeficiente
    arquivo.write('Valor da Parcela:' + str(round(valorParcela, 2)) + '\n')
    amortizacao = 0
    juros = 0
    prestacao = 0
    saldoDevedor = round(valorEmprestimo, 2)
    arquivo.write('{}\t{}\t{}\t{}\t{}\n'.format('Linha', 'Sld Devedor',
                  'Prestacao', 'Juros', 'Amort'))
    for linha in range(qtdLinhas):
        arquivo.write('{}\t{}\t{}\t{}\t{}\n'.format(str(linha),
                                                    str(saldoDevedor),
                                                    str(prestacao),
                                                    str(juros),
                                                    str(amortizacao)))
        prestacao = round(valorParcela, 2)
        juros = round(saldoDevedor * valorJurosAbsoluto, 2)
        amortizacao = round(prestacao - juros, 2)
        saldoDevedor = round(saldoDevedor - amortizacao, 2)
    arquivo.write('Sistema SAC \n')
    arquivo.write('Valor do Empréstimo: R$' + str(round(valorEmprestimo, 2)) +
                  '\n')
    arquivo.write('Valor dos juros:' + str(valorJuros) + '%\n')
    arquivo.write('Quantidade de Parcelas:' + str(qtdParcelas)+'\n')
    amortizacao = 0
    juros = 0
    prestacao = 0
    saldoDevedor = round(valorEmprestimo, 2)
    arquivo.write('Linha\tSld Devedor\tAmort\tJuros\tPrestacao\n')
    for linha in range(qtdLinhas):
        arquivo.write(str(linha) + '\t' + str(saldoDevedor) +
                      '\t' + str(amortizacao) +
                      '\t' + str(juros) + '\t' +
                      str(prestacao)+'\n')
        juros = round(saldoDevedor * valorJurosAbsoluto, 2)
        amortizacao = round(valorEmprestimo / qtdParcelas, 2)
        prestacao = round(amortizacao + juros, 2)
        saldoDevedor = round(saldoDevedor - amortizacao, 2)
    arquivo.close
    print('Verificar o resultado em \fabiovenicius\GitHub\diversos\
    amortizacao.txt')

if __name__ == "__main__":
    main()
