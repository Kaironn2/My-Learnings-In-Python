import os
import json

current_list = []
redo_list = []
counter = 0
file_name = 'Lista de Tarefas'
# Pega o caminho atual do arquivo
file_path = os.path.join(os.path.dirname(__file__), file_name)


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


def clear():
    global counter, current_list, redo_list
    current_list = []
    redo_list
    counter = 0


def add():
    global counter, redo_list, current_list
    current_list.append(option)
    counter = 0
    redo_list = []


while True:

    if len(current_list) > 0:
        for indice, item in enumerate(current_list):
            print(f'{indice + 1} - {item}')
    else:
        print('Sua lista está vazia.')
    print()

    print(
        'Comandos: \n'
        'Para refazer a última ação: redo\n'
        'Para desfazer a última ação: undo\n'
        'Para limpar os itens da lista: clear\n'
        'Para importar uma lista pronta: import\n'
        'Para exportar e salvar sua lista: export\n'
        'Para adicionar algo na lista, apenas digite o que você deseja adicionar.\n'
        'Para encerrar o programa: exit\n\n'
    )
    option = input('Digite um dos comandos: ')

    os.system('cls')

    if option == 'redo':
        redo()

    elif option == 'undo':
        undo()

    elif option == 'clear':
        clear()

    elif option == 'exit':
        print('Programa encerrado.')
        break

    elif option == 'export':
        with open(file_path, 'w') as file_json:
            json.dump(current_list, file_json, indent=2)
        print('Sua lista foi exportada com sucesso!')

    elif option == 'import':
        with open(file_path, 'r') as file_json:  # caminho do arquivo, modo de abertura
            # Faz a leitura do arquivo Json em string para não ocorrer um erro de leitura
            content = file_json.read()
            # Depois pegamos a lista já em STR e guardamos na variável
            current_list = json.loads(content)

    elif option == '':
        continue

    else:
        add()
