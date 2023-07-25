import os

def tabuada(numero):
    for num in range(1, 11):
        multiplicar = numero * num
        print(f'{numero} x {num} =  {multiplicar}')

while True:

    try:
        numero_usuario = int(input('Digite um número para ver sua tabuada: '))
    except ValueError:
        os.system('cls')
        print('Valor inválido. Por favor, digite um número inteiro.')
        continue

    tabuada(numero_usuario)


    while True:

        opcao_user = input('Você deseja ver a tabuada de outro número? [s]im [n]ão: ').upper()

        if opcao_user[0] not in 'SN':
            os.system('cls')
            tabuada(numero_usuario)
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
