# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status, de acordo com a ta-
# bela abaixo:
# - Abaixo de 18.5: Abaixo do peso;
# - Entre 18.5 e 25 : Peso ideal;
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite a altura em m: '))

imc = peso/(altura**2)

print('Seu IMC é: {:.1f}'.format(imc))
print('Classificação: ', end='')

if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')