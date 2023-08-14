import os

import pygame

pygame.init()
pygame.mixer.init()


def play_mp3(mp3_path):
    pygame.mixer.music.load(mp3_path)
    pygame.mixer.music.play()


def main():
    while True:
        os.system('cls')
        mp3_path = input(
            'Digite o caminho do arquivo MP3 que deseja reproduzir (ou "sair" para finalizar).'
            '\nTambém coloque a extensão .mp3. Ex: desafio_021.mp3: ')

        if mp3_path.lower() == 'sair':
            break

        play_mp3(mp3_path)

        while pygame.mixer.music.get_busy():
            pass  # Aguarda a reprodução do arquivo terminar

        option = input("Deseja reproduzir novamente? (s/n): ")
        if option.lower() != 's':
            print('Programa encerrado.')
            break

    pygame.mixer.music.stop()
    pygame.quit()


if __name__ == "__main__":
    main()
