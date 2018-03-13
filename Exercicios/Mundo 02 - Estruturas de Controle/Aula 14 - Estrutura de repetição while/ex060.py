# Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input('Digite um número inteiro para saber seu fatorial: '))
fat = 1
num = n

while num >= 1:
    fat *= num
    num -= 1

print('O fatorial de {} é {}'.format(n, fat))
