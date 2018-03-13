# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = date.today().year

nasc = int(input('Digite o ano de nascimento: '))

print('Digite o seu gênero:\nM para masculino;\nF para feminino.')
genero = input('Gênero: ').upper()

idade = ano - nasc

print('Quem nasceu no ano {} tem {} anos em {}.'.format(nasc, idade, ano))

if genero == 'F':
    print('O alistamento não é obrigatório para mulheres.')
elif genero == 'M':
    if idade < 18:
        print('Ainda falta(m) {} ano(s) para seu alistamento.'.format(18-idade))
        print('Seu alistamento será em {}.'.format(ano+(18-idade)))
    elif idade == 18:
        print('Você deve se alistar esse ano.')
    else:
        print('Você deveria ter se alistado há {} ano(s).'.format(idade-18))
        print('Seu alistamento foi no ano {}.'.format(ano-(idade-18)))
else:
    print('O gênero digitado é inválido.')
