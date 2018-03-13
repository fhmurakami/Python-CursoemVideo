# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.

nome = str(input('Digite seu nome completo: ')).strip()

lista_nome = nome.split()

print('O nome da pessoa é: {}'.format(nome.title()))
print('O primeiro nome é {}'.format(lista_nome[0].capitalize()))
print('O último nome é {}'.format(lista_nome[-1].capitalize()))
