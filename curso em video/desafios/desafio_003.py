import os

def somar(numero1, numero2):
    soma = numero1 + numero2
    os.system('cls')
    print(f'{numero1} + {numero2} = {soma}')

while True:

    while True:
        try:
            numero1 = int(input('Digite um número: '))
            numero2 = int(input('Digite mais um número: '))
            break
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números.')

    somar(numero1, numero2)

    opcao = input('Você deseja realizar outra operação? [s]im [n]ão: ').upper().startswith('S')

    if opcao:
        os.system('cls')
    else:
        print('Programa finalizado.')
        break
