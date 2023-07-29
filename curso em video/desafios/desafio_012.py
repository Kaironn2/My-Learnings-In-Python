import os

def desconto_produto(valor_produto, porcentagem):
    valor_com_desconto = valor_produto - (valor_produto * (porcentagem / 100))
    return valor_com_desconto

def validar_float_value(mensagem):
    while True:
        try:
            float_value = float(input(f'{mensagem}'))
            break
        except:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números. No caso de decimais, use o . no lugar da vírgula.')
    return float_value

def validate_option(mensagem):
    global encerrar

    while True:

        opcao_user = input(f'{mensagem}').upper()

        if opcao_user == '':
            os.system('cls')
            continue
        elif opcao_user[0] not in 'SN':
            os.system('cls')
            print('Opção inválida, por favor, digite SIM para continuar e NÃO para finalizar.')
            continue
        else:
            if opcao_user == 'S':
                encerrar = False
            else:
                encerrar = True
            break
    


while True:

    valor_produto_user = validar_float_value('Digite o valor do produto: R$')

    porcentagem_desconto = validar_float_value('Digite a porcentagem que você quer dar de desconto no produto: ')

    produto_com_desconto = desconto_produto(valor_produto_user, porcentagem_desconto)

    print(f'O valor original do produto é R${valor_produto_user:.2f} e com os {porcentagem_desconto}% ele fica por R${produto_com_desconto:.2f}.')

    validate_option('Você deseja calcular o desconto de outro produto? [s]im [n]ão: ')

    if encerrar:
        print('Programa encerrado.')
        break
    os.system('cls')
