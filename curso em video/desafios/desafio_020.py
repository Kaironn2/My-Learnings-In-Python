from random import shuffle
import os

lista = []

def shuffle_list(lista):
    shuffled_list = shuffle(lista)
    return shuffled_list

def opcao_sn(msg):
    while True:
        try:
            opcao = input(msg).upper()
            if opcao not in 'SN':
                os.system('cls')
                print('Por favor, digite SIM ou NÃO.')
                continue
            break
        except IndexError:
            os.system('cls')
            print('Você não digitou nada. ')
            continue
    return opcao

def add_name():
    global lista

    while True:
        nome = input('Digite o nome que você deseja inserir na lista: ')

