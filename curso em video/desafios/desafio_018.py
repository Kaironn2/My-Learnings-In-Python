import os
import math

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

def calc_seno(angulo):
    global seno
    seno = math.sin(angulo)
    return seno

def calc_coseno(angulo):
    global coseno
    coseno = math.cos(angulo)
    return coseno

def calc_tangente(angulo):
    global tangente
    tangente = math.tan(angulo)
    return tangente

def validar_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números inteiros.')

while True:

    angulo = validar_int('Digite o ângulo para fazer seu seno, coseno e tangente: ')

    calc_seno(angulo)
    calc_coseno(angulo)
    calc_tangente(angulo)

    print(
        f'Ângulo: {angulo}°\n'
        f'Seno: {seno}\n'
        f'Coseno: {coseno}\n'
        f'Tangente: {tangente}°\n'
    )

    validate_option('Você deseja ver informações trigonométricas de outro ângulo? [s]im [n]ão: ')

    if encerrar:
        print('Programa finalizado')
        break

    os.system('cls')
