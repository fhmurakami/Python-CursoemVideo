# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

# pygame.init() # Não funcionou
pygame.mixer.init()

# Carrega um arquivo MP3:
pygame.mixer.music.load('ex021.mp3')

# Reproduz um arquivo MP3:
pygame.mixer.music.play()
# Espera terminar de reproduzir para encerrar a aplicação:
# pygame.event.wait() # Não funcionou

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
