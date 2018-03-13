# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.

maior = 0.0
menor = 0.0

for c in range(0, 5):
    peso = float(input('Digite seu peso em kg: '))
    if c == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O maior peso é {} kg e o menor {} kg'.format(maior, menor))
