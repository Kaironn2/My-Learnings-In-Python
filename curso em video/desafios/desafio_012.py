import os

def desconto(valor_produto, porcentagem):
    valor_com_desconto = valor_produto - (valor_produto * (porcentagem / 100))
    return valor_com_desconto

while True:

    while True:

        try:
            valor_produto = float(input('Digite o valor do produto: R$'))
            break
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números. Para decimais, use o . no lugar da vírgula.')
    
    while True:
        try:
            porcentagem_desconto = float(input('Informe qual a porcentagem de desconto que você quer dar no produto: '))
            break
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números. Para decimais, use o . no lugar da vírgula.')
    
    valor_com_desconto = desconto(valor_produto, porcentagem_desconto)

    print(f'O valor original do produto é {valor_produto:.2f} e com {porcentagem_desconto}% de desconto ficará R${valor_com_desconto:.2f}.')

    while True:

        opcao_user = input('Você deseja calcular outro desconto? [s]im [n]ão: ').upper()

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
    
    if encerrar:
        print('Programa encerrado.')
        break

    os.system('cls')
