# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de km percorridos: '))
d = int(input('Digite a quantidade de dias de aluguel: '))

p = (d * 60) + (km * 0.15)

print('O carro foi alugado por {} dias, e foram percorridos {}km.\nO valor a ser pago é R${:.2f}'.format(d, km, p))
