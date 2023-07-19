primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite mais um valor: ')

if type(primeiro_valor) == str or type(segundo_valor) == str:
    comparacao = primeiro_valor == segundo_valor

    if comparacao == True:
        print(f'{primeiro_valor} é igual a {segundo_valor}')

    else:
        print(f'{primeiro_valor} é diferente de {segundo_valor}')

else:
    primeiro_numero = float(primeiro_valor)
    segundo_numero = float(segundo_valor)

    if primeiro_numero == segundo_numero:
        print(f'{primeiro_valor} é igual a {segundo_valor}')

    elif primeiro_numero > segundo_numero:
        print(f'{primeiro_valor} é maior que {segundo_valor}')
        
    else:
        print(f'{primeiro_valor} é menor que {segundo_valor}')
