# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

# Regra de existência do triângulo:
# A medida de qualquer um dos lados deve ser menor que a soma dos outros dois, e menor que o valor absoluto da diferença
# entre os mesmos.
# Ex.: |b - c| < a < b + c

if ((abs(b - c) < a and a < (b + c)) and (abs(a - c) < b and b < (a + c)) and (abs(b - a) < c and c < (b + a))):
    print('É possível formar um triângulo com as retas de comprimentos {}, {} e {}'.format(a, b, c))
else:
    print('Não é possível formar um triângulo com as retas de comprimentos {}, {} e {}'.format(a, b, c))
