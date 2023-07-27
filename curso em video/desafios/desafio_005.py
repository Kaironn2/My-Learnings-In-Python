import os

def vizinhos(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

while True:

    while True:

        try:
            numero = int(input('Digite um número para ver seu sucessor e seu atencessor: '))
            break
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números.')

    os.system('cls')

    antecessor, sucessor = vizinhos(numero)

    print(
        f'Antecessor -> {antecessor}\n'
        f'número -----> {numero}\n'
        f'Sucessor ---> {sucessor}'
        )

    while True:

        opcao = input('Você deseja realizar outra operação? [s]im [n]ão: ').upper()

        if opcao == '':
            os.system('cls')
            continue
        elif opcao[0] in 'S':
            os.system('cls')
            encerrar = False
            break
        elif opcao[0] in 'N':
            encerrar = True
            break
        else:
            os.system('cls')
            print('Opção inválida. Por favor, digite SIM para continuar e NÃO para finalizar.')
    
    if encerrar:
        print('Programa encerrado')
        break
