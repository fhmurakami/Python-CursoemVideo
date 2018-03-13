# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua cate-
# goria, de acordo com a idade:
# - Até 9 anos: Mirim.
# - Até 14 anos: Infantil
# - Até 19 anos: Júnior
# - Até 20 anos: Sênior
# - Acima: Master

from datetime import date

ano_atual = date.today().year

nasc = int(input('Digite o ano de nascimento do atleta: '))

idade = ano_atual - nasc

print('Quem nasceu no ano {} tem {} anos em {}.'.format(nasc, idade, ano_atual))
print('O atleta está na categoria: ', end='')

if idade < 10:
    print('MIRIM.')
elif idade < 15:
    print('INFANTIL.')
elif idade < 20:
    print('JÚNIOR.')
elif idade < 26:
    print('SÊNIOR.')
else:
    print('MASTER.')