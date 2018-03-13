# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos;
# B) Quantos homens foram cadastrados;
# C) Quantas mulheres tem menos de 20 anos.

tot_18 = tot_homem = tot_mulher = 0

while True:
    sexo = ' '
    opt = ' '
    idade = 0

    while idade <= 0:
        idade = int(input('Digite a idade: '))
    while sexo not in 'MF':
        sexo = input('Digite o sexo: (M/F): ').upper().replace(' ', '')

    if idade > 18:
        tot_18 += 1
    if idade < 20 and sexo == 'F':
        tot_mulher += 1
    if sexo == 'M':
        tot_homem += 1
    while opt not in 'SN':
        opt = input('Deseja continuar? (S/N) ').upper().replace(' ', '')
    if opt == 'N':
        break

print(f'{tot_18} pessoas tem mais de 18 anos, {tot_homem} homens foram cadastrados e '
      f'{tot_mulher} mulheres tem menos de 20 anos.')
