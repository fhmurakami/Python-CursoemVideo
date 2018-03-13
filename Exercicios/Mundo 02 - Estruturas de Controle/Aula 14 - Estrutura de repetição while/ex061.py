# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = 0
pa = pt

while termo < 10:
    print('{}'.format(pa), end=' ')
    pa += r
    termo += 1
