import pygame
import os
import time

def playmp3(mp3file):
    print(f'Reproduzindo {mp3file}')
    pygame.mixer.init()                 # inicia o mixer
    pygame.mixer.music.load(mp3file)    # carregar o arquivo mp3 no mixer
    pygame.mixer_music.play()           # toca o arquivo carregado
    time.sleep(6)                       # tempo do audio 
    print('O audio acabou!')
    os.system('exit')

os.system('cls')

playmp3('desafio_021.mp3')              # Nome do arquivo mp3
