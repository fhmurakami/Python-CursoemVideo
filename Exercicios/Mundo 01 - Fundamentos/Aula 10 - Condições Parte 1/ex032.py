# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

from datetime import date

ano = int(input('Digite um ano. Para analisar o ano atual, digite 0: '))
if ano == 0:
    ano = date.today().year

if (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)):
    print('O ano {} É bissexto.'.format(ano))
else:
    print('O ano {} NÃO É bissexto.'.format(ano))

# if (ano % 400 == 0):
#     print('O ano {} É bissexto.'.format(ano))
# elif(ano % 100 == 0):
#     print('O ano {} NÃO É bissexto.'.format(ano))
# elif(ano % 4 == 0):
#     print('O ano {} É bissexto.'.format(ano))
# else:
#     print('O ano {} NÃO É bissexto.'.format(ano))