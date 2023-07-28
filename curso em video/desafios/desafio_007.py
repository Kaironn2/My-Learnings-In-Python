import os
lista_de_notas = []
soma_das_notas = 0

def media(soma_das_notas, quantidade_de_notas):
    soma = soma_das_notas / quantidade_de_notas
    return soma

while True:

    while True:
        
        contador = 1

        try:
            nota_usuario = float(input('Digite a nota: '))
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite um número.')
            continue

        lista_de_notas.append(nota_usuario)

        digitar_mais_notas = input('Você deseja digitar mais alguma nota? [s]im [n]ão: ').upper().startswith('S')

        quantidade_de_notas = len(lista_de_notas)

        if digitar_mais_notas is False:
            contador = 1
            break

        os.system('cls')

        

        print(f'Notas digitadas: ', end='')
        for notas_digitadas in lista_de_notas:

            if contador == quantidade_de_notas:
                print(notas_digitadas)
            else:
                print(notas_digitadas, end=' - ')
                contador += 1
           

    os.system('cls')


    for nota in lista_de_notas:
        soma_das_notas += nota
        print(f'Nota {contador}: {nota}')
        contador += 1

    media_aluno = media(soma_das_notas, quantidade_de_notas)

    print(f'A média é {media_aluno}')

    while True:

        opcao = input('Você deseja calcular outra média? [s]im [n]ão: ').upper()

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
