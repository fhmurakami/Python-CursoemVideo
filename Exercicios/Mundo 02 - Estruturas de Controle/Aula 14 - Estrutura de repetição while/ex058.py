# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

contador = 1

computador = randint(0, 10)  # Computador sorteia um número entre 0 e 5.

print('\033[35;m-=-\033[m' * 20)
print('\033[36mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m')
print('\033[35;m-=-\033[m' * 20)

jogador = int(input('Em que número eu pensei? '))  # Recebe a resposta do jogador.

print('\033[32;mPROCESSANDO...\033[m')
sleep(0.5) # Faz o computador 'dormir' por 0.5 segundo.
while jogador != computador:
    jogador = int(input('Não foi desta vez... Tente novamente: '))
    print('\033[32;mPROCESSANDO...\033[m')
    sleep(0.5)  # Faz o computador 'dormir' por 0.5 segundo.
    contador += 1
print('\033[34;mPARABÉNS! Você conseguiu me vencer! Você precisou de {} palpite(s).\033[m'.format(contador))

