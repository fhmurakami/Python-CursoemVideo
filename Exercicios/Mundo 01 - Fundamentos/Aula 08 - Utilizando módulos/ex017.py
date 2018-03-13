# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hip = (co ** 2 + ca ** 2) ** (1 / 2)

print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {}'.format(co, ca, hip))

# Segunda Solução:
#
# from math import hypot
#
# co = float(input('Digite o comprimento do cateto oposto: '))
# ca = float(input('Digite o comprimento do cateto adjacente: '))
#
# print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {}'.format(co, ca, hypot(co, ca)))
