import os

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

def validar_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números. Use o . no lugar na vírgula.')

def validar_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números inteiros.')


def calc_valor_aluguel_km(quant_km):
    pagar_km_rodado = quant_km * 0.15
    return pagar_km_rodado

def calc_valor_aluguel_dia(dias):
    pagar_dia_alugado = 60 * dias
    return pagar_dia_alugado

def calc_total_aluguel(aluguel_dia, aluguel_km):
    valor_total = aluguel_dia + aluguel_km
    return valor_total


while True:

    dias_alugados = validar_int('Quantos dias o carro ficou alugado? Digite apenas números inteiros: ')
    valor_aluguel_dia = calc_valor_aluguel_dia(dias_alugados)

    km_rodados = validar_float('Quantos KM você percorreu com o carro? Digite apenas números(. no lugar da ,): ')
    valor_aluguel_km = calc_valor_aluguel_km(km_rodados)

    valor_total_aluguel = calc_total_aluguel(valor_aluguel_dia, valor_aluguel_km)

    os.system('cls')

    print(
        f'Você rodou {km_rodados:.1f}KM, cada KM tendo o custo de R$0.15, o valor por KM rodados foi R${valor_aluguel_km:.2f}.\n'
        f'O total de dias alugados foi {dias_alugados}. Cada dia custando R$60.00, o valor total de dias alugados foi R${valor_aluguel_dia:.2f}.\n'  
        f'O valor total a ser pago, contando dias alugados e KM rodados foi de R${valor_total_aluguel:.2f}'
        )
    
    validate_option('\nVocê deseja simular o aluguel de carros novamente? [s]im [n]ão: ')

    if encerrar:
        print('Programa encerrado.')
        break

    os.system('cls')
