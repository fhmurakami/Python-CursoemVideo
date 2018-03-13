# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

casa = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Em quantos anos será pago o valor total da casa? '))

prest = (casa / anos) / 12

print(
    'Para pagar uma casa no valor de R$ {:.2f} em {} anos, as prestações serão de R$ {:.2f}.'.format(casa, anos, prest))

if prest > sal * 0.3:
    print('O empréstimo foi negado, pois as prestações excedem 30% do salário. ')
else:
    print('O empréstimo foi aprovado.')
