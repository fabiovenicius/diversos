def isfloat(valor):
    try:
        resultado = float(valor)
        return True
    except(ValueError):
        print('Valor informado {} não é um valor numérico válido'.format(valor))
        return False
        

def isint(valor):
    try:
        resultado = int(valor)
        return True
    except(ValueError):
        print('Valor informado {} não é um valor numérico válido'.format(valor))
        return False
        
def ischar(valor):
    try:
        resultado = str(valor)
        return True
    except(ValueError):
        print('Valor informado {} não é uma palavra válida'.format(valor))
        return False

def escolha(opcao,alternativas):
    if opcao in alternativas:
        return True
    else:
        print('Valor informado {} não faz parte das alternativas válidas!'.format(opcao))
        return False