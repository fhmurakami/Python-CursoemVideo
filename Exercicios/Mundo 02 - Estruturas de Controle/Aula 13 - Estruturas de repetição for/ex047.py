# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# for c in range(1,51):
#     if c % 2 == 0:
#         print(c)

# Desta forma reduz o numero de iterações, logo, o programa é mais rápido.
for c in range(1,51,2):
    print(c+1, end=' ')
