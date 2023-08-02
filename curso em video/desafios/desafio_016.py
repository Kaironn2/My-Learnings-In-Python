import math
import os 

def validar_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números. Use o . no lugar na vírgula.')

def validate_option(mensagem):
    global encerrar

    while True:

        opcao_user = input(f'{mensagem}').upper()

        if opcao_user == '':
            os.system('cls')
            continue
        elif opcao_user[0] not in 'SN':
            os.system('cls')
            print('Opção inválida. Por favor, digite SIM para continuar e NÃO para finalizar.')
            continue
        else:
            if opcao_user == 'S':
                encerrar = False
            else:
                encerrar = True
            break

def truncar_numero(numero):
    valor_truncado = math.trunc(numero)
    return valor_truncado


while True:

    numero = validar_float('Digite o número que você deseja truncar(mostrar porção inteira): ')

    numero_truncado = truncar_numero(numero)

    os.system('cls')

    print(f'Você digitou {numero} e sua porção inteira é {numero_truncado}.\n')

    validate_option('Você deseja truncar outro número? [s]im [n]ão: ')

    if encerrar:
        print('Programa encerrado.')
        break

    os.system('cls')
    