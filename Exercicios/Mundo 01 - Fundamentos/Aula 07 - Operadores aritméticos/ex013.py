# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o salário: '))

ns = s * 1.15

print('Salário: R${:.2f}, Salário com 15% de aumento: R${:.2f}'.format(s, ns))
