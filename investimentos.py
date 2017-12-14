# coding: utf-8


def main():
    saldo_inicial = float(input('Informe o Valor a ser alocado:'))
    saldo_atual = saldo_inicial
    relatorio = open('relatorio.txt', 'w')
    opcao = True
    alocacao = ''
    while opcao:
        alocacao = raw_input('Informe nome da alocação: \n')
        if alocacao == 'fim':
            break
        valor = float(input('Informe o valor a ser alocado'))
        saldo_temp = saldo_atual
        if (saldo_temp < 0):
            print('Fim dos Recursos! Diminua o valor a ser alocado!')
        else:
            saldo_atual = saldo_atual - valor
            print('Nome do Titulo:', alocacao)
            relatorio.write('Nome do Título:' + alocacao + '\n')
            print('Valor alocado:', valor)
            relatorio.write('Valor alocado:' + str(valor) + '\n')
            print('Saldo atualizado:', saldo_atual)
            relatorio.write('Saldo Atualizado:' + str(saldo_atual) + '\n')
    relatorio.close()

if __name__ == "__main__":
    main()
