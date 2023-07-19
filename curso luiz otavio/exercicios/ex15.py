from random import randint


for cpfs in range(0, 10):

    contador1 = 10
    contador2 = 11
    acumulador1 = 0
    acumulador2 = 0


    nove_digitos_cpf = ''

    for i in range(0, 9):
        nove_digitos_cpf += str(randint(0, 9))

    for numero in nove_digitos_cpf:
        acumulador1 += int(numero) * contador1
        contador1 -= 1

    digito_1 = (acumulador1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0


    dez_digitos_cpf = nove_digitos_cpf + str(digito_1)

    for numero in dez_digitos_cpf:
        acumulador2 += int(numero) * contador2
        contador2 -= 1

    digito_2 = (acumulador2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    novo_cpf_gerado = dez_digitos_cpf + str(digito_2)

    novo_cpf_gerado_formatado = (
    f'{novo_cpf_gerado[0]}{novo_cpf_gerado[1]}{novo_cpf_gerado[2]}.'
    f'{novo_cpf_gerado[3]}{novo_cpf_gerado[4]}{novo_cpf_gerado[5]}.'
    f'{novo_cpf_gerado[6]}{novo_cpf_gerado[7]}{novo_cpf_gerado[8]}-'
    f'{novo_cpf_gerado[9]}{novo_cpf_gerado[10]}'
    )

    print(novo_cpf_gerado_formatado)
    