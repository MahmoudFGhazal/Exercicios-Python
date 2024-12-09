import pygame
pygame.init()
pygame.mixer.music.load('pua.mp3')
while True:
    pygame.mixer.music.play()
    if input("Se você deseja sair insira 'sair'\ne se quiser repetir aperte qualquer outro botão: ").lower().strip() == 'sair':
        break
