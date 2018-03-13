# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = ' '

# while sexo != 'M' and sexo != 'F':
while sexo not in ['M', 'F', 'MASCULINO', 'FEMININO']:
    sexo = input('Informe seu sexo (M/F): ').upper().replace(' ', '')
sexo = sexo[0]
print('A pessoa é do sexo {}.'.format('masculino' if sexo == 'M' else 'feminino'))
