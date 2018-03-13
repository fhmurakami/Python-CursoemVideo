# Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais.
# - Isósceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

# Regra de existência do triângulo:
# A medida de qualquer um dos lados deve ser menor que a soma dos outros dois, e menor que o valor absoluto da diferença
# entre os mesmos.
# Ex.: |b - c| < a < b + c

if (abs(b - c) < a < (b + c)) and (abs(a - c) < b < (a + c)) and (abs(b - a) < c < (b + a)):
    # Tipo do triângulo:
    if a == b == c:
        tipo = 'EQUILÁTERO'
    elif a != b != c != a:
        tipo = 'ESCALENO'
    else:
        tipo = 'ISÓSCELES'
    print('É possível formar um triângulo {} com as retas de comprimentos {}, {} e {}'.format(tipo, a, b, c))
else:
    print('Não é possível formar um triângulo com as retas de comprimentos {}, {} e {}'.format(a, b, c))
