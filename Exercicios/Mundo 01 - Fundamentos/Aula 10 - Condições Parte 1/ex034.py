# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o salário do funcionário. R$'))

if sal > 1250.00:
    novo = sal * 1.1
    print('O salário do funcionário era de R${:.2f}.\n'
          'Com o aumento de 10%, seu novo salário é de R${:.2f}'.format(sal, novo))
else:
    novo = sal * 1.15
    print('O salário do funcionário era de R${:.2f}.\n'
          'Com o aumento de 15%, seu novo salário é de R${:.2f}'.format(sal, novo))
