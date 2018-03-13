# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
# ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 50)
print(f'{"BANCO MRK":^50}')
print('=' * 50)

valor = int(input('Qual valor você quer sacar? R$'))

cd = 50
tot_cd = 0

while True:
    if valor >= cd:
        tot_cd += 1
        valor -= cd
    else:
        if tot_cd > 0:
            print(f'Total de {tot_cd} cédula(s) de R${cd}')
        if cd == 50:
            cd = 20
        elif cd == 20:
            cd = 10
        elif cd == 10:
            cd = 1
        tot_cd = 0
        if valor == 0:
            break

print('=' * 50)
print('Volte sempre ao BANCO MRK! Tenha um bom dia.')
