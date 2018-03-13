# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# (desconsiderando o flag)

n = soma = 0
cont = -1

while n!= 999:
    soma += n
    n = int(input('Digite um número inteiro (999 para terminar): '))
    cont += 1
print('Foram digitados {} números e a soma entre eles é igual a {}.'.format(cont, soma))
