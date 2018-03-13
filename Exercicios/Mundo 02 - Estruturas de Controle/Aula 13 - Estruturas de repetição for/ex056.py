# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do HOMEM mais velho.
# - Quantas mulheres tem menos de 20 anos.

soma_idade = 0

velho = 0

mulheres = 0

old_man = ''

for c in range(0, 4):
    nome = (input('Digite o nome: ')).title()
    idade = int(input('Digite a idade: '))
    genero = input('Digite o sexo [M/F]: ').upper()

    soma_idade += idade
    if genero == 'M' or genero == 'F':
        if (genero == 'M') and (idade > velho):
            old_man = nome
            velho = idade
        if genero == 'F' and idade < 20:
            mulheres += 1
    else:
        print('Genero inválido!')
        break

media = soma_idade / 4

print('''\nA média de idade do grupo é {} anos;
O homem mais velho se chama {};
{} mulher(es) tem menos de 20 anos.'''.format(media, old_man, mulheres))
