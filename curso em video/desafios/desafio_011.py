import os

def calcular_area(largura, altura):
    area = largura * altura
    return area

def calcular_tinta(area):
    quantidade_de_tinta = area / 2
    return quantidade_de_tinta

    
while True:

    while True:
        try:
            largura_parede = float(input('Digite a largura, em metros, da parede: '))
            break
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números')

    while True:
        try:
            altura_parede = float(input('Digite a altura, em metros, da parede: '))
            break
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números')

    os.system('cls')
    area_parede = calcular_area(largura_parede, altura_parede)
    quantidade_de_tinta = calcular_tinta(area_parede)

    print(f'A sua parede tem {largura_parede}m de largura e {altura_parede}m de altura,'
          f' resultando numa área de {area_parede}m², sendo necessários {quantidade_de_tinta}L de tinta para pintá-la.')
    
    while True:

        opcao_user = input('Você deseja calcular a quantidade de tinta novamente? [s]im [n]ão: ').upper()

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
