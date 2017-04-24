import Validador as val

opcoes = input('O que vc deseja?\n1.Seguir em frente\n2.Sair\n')

if opcoes == '2':
    exit()
elif (opcoes not in ('1','2')):
    print ('Tente novamente!')
else:
    nome = input('Informe seu nome:')

print('Parabéns {}! Você chegou longe...'.format(nome))
            

