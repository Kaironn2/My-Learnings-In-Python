import os 

ca_co_hi = {'Cateto Oposto': 0, 'Cateto Adjacente': 0, 'Hipotenusa': 0}
contador = 0
lista_opcoes = []

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

        os.system('cls')
