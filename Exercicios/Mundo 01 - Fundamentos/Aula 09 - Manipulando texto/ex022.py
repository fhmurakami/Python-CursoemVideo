# Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e
# minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

# Recebe o nome do usuário:
nome = input('Digite o seu nome completo: ')

# Separa os nomes e cria uma lista:
n1 = nome.split()

# Imprime em letras maiúsculas:
print('Maíusculo: {}'.format(nome.upper()))
# Imprime em letras minúsculas:
print('Minúsculo: {}'.format(nome.lower()))
# Retira os espaços e imprime a quantidade de letras do nome completo:
print('Quantidade de letras: {}'.format(len(nome.replace(' ',''))))
# Imprime a quantidade de letras do primeiro nome contido na lista 'n1':
print('Letras do primeiro nome: {}'.format(len(n1[0])))
