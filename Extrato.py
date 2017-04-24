# conta = input('Digite o número da conta (1-BB, 6-Ourocard, 0-Sair):')

arquivo = open('extrato.csv', 'r')

for key, linha in enumerate(arquivo):
    if (key > 0):
        campos = linha.split(",")
        data = campos[0][1:-1]
        ano = data[6:]
        mes = data[0:2]
        dia = data[3:5]
        descricao = campos[2][1:-1]
        valor = campos[5][1:-1]
        print(key, data, ano, mes, dia, descricao, valor)
