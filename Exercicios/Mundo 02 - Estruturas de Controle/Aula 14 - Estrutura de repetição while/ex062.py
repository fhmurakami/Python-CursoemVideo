# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.

pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = 10
pa = pt
n = 0

while termo != 0:
    while n < termo:
        print('{}'.format(pa), end=' ')
        pa += r
        n += 1
    termo = int(input('\nDigite a quantidade de próximos termos que deseja visualizar: '))
    n = 0