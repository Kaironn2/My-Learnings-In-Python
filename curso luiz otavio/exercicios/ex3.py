primeiro_valor = float(input('Digite um valor: '))
segundo_valor = float(input('Digite mais um valor: '))

if primeiro_valor == segundo_valor:
    print(f'\n{primeiro_valor} é igual a {segundo_valor}')
elif primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}')
else:
    print(f'{primeiro_valor} é menor que {segundo_valor}')
