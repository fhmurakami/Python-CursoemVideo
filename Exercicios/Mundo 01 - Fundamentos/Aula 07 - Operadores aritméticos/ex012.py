# Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço: '))

np = p * 0.95

print('Preço antigo: {:.2f}\nPreço com 5% de desconto: {:.2f}'.format(p, np))
