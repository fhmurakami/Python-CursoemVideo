# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

# from random import randint
#
# n = randint(0, 5)
#
# num = int(input('Tente adivinhar o número que o computador escolheu. Digite um número entre 0 e 5: '))
#
# if num == n:
#     print('Parabéns, você acertou!')
# else:
#     print('O computador venceu. =/\nO número escolhido correto era {}.\nTente novamente.'.format(n))

from random import randint
from time import sleep

computador = randint(0, 5)  # Computador sorteia um número entre 0 e 5.

print('\033[35;m-=-\033[m' * 20)
print('\033[36mVou pensar em um núemro entre 0 e 5. Tente adivinhar...\033[m')
print('\033[35;m-=-\033[m' * 20)
jogador = int(input('Em que número eu pensei? '))  # Recebe a resposta do jogador.

print('\033[32;mPROCESSANDO...\033[m')
sleep(1) # Faz o computador 'dormir' por 2 segundos.

if jogador == computador:
    print('\033[34;mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[31;mGANHEI! A resposta correta era {} e não {}\033[m'.format(computador, jogador))
