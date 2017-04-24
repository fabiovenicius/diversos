arquivo_entrada = open(r'C:\Users\M050183\Documents\GitHub\Bacas\BalanceteCADAMMar-2017.txt', 'r')
arquivo_saida = open(r'C:\Users\M050183\Documents\GitHub\Bacas\BalanceteCADAMMar-2017-Fabio.txt', 'w')
primeira_coluna = '100'
continuacao = '-- (continued)'
relat=''
conta=''
valor=''
descricao=''
for linha in arquivo_entrada:
    if linha[0:3] == primeira_coluna and linha[117:131] != continuacao:
        conta = linha[8:13]
        descricao = linha[53:116]
        relat = conta + ' ' + descricao +'\n'
        arquivo_saida.write(relat)
        relat=''
        descricao=''
        conta = ''
        valor = ''
arquivo_entrada.close()
arquivo_saida.close()
