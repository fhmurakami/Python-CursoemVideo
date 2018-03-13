# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))

div = 0

for c in range(1, n + 1):
    if (n % c == 0):
        div += 1

if div == 2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))
