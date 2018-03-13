# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tc = float(input('Digite uma temperatura em °C: '))

tf = (9 / 5 * tc) + 32

print('A temperatura de {}°C corresponde a {}°F.'.format(tc, tf))
