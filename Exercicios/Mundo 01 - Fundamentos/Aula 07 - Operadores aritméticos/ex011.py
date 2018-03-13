# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro  de tinta pinta uma área de 2m^2.

larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

area = larg * alt

tinta = area / 2

print('A área a ser pintada é {}m * {}m = {}m², e a quantidade de tinta necessária é {} litros.'.format(larg, alt, area,
                                                                                                    tinta))
