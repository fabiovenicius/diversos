valor_imovel = input("Valor do Imóvel:")
valor_entrada = input("Valor da Entrada (padrão 30%):")
if not valor_entrada:
    valor_entrada = valor_imovel * 0.3
print(valor_entrada)