import os


while True:

    acumulador = 0
    acumulador2 = 0
    contador = 0
    contador2 = 0


    cpf = input('Digite o seu cpf: ').replace('-', '').replace('.', '').replace(' ', '')


    cpf_lista = list(cpf)
    cpf_int = []

    if len(cpf_lista) != 11:
        os.system('cls')
        print('Formato inválido, tente novamente')
        continue
    
    os.system('cls')


    for numero in range(0, 11):                             # Converte o cpf em int e joga na lista
        cpf_int.append(int(cpf_lista[numero]))


    cpf_formatado = (
    f'{cpf_int[0]}{cpf_int[1]}{cpf_int[2]}.'
    f'{cpf_int[3]}{cpf_int[4]}{cpf_int[5]}.'
    f'{cpf_int[6]}{cpf_int[7]}{cpf_int[8]}-'
    f'{cpf_int[9]}{cpf_int[10]}'
    )



    for contagem in range(10, 1, -1):                       # Faz o produto dos 9 digitos do cpf em ordem regressiva
        contador += (cpf_int[acumulador] * contagem)
        acumulador += 1

    produto_digito_cpf = contador * 10
    resto_divisao_cpf = produto_digito_cpf % 11

    if resto_divisao_cpf <= 9:
        digito1 = resto_divisao_cpf
    else:
        digito1 = 0

    validar_cpf_digito1 = digito1 == cpf_int[9]             # Validar primeiro digito do cpf



    for contagem2 in range(11, 1, -1):                      # Faz o produto dos 10 digitos do cpf em ordem regressiva
        contador2 += (cpf_int[acumulador2] * contagem2)
        acumulador2 += 1


    produto_digito_cpf2 = contador2 * 10
    resto_divisao_cpf2 = produto_digito_cpf2 % 11

    if resto_divisao_cpf2 <= 9:
        digito2 = resto_divisao_cpf2
    else:
        digito2 = 0

    validar_cpf_digito2 = digito2 == cpf_int[10]            # Valida segundo digito do cpf



    if validar_cpf_digito1 and validar_cpf_digito2:
        print(f'O CPF de n° {cpf_formatado} é válido')
        validar_outro_cpf = input('Deseja validar outro cpf? [s]im [n]ão: ').upper().startswith('S')
        if validar_outro_cpf:
            os.system('cls')
            continue
        else:
            print('Programa finalizado.')
            break
    else:
        os.system('cls')
        print('CPF inválido, tente novamente.')
        continue
