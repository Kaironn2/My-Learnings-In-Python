from random import shuffle
import os

lista = []

def shuffle_list(lista):
    if len(lista) == 0:
        print('Nada para embaralhar. Primeiro adicione nomes à lista.')
    else:
        shuffled_list = shuffle(lista)
        print('A lista foi embaralhada!')
        ver_lista()
        return shuffled_list

def opcao_sn(msg):
    while True:
        try:
            opcao = input(msg).upper()
            if opcao[0] not in 'SN':
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
        lista.append(nome)
        print(f'{nome} foi adicionado na lista.')

        opcao = opcao_sn('Você deseja adicionar outro nome na lista? [s]im [n]ão: ')

        if opcao[0] == 'N':
            os.system('cls')
            break
            
        os.system('cls')

def apagar_nome():
    global lista

    if len(lista) != 0:
        
        while True:
            
            ver_lista()
            try:
                apagar_da_lista = int(input('Digite o índice relativo ao nome que você deseja apagar(Ex: 1 - Rafael, digite 1): '))

                if apagar_da_lista == 0:
                    os.system('cls')
                    print('Por favor, digite um dos índices listados.')
                    continue

                indice_apagar = apagar_da_lista - 1
                print(f'{lista[indice_apagar]} foi apagado da lista.')
                lista.pop(indice_apagar)
            except IndexError:
                os.system('cls')
                print('Por favor, digite um dos índices listados.')
                continue
            
            opcao = opcao_sn('Você deseja apagar outro nome da lista? [s]im [n]ão: ')

            if opcao == 'N':
                os.system('cls')
                break

            os.system('cls')

    else:
        print('Não há nada para apagar ainda. Primeiro adicione nomes à lista.')

def limpar_lista():
    global lista
    if len(lista) == 0:
        print('Nada pagar apagar. Primeiro adicione nomes à lista.')
    else:
        lista = []
        print('A lista inteira foi apagada!')

def ver_lista():
    global lista

    if len(lista) != 0:
        for indice, nome in enumerate(lista):
            print(f'{indice + 1} - {nome}')
        print()
    else:
        print('Ops, nada para mostrar :(')

def menu():
    lista_opcoes_menu = [numero for numero in range(1, 7)]

    while True:
        print(
            'O que você deseja fazer?\n\n'
            '1 - Adicionar um nome na lista\n'
            '2 - Apagar um nome da lista\n'
            '3 - Embaralhar lista\n'
            '4 - Ver lista\n'
            '5 - Apagar lista inteira\n'
            '6 - Sair do programa\n'

        )

        try:
            opcao_menu = int(input('Digite uma das opções listadas: '))

            if opcao_menu not in lista_opcoes_menu:
                os.system('cls')
                print('Digite uma das opções listadas.')
                continue

        except ValueError:
            os.system('cls')
            print('Digite apenas números! Escolha uma das opções listadas.')
            continue
        return opcao_menu


while True:

    opcao = menu()

    os.system('cls')

    match opcao:
        
        case 1:
            add_name()
        
        case 2:
            apagar_nome()
        case 3:
            shuffle_list(lista)

        case 4:
            ver_lista()
        
        case 5:
            limpar_lista()

        case 6:
            print('Programa encerrado.')
            break
    
