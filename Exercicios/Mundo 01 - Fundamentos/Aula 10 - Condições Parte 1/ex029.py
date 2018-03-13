# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Digite a velocidade do carro: '))

if vel > 80:
    multa = (vel-80)*7
    print('Você foi multado!')
    print('O limite de velocidade é 80km/h e a velocidade do carro é {}km/h'.format(vel))
    print('O valor da multa a ser paga é R${:.2f}'.format(multa))
else:
    print('Você está dentro do limite de velocidade.')