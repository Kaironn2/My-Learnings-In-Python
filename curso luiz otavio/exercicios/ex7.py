nome = input('Digite o seu primeiro nome: ')
quant_letras_do_nome = len(nome)

print()

if quant_letras_do_nome <= 4:
    print(f'Olá, {nome}! \nSeu nome é curto, tem apenas {quant_letras_do_nome} letras.')

elif quant_letras_do_nome == 5 or quant_letras_do_nome == 6:
    print(f'Olá, {nome}! \nSeu nome tem {quant_letras_do_nome} letras, é considerado normal.')

else:
    print(f'Olá, {nome}! \nSeu nome tem {quant_letras_do_nome} letras. '
    'Nomes com mais de 6 letras são considerados grandes.')
