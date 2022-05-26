import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()
pygame.mixer.music.load('../music.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#from playsound import playsound
#playsound('henrique.mp3')