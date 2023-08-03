import os 
from math import sqrt

ca_co_hi = {'Cateto Oposto': 0, 'Cateto Adjacente': 0, 'Hipotenusa': 0}
contador = 0
acumulador = 0
lista_opcoes = []

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

def redefinir_lados():
    global ca_co_hi
    ca_co_hi = {'Cateto Oposto': 0, 'Cateto Adjacente': 0, 'Hipotenusa': 0}

def redefinir_contador(valor_contador):
    global contador
    contador = valor_contador

def redefinir_acumulador(valor_acumulador):
    global acumulador
    acumulador = valor_acumulador

def opcoes_inseridas():
        pular_linha = None
        for chave, valor in ca_co_hi.items():
            if valor > 0:
                print(f'{chave}: {valor}')
                pular_linha = True
        if pular_linha:
            print()

def mostrar_menu():
    global contador
    global lista_opcoes

    while True:

        opcoes_inseridas()
        redefinir_contador(1)

        for chave in ca_co_hi.keys():
            print(f'{contador} - {chave}')
            contador += 1
        print(f'{contador} - Sair')
        
        opcao = input('\nInsira uma opção: ')

        if opcao == '':
            os.system('cls')
            print('Você não digitou nada. Digite uma das opções listadas')
        elif len(opcao) > 1:
            os.system('cls')
            print('Digite apenas uma opção.')
        elif opcao in '123':
            if opcao not in lista_opcoes:
                lista_opcoes.append(opcao)
                return opcao[0]
            else:
                os.system('cls')
                print('Essa opção já foi inserida. Digite outra opção.')
        else:
            os.system('cls')
            print('Opção inválida. Por favor, digite uma das opções listadas.')


while True:

    redefinir_lados()

    while True:

        opcao = mostrar_menu()

        os.system('cls')

        match opcao:

            case '1':
                ca_co_hi['Cateto Oposto'] = validar_float('Insira o valor do cateto oposto: ')
            case '2':
                ca_co_hi['Cateto Adjacente'] = validar_float('Insira o valor do cateto adjacente: ')
            case '3':
                ca_co_hi['Hipotenusa'] = validar_float('Insira o valor do hipotenusa: ')

        for chave, valor in ca_co_hi.items():
            if valor > 0:
                acumulador += 1
        
        if acumulador == 2:
            break
        
        redefinir_acumulador(0)
        os.system('cls')

    cateto_oposto = ca_co_hi['Cateto Oposto']
    cateto_adjacente = ca_co_hi['Cateto Adjacente']
    hipotenusa = ca_co_hi['Hipotenusa']

    if cateto_oposto > 0 and cateto_adjacente > 0:
        hipotenusa = sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))
        ca_co_hi['Hipotenusa'] = hipotenusa
    
    elif cateto_oposto > 0 and hipotenusa > 0:
        cateto_adjacente = sqrt((hipotenusa ** 2) - (cateto_oposto ** 2))
        ca_co_hi['Cateto Adjacente'] = cateto_adjacente
    
    elif cateto_adjacente > 0 and hipotenusa > 0:
        cateto_oposto = sqrt((hipotenusa ** 2) - (cateto_adjacente ** 2))
        ca_co_hi['Cateto Oposto'] = cateto_oposto

    for chave, valor in ca_co_hi.items():
        print(f'{chave}: {valor:.2f}')

    validate_option('Você deseja calcular outro triângulo retângulo? [s]im [n]ão: ')

    if encerrar:
        print('Programa encerrado.')
        break

    os.system('cls')
