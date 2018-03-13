# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('''Digite um número inteiro para saber sua tabuada.
(Para sair, digite um valor negativo): '''))
    if n < 0:
        break
    else:
        print('-' * 20)
        for i in range(0, 11):
            print(f'{n:2} x {i:2} = {n*i:2}')
        print('-' * 20)
print('Programa encerrado.')