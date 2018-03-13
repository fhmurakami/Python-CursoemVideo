# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Digite a distância da viagem em km: '))

# preco = dist * 0.50 if dist <=200 else dist * 0.45

if (dist > 200.0):
    preco = dist * 0.45
else:
    preco = dist * 0.5
print('O preço da passagem para uma viagem de {}km é de R${:.2f}'.format(dist, preco))
