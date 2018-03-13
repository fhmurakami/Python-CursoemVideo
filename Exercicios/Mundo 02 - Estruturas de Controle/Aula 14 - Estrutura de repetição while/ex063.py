# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência
# de Fibonacci. Ex: 0, 1, 1, 2, 3, 5, 8...

n = int(input('Digite o número de elementos da sequência de Fibonacci: '))

fib = 0
ant = 0
atu = 1

print('{} {}'.format(ant, atu), end=' ')

while (n-2) > 0:
    fib = ant + atu
    print('{}'.format(fib), end=' ')
    ant = atu
    atu = fib
    n -= 1
