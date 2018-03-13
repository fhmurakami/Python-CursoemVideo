# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite o primeiro número: '))
# Atribui n1 como maior e menor número
maior = n1
menor = n1

n2 = float(input('Digite o segundo número: '))
# Testa se n2 é maior que 'maior', se verdadeiro, atribui n2 como 'maior'
if (n2 > maior):
    maior = n2
# Se falso, atribui n2 como menor. (Se forem iguais, é indiferente se 'maior' é igual n1 ou n2)
else:
    menor = n2

n3 = float(input('Digite o terceiro número: '))
# Testa se n3 é maior que 'maior', se verdadeiro, atribui n3 como 'maior'.
if (n3 > maior):
    maior = n3
# Se falso, testa se n3 é menor que 'menor', e se verdadeiro, atribui n3 como 'menor'.
elif n3 < menor:
    menor = n3

print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))