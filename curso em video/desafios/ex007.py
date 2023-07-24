import os
lista_de_notas = []
soma_das_notas = 0

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

    media = soma_das_notas / quantidade_de_notas

    print(f'A média é {media}')

    outra_media = input('\nVocê deseja calcular outra média? [s]im [n]ão: ').upper().startswith('S')

    if outra_media is False:
        print('Programa encerrado')
        break

    os.system('cls')