from random import randint
import os

lista_nomes = [
    'Jonathas', 'Pedro', 'Michael', 'Luiz', 'Madre', 'Wendell', 'Maria', 'Larissa', 'Priscila', 'Eduarda'
]
ultimo_ganhador = None

def sortear():
    global ultimo_ganhador
    if lista_nomes == []:
        print('Lista vazia. Adicione nomes para poder sortear.')
    else:
        tamanho_lista = len(lista_nomes) - 1
        random_number = randint(0, tamanho_lista)
        nome_sorteado = lista_nomes[random_number]
        # print(f'Ganhador do sorteio: {nome_sorteado}')
        ultimo_ganhador = nome_sorteado

def limpar_lista():
    global lista_nomes
    if len(lista_nomes) == 0:
        print('Nada para limpar aqui. ')
    else:
        lista_nomes = []

def ver_lista():
    global lista_nomes
    
    if len(lista_nomes) != 0:
        for nome in lista_nomes:
            print(nome)
        print()
    else:
        print('Ops! Nada para mostrar aqui. Primeiro adicione nomes na lista.')

def adicionar_nome_na_lista():
    global lista_nomes
    while True:
        nome_novo = input('Digite o nome a ser adicionado na lista: ')
        print(f'O nome "{nome_novo}" foi adicionado na lista.')
        lista_nomes.append(nome_novo)

        while True:
            opcao = input('Deseja adicionar outro nome na lista? [s]im [n]ão: ').upper()
            if opcao == '':
                os.system('cls')
            elif opcao in 'SN':
                if opcao == 'S':
                    encerrar = False
                    os.system('cls')
                    break
                elif opcao == 'N':
                    encerrar = True
                    break
            else:
                os.system('cls')
                print('Opção inválida. Digite SIM para adicionar outro nome e NÃO para voltar ao menu.')
        
        if encerrar:
            os.system('cls')
            break

def menu_opcoes():
    global lista_nomes
    global encerrar
    while True:
        if ultimo_ganhador is not None:
            print(f'Último sorteado nome sorteado: {ultimo_ganhador}')
        print(
            'O que você deseja fazer?\n\n'
            '1 - Sortear um nome\n'
            '2 - Limpar a lista\n'
            '3 - Adicionar um nome na lista\n'
            '4 - Mostrar lista\n'
            '5 - sair do programa\n'
        )

        opcao_user = input('\nDigite uma das opções listadas: ')
        os.system('cls')
        
        if opcao_user == '':
            os.system('cls')
            continue
        elif opcao_user[0] == '1':
            sortear()
        elif opcao_user[0] == '2':
            limpar_lista()
        elif opcao_user[0] == '3':
            adicionar_nome_na_lista()
        elif opcao_user[0] == '4':
            ver_lista()
        elif opcao_user[0] == '5':
            encerrar = True
            break
        else:
            os.system('cls')
            print('Opção inválida. Por favor, digite uma das opções listadas')

while True:

    menu_opcoes()

    if encerrar:
        print('Programa finalizado.')
        break

