import os

contador = 1

def definir_contador(x):
    global contador

    contador = x

moedas = {
            'Dólar Americano (USD)': 1, 'Euro (EUR)': 1.11, 'Iene (JPY)': 0.0071, 'Libra Esterlina (GBP)': 1.29, 'Franco Suiço (CHF)': 1.16, 
            'Dólar Canadense (CAD)': 0.76, 'Dólar Australiano (AUD)': 0.68, 'Yuan Chinês (CNY)': 0.14, 'Coroa Sueca (SEK)': 0.096, 'Real': 0.21
            }

moedas_ordenadas = sorted(moedas.keys())

opcoes_moedas = []
quant_moedas = len(moedas)
quant_opcoes = quant_moedas + 1

for i in range(1, quant_opcoes):

    contador_string = str(contador)
    opcoes_moedas.append(contador_string)
    contador += 1

def converter_usd(moeda_usuario, valor_usuario):
    unidade_moeda_em_usd = moeda_usuario
    valor_convertido = valor_usuario * moeda_usuario

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
        
        opcao1 = input('\nDe qual moeda você quer converter o valor? ').upper()


        if opcao1 not in opcoes_moedas:
            os.system('cls')
            print('Opção inválida. Por favor, insira uma das opções listadas.')
            continue

        break


    while True:    
        try:
            valor_usuario = float(input('Agora digite o valor que você quer converter: '))
            break
        except ValueError:
            os.system('cls')
            print(f'Valor inválido. Por favor, digite apenas núemros e utilize o . no lugar da vírgula.')
            continue
