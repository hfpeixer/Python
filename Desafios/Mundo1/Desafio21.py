import pygame
#iniciar
pygame.init()
#carregar arquivo
pygame.mixer.music.load('EU TENHO A SENHA.mp3')
#play
pygame.mixer_music.play()
print(input('Você quer pausar a musíca: '))
#pausar
pygame.mixer_music.pause()
#finaliza evento
pygame.event.wait()
