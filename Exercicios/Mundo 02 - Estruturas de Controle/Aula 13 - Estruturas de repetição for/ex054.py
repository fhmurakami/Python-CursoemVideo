# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores. (Considere 21 anos)

from datetime import date

atual = date.today().year

maior = 0
menor = 0

for c in range(0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = atual - nasc
    if idade > 20:
        maior += 1
    else:
        menor += 1

print('{} pessoas ainda não atingiram a maioridade e {} já são maiores.'.format(menor, maior))
