# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

placar = 0
player = -1

while True:
    escolha_player = input('Escolha PAR ou ÍMPAR: ').upper().replace(' ', '')
    if escolha_player in ['P', 'PAR', 'I', 'ÍMPAR', 'IMPAR']:
        while player < 0 or player > 5:
            player = int(input('Agora, escolha um número entre 0 e 5: '))

        pc = randint(0, 5)
        soma = pc + player

        if soma % 2 == 0:
            print(f'A soma entre {pc} e {player} é PAR!')
            if escolha_player in ['P', 'PAR']:
                print('PARABÉNS!!! Você venceu!!')
                placar += 1
            else:
                break
        else:
            print(f'A soma entre {pc} e {player} é ÍMPAR!')
            if escolha_player in ['I', 'ÍMPAR', 'IMPAR']:
                print('PARABÉNS!!! Você venceu!!')
                placar += 1
            else:
                break
        player = -1

print('Que pena, você perdeu.')
print(f'Você conseguiu vencer o computador {placar} vez(es) seguida(s).')
print('GAME OVER')
