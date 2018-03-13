# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de paga-
# mento:
# - À vista, dinheiro/cheque: 10% de desconto;
# - À vista no cartão: 5% de desconto;
# - Em até 2x no cartão: preço normal;
# - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS MURAKAMI '))
valor = float(input('Digite o valor da compra: R$ '))

print('''Escolha a forma de pagamento:
[ 1 ] - À vista em dinheiro ou cheque.
[ 2 ] - À vista no cartão.
[ 3 ] - 2x no cartão.
[ 4 ] - 3x ou mais no cartão.''')

option = int(input('Opção: '))

if option == 1:
    desc = valor * 0.9
    print('O valor a ser pago é R$ {:.2f}.'.format(desc))
elif option == 2:
    desc = valor * 0.95
    print('O valor a ser pago é R$ {:.2f}.'.format(desc))
elif option == 3:
    print('O valor a ser pago é R$ {:.2f}.'.format(valor))
    print('As parcelas serão de R$ {:.2f}'.format(valor/2))
elif option == 4:
    desc = valor * 1.2
    parcelas = int(input('Quantas parcelas? '))
    print('O valor a ser pago é R$ {:.2f}.'.format(desc))
    print('As parcelas serão de R$ {:.2f}'.format(desc/parcelas))
else:
    print('Opção inválida.')
