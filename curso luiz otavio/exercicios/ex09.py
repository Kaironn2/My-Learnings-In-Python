while True:
    print()
    valor_1 = input('Digite um número: ')
    valor_2 = input('Digite mais um número: ')
    operador = input('Digite o operador (+-/*): ')

    validar_valor_1 = None
    validar_valor_2 = None
    validar_operadores = '+-*/'

    try:
        valor_1 = float(valor_1)
        validar_valor_1 = True
    except:
        validar_valor_1 = None


    try:
        valor_2 = float(valor_2)
        validar_valor_2 = True
    except:
        validar_valor_2 = None

    print()

    if validar_valor_1 == None:
        print('O primeiro valor digitado não é válido.')
        continue

    if validar_valor_2 == None:
        print('O segundo valor digitado não é válido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    
    if operador not in validar_operadores:
        print('O operador digitado não é válido.')
        continue 

    ###

    if operador == '+':
        resultado = valor_1 + valor_2

    elif operador == '-':
        resultado = valor_1 - valor_2

    elif operador == '/':
        resultado = valor_1 / valor_2

    elif operador == '*':
        resultado = valor_1 * valor_2
        operador = 'x'

    else:
        print('Se chegou aqui, parabéns')

    print('O resultado da sua conta foi: ')
    print(f'{valor_1} {operador} = {resultado}')

    sair = input('\nVocê deseja encerrar o programa? [s]im: ').lower().startswith('s')
    
    if sair:
        print('Programa encerrado.')
        break
