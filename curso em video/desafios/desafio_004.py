import os

def numero(texto_usuario):
    number = texto_usuario.isdigit()

    if number:
        number = 'É composto apenas por números'
    else:
        number = 'Não é composto apenas por números'
    return number

def apenas_espacos(texto_usuario):
    apenas_espacos = texto_usuario.isspace()

    if apenas_espacos:
        apenas_espacos = 'É composto apenas de espaços.'
    else:
        apenas_espacos = 'Não é composto apenas de espaços.'
    return apenas_espacos

def alfanumerico(texto_usuario):
    alfanumerico = texto_usuario.isalnum()

    if alfanumerico:
        alfanumerico = 'É alfanúmerico'
    else:
        alfanumerico = 'Não é alfanúmerico'
    return alfanumerico

def alfabetico(texto_usuario):
    alfabetico = texto_usuario.isalpha()

    if alfabetico:
        alfabetico = 'É alfabético'
    else:
        alfabetico = 'Não é alfabético'
    return alfabetico

def maiusculo(texto_usuario):
    maiusculo = texto_usuario.isupper()

    if maiusculo:
        maiusculo = 'Tem apenas letras maiúsculas'
    else:
        maiusculo = 'Não tem apenas letras maiúsculas'
    return maiusculo

def minusculo(texto_usuario):
    minusculo = texto_usuario.islower()

    if minusculo:
        minusculo = 'Tem apenas letras minúsculas'
    else:
        minusculo = 'Não tem apenas letras minúsculas'
    return minusculo



while True:  
    
    texto_usuario = input('Digite algo para ver suas informações: ')

    v_tipo = type(texto_usuario)
    v_numero = numero(texto_usuario)
    v_apenas_espacos = apenas_espacos(texto_usuario)
    v_alfanumerico = alfanumerico(texto_usuario)
    v_alfabetico = alfabetico(texto_usuario)
    v_maiusculo = maiusculo(texto_usuario)
    v_minusculo = minusculo(texto_usuario)

    os.system('cls')

    print(
        f'O tipo primitivo de "{texto_usuario}" é: {v_tipo}\n'
        f'{v_numero}\n'
        f'{v_apenas_espacos}\n'
        f'{v_alfanumerico}\n{v_alfabetico}\n'
        f'{v_minusculo}\n{v_maiusculo}'
        )

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
