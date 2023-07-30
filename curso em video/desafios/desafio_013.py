import os

def aumento_salario(valor_salario, porcentagem):
    valor_com_desconto = valor_salario + (valor_salario * (porcentagem / 100))
    return valor_com_desconto

def validar_float_value(mensagem):
    while True:
        try:
            float_value = float(input(f'{mensagem}'))
            return float_value
        except:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números. No caso de decimais, use o . no lugar da vírgula.')

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
    


while True:

    valor_salario = validar_float_value('Digite o valor atual do salário: R$')

    porcentagem_desconto = validar_float_value('Digite a porcentagem que você quer dar de aumento: ')

    produto_com_desconto = aumento_salario(valor_salario, porcentagem_desconto)

    print(f'O salário atual é R${valor_salario:.2f} e com o reajuste de {porcentagem_desconto}% ele ficará R${produto_com_desconto:.2f}.')

    validate_option('Você deseja calcular o desconto de outro produto? [s]im [n]ão: ')

    if encerrar:
        print('Programa encerrado.')
        break
    os.system('cls')
