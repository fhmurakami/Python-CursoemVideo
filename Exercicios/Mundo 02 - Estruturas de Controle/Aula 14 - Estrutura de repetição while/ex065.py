# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

resp = 'S'
soma = cont = maior = menor = 0

while resp in 'SIM':
    n = int(input('Digite um número inteiro: '))
    soma += n
    if cont == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    cont += 1
    resp = input('Deseja continuar (S/N)? ').upper().replace(' ', '')
media = soma / cont

print(
    'A média dos {} valores digitados foi {:.2f}, o maior valor foi {} e o menor valor foi {}.'.format(cont, media,
                                                                                                       maior, menor))
