# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite o nome completo: ').strip()

# Transforma as palavras em letra maiúscula e  divide os nomes da cidade em uma lista:
lista_nomes = nome.upper().split()

# Imprime se o primeiro nome começa com a palavra SANTO:
print('A pessoa tem SILVA no nome? {}'.format('SILVA' in lista_nomes))
