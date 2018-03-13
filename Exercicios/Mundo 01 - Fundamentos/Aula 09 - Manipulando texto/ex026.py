# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()

print('A letra \'A\' aparece {} vezes'.format(frase.upper().count('A')))
print('A posição da primeira letra \'A\' é {}'.format(frase.upper().find('A')+1))
print('A posição da última letra \'A\' é {}'.format(frase.upper().find('A',-1)+1))
