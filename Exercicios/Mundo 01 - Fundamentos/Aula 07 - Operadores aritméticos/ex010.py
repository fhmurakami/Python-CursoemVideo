# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$ 1,00 = R$3,27

r = float(input('Quanto dinheiro você possui? R$'))

d = r/3.27

print('Reais: {:.2f}\nDólares: {:.2f}'.format(r,d))