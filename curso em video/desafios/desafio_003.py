import os

def somar(numero1, numero2):
    soma = numero1 + numero2
    os.system('cls')
    print(f'{numero1} + {numero2} = {soma}')

def digitar_numero(numero):

    while True:
        try:
            numero1 = int(input('Digite um número: '))
            break
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números.')

    while True:
        try:
            numero2 = int(input('Digite mais um número: '))
            break
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite apenas números.')
            
    return numero1, numero2

while True:

    numero1, numero2 = digitar_numero('numero')

    somar(numero1, numero2)

    
    
    while True:

        opcao = input('Você deseja realizar outra operação? [s]im [n]ão: ').upper()

        if opcao == '':
            os.system('cls')
            continue
        elif opcao[0] in 'S':
            os.system('cls')
            encerrar = False
            break
        elif opcao[0] in 'N':
            encerrar = True
            break
        else:
            os.system('cls')
            print('Opção inválida. Por favor, digite SIM para continuar e NÃO para finalizar.')
    
    if encerrar:
        print('Programa encerrado')
        break