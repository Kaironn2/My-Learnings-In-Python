import os

current_list = []
redo_list = []
counter = 0


def undo():
    global counter
    if len(current_list) > 0:
        redo_list.append(current_list[-1])
        current_list.pop()
        counter += 1
    else:
        print('Não há nada para desfazer.')


def redo():
    global counter
    if counter > 0:
        current_list.append(redo_list[-1])
        redo_list.pop()
        counter -= 1
    else:
        print('Não há nada para refazer.')


while True:

    if len(current_list) > 0:
        for indice, item in enumerate(current_list):
            print(f'{indice + 1} - {item}')
    else:
        print('Sua lista está vazia.')
    print()

    print(
        'Comandos: \n'
        'Para refazer a última ação: refazer\n'
        'Para desfazer a última ação: desfazer\n'
        'Para adicionar algo na lista, apenas digite o que você deseja adicionar.\n\n'
    )
    option = input('Digite um dos comandos: ')

    os.system('cls')

    if option == 'refazer':
        redo()
    elif option == 'desfazer':
        undo()
    elif option == 'limpar':
        current_list = []
    elif option == 'exit':
        print('Programa encerrado.')
        break
    else:
        current_list.append(option)
        counter = 0
        redo_list = []
