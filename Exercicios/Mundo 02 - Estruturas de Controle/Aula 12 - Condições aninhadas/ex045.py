# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('''Escolha uma opção: 
1 - Pedra
2 - Papel
3 - Tesoura''')
jogador = int(input('Opção: '))

lista = ['Inválido', 'PEDRA', 'PAPEL', 'TESOURA']

comp = randint(1,3)

if 0 < jogador < 4:
    print('Você escolheu: {}'.format(lista[jogador]))
    print('O computador escolheu...')
    sleep(1)
    print('{}\n'.format(lista[comp]))
    print('RESULTADO: ')
    if jogador == comp:
        print('Empate!')
    elif (jogador == 1 and comp == 2) or (jogador == 2 and comp == 3) or (jogador == 3 and comp == 1):
        print('O computador venceu!')
    # elif (jogador == 1 and comp == 3) or (jogador == 2 and comp == 1) or (jogador == 3 and comp == 2):
    else:
        print('Você venceu!')
else:
    print('Opção inválida!')
