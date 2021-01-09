#Crie um programa que toque um MP3

import pygame
pygame.mixer.init()
pygame.mixer.music.load('medo.mp3')
pygame.mixer.music.play()
x = input('Digite algo para parar: ')