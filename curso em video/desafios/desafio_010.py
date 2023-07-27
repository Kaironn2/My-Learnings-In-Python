import os

contador = 1

def definir_contador(x):
    global contador

    contador = x

moedas = {
            'Dólar Americano (USD$)': 1, 'Euro (EUR$)': 1.11, 'Iene (JPY$)': 0.0071, 'Libra Esterlina (GBP$)': 1.29, 'Franco Suiço (CHF$)': 1.16, 
            'Dólar Canadense (CAD$)': 0.76, 'Dólar Australiano (AUD$)': 0.68, 'Yuan Chinês (CNY$)': 0.14, 'Coroa Sueca (SEK$)': 0.096, 'Real Brasileiro (R$)': 0.21
        }


moedas_ordenadas = sorted(moedas.keys())

lista_de_moedas = list(moedas_ordenadas)
lista_de_moedas.insert(0, 0)


opcoes_moedas = []
quant_moedas = len(moedas)
quant_opcoes = quant_moedas + 1

for i in range(1, quant_opcoes):

    contador_string = str(contador)
    opcoes_moedas.append(contador_string)
    contador += 1

def converter_moeda(valor_moeda1, valor_moeda2, valor_do_usuario):
    conversao_usd = valor_do_usuario * valor_moeda1
    valor_convertido = conversao_usd / valor_moeda2

    return valor_convertido

def listar_moedas(y):
    global contador

    for moeda in moedas_ordenadas:
            print(f'{contador} - {moeda}')
            contador += 1

while True:
    

    while True:
        
        definir_contador(1)
        listar_moedas(1)
        
        opcao1 = input('\nDe qual moeda você quer converter o valor? ')


        if opcao1 not in opcoes_moedas:
            os.system('cls')
            print('Opção inválida. Por favor, insira uma das opções listadas.')
            continue

        opcao1_int = int(opcao1)

        break
    
    os.system('cls')
    
    while True:
        
        definir_contador(1)
        listar_moedas(1)
        
        opcao2 = input('\nE para qual moeda você quer converter? ')


        if opcao2 not in opcoes_moedas:
            os.system('cls')
            print('Opção inválida. Por favor, insira uma das opções listadas.')
            continue
        
        opcao2_int = int(opcao2)

        break

    os.system('cls')
    

    while True:    
        try:
            valor_usuario = float(input('Agora digite o valor que você quer converter: '))
            break
        except ValueError:
            os.system('cls')
            print(f'Valor inválido. Por favor, digite apenas números. No caso de precisar da vírgula, utilize o . no lugar da vírgula. Ex: 2.30')
            continue

    moeda1 = lista_de_moedas[opcao1_int]
    moeda2 = lista_de_moedas[opcao2_int]
    valor_moeda1 = moedas[moeda1]
    valor_moeda2 = moedas[moeda2]

    moeda_convertida = converter_moeda(valor_moeda1, valor_moeda2, valor_usuario)
    
    os.system('cls')
    print(f'{valor_usuario:.2f} {moeda1} --> {moeda_convertida:.2f} {moeda2}\n')

    while True:

        opcao_user = input('Você deseja realizar outra conversão? [s]im [n]ão: ').upper()

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
