# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

n = float(input('Digite um número real: '))
print('O número digitado foi {} e sua parte inteira é {}'.format(n, int(n)))

# Segunda forma:

# from math import trunc
#
# n = float(input('Digite um número real: '))
#
# print('O número digitado foi {}.\nSua parte inteira é {}.'.format(n, trunc(n)))
