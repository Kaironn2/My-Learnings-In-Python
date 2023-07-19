import os

while True:
    while True:
        try:
            numero = int(input('Digite um número para ver seu sucessor e seu atencessor: '))
            break
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números.')

    def vizinhos(numero):
        antecessor = numero - 1
        sucessor = numero + 1

        os.system('cls')

        print(
            f'Antecessor -> {antecessor}\n'
            f'número -----> {numero}\n'
            f'Sucessor ---> {sucessor}'
            )

    vizinhos(numero)

    opcao = input('Você deseja analisar outro número? [s]im [n]ão: ').upper().startswith('S')

    if opcao:
        os.system('cls')
    else:
        print('Programa finalizado.')
        break
