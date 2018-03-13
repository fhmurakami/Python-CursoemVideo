# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona.

frase = input('Digite uma frase: ').replace(' ', '')
palindromo = 0
inv = []

# Sem utilizar o laço 'for':
# inv = frase[::-1]

for c in range(0, len(frase)):
    if frase[c] == frase[len(frase) - (c + 1)]:
        palindromo += 1
    inv.insert(c, frase[len(frase) - (c + 1)])

print('A frase {} ao contrário é {}'.format(frase, ''.join(inv)))

if palindromo == len(frase):
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
