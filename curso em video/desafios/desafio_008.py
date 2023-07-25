import os

medidas = {
    'milimetro': 0, 'centimetro': 0, 'decimetro': 0,
    'metro': 0, 'decametro': 0, 'hectometro': 0, 'quilometro': 0 
    }

medida_em_metros = 0


def converter_para_metros(medida):
    global opcao
    global medida_em_metros
    
    match opcao:
    
        case '1':
            medida_em_metros = medida * 1000
        
        case '2':
            medida_em_metros = medida * 100

        case '3':
            medida_em_metros = medida * 10
        
        case '4':
            medida_em_metros = medida
        
        case '5':
            medida_em_metros = medida / 10
        
        case '6':
            medida_em_metros = medida / 100

        case '7':
            medida_em_metros = medida / 1000
        


def converter_todas_medidas(medida):
    global medidas

    medidas['milimetro'] = medida / 1000
    medidas['centimetro'] = medida / 100
    medidas['decimetro'] = medida / 10
    medidas['metro'] = medida
    medidas['decametro'] = medida * 10
    medidas['hectometro'] = medida * 100
    medidas['quilometro'] = medida * 1000
        

while True:


    while True:

        print(
            'Qual é o tipo da medida que você quer converter?\n\n'
            '1 - Milimimetro\n'
            '2 - Centímetro\n'
            '3 - Decímetro\n'
            '4 - Metro\n'
            '5 - Decâmetro\n'
            '6 - Hectômetro\n'
            '7 - Quilômetro\n'
            )
        
        opcao = input('Digite a opção desejada: ')

        if opcao not in '1234567':
            os.system('cls')
            print('Opção inválida. Por favor, digite uma das opções exibidas.\n')
            continue
        
        os.system('cls')
        break


    try:
        medida_usuario = float(input('Digite o valor que você quer converter: '))
    except ValueError:
        os.system('cls')
        print('Valor inválido. Por favor, digite um número.')
        continue

    os.system('cls')

    converter_para_metros(medida_usuario)
    converter_todas_medidas(medida_em_metros)


    print(
        f'Medida em milímetros:  ', medidas['milimetro'],'mm\n'
        f'Medida em centímetros: ', medidas['centimetro'],'cm\n'
        f'Medida em decímetros:  ', medidas['decimetro'],'dm\n'
        f'Medida em metros:      ', medidas['metro'],'m\n'
        f'Medida em decâmetros:  ', medidas['decametro'],'dam\n'
        f'Medida em hectômetros: ', medidas['hectometro'],'hm\n'
        f'Medida em quilômetros: ', medidas['quilometro'],'km\n'    
    )

    finalizar = input('Você deseja converter outro número? [s]im [n]ão: ').upper().startswith('n')

    if finalizar:
        print('Programa encerrado')
        break

    os.system('cls')
