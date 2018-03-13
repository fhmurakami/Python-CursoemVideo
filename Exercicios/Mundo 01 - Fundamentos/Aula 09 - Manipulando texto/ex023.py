# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Recebe um número inteiro:
num = int(input('Digite um número de 0 a 9999: '))

# Separa a unidade:
u = num // 1 % 10
# Separa a dezena:
d = num // 10 % 10
# Separa a centena:
c = num // 100 % 10
# Separa o milhar:
m = num // 1000 % 10

print('Analisando o número {}.'.format(num))
print('Milhar:  {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena:  {}'.format(d))
print('Unidade: {}'.format(u))
