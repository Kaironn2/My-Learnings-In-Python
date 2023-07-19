while True:
    import os

    texto_usuario = input('Digite algo para ver suas informações: ')

    
    tipo = type(texto_usuario)
    numero = texto_usuario.isdigit()
    apenas_espacos = texto_usuario.isspace()
    alfanumerico = texto_usuario.isalnum()
    alfabetico = texto_usuario.isalpha()
    maiusculo = texto_usuario.isupper()
    minusculo = texto_usuario.islower()

    if texto_usuario:
        numero = 'É um número'
    else:
        numero = 'Não é um número'

    if texto_usuario:
        apenas_espacos = 'É composto apenas de espaços.'
    else:
        apenas_espacos = 'Não é composto apenas por espaços'
    
    if texto_usuario:
        alfanumerico = 'É alfanúmerico'
    else:
        alfanumerico = 'Não é alfanúmerico'
    
    if texto_usuario:
        alfabetico = 'É alfabético'
    else:
        alfabetico = 'Não é alfabético'
    
    if maiusculo:
        maiusculo = 'Tem apenas letras maiúsculas'
    else:
        maiusculo = 'Não tem apenas letras maiúsculas'
    
    if minusculo:
        minusculo = 'Tem apenas letras minúsculas'
    else:
        minusculo = 'Não tem apenas letras minúsculas'

    os.system('cls')

    print(
        f'O tipo primitivo de "{texto_usuario}" é: {tipo}\n'
        f'Esse valor {numero}\n'
        f'{apenas_espacos}\n'
        f'{alfanumerico}\n{alfanumerico}\n'
        f'{minusculo}\n{maiusculo}'
        )

    opcao = input('Você deseja realizar outra operação? [s]im [n]ão: ').upper().startswith('S')

    if opcao:
        os.system('cls')
    else:
        print('Programa finalizado.')
        break
