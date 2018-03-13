# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos,sin,tan,radians

ang = float(input('Digite um ângulo: '))
rad = radians(ang)
print('O ângulo digitado foi {:.2f}.\nSeno: {:.2f}, Cosseno: {:.2f}, Tangente: {:.2f}'.format(ang, sin(rad), cos(rad),
                                                                                              tan(rad)))