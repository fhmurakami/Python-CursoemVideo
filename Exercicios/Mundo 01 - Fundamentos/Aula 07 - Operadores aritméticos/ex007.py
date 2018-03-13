# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2

print('N1 = {:.1f}, N2 = {:.1f}, Média = {:.1f}'.format(n1, n2, m))
