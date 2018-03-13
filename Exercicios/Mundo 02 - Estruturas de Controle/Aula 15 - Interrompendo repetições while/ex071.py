# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
# ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cd50 = cd20 = cd10 = cd1 = 0

print('=' * 50)
print(f'{"BANCO MRK":^50}')
print('=' * 50)

valor = int(input('Qual valor você quer sacar? R$'))

while True:
    if valor > 0:
        if valor % 50 == 0:
            cd50 += 1
            valor -= 50
        elif valor %20 == 0:
            cd20 += 1
            valor -= 20
        elif valor % 10 == 0:
            cd10 += 1
            valor -= 10
        else:
            cd1 += 1
            valor -= 1
    else:
        break

print('\nVocê receberá:')
print(f'{cd50} cédulas de R$50' if cd50 > 0 else '') # O 'else' é sempre necessário quando escrito em uma linha
print(f'{cd20} cédula(s) de R$20' if cd20 > 0 else '')
print(f'{cd10} cédula(s) de R$10' if cd10 > 0 else '')
print(f'{cd1} cédula(s) de R$1' if cd1 > 0 else '')
print('=' * 50)
print('Volte sempre ao BANCO MRK! Tenha um bom dia.')
