# Crie um programa que leia dois valores e mostre um menu na tela:
# - 1: SOMAR
# - 2: MULTIPLICAR
# - 3: MAIOR
# - 4: NOVOS NÚMEROS
# - 5: SAIR DO PROGRAMA
#   Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

opt = 0

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while opt != 5:

    print('''Selecione uma opção:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opt = int(input('Opção: '))

    if opt == 1:
        print('A soma dos números {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    elif opt == 2:
        print('A multiplicação dos números {} e {} é igual a {}'.format(n1, n2, n1 * n2))
    elif opt == 3:
        print('O número {} é maior.'.format(n1 if n1 > n2 else n2))
    elif opt == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opt == 5:
        print('O programa será encerrado...')
        sleep(1)
    else:
        print('Opção inválida.')

print('O programa foi finalizado.')
