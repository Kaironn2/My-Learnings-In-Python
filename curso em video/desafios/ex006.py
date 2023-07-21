import os

lista_numeros_multiplicados = []
lista_numeros_usuario = []
numero_mais_recente = 0
lista_mais_recente = []
numeral = 1
contador = 0
verificador = 0

def multiplos(numero):

    global lista_mais_recente
    global numero_mais_recente
    
    dobro = numero * 2
    triplo = numero * 3
    quadruplo = numero * 4

    lista_menor = []
    lista_menor.append(dobro)
    lista_menor.append(triplo)
    lista_menor.append(quadruplo)
    lista_numeros_multiplicados.append(lista_menor)

    lista_mais_recente = lista_menor
    numero_mais_recente = numero
    
    lista_numeros_usuario.append(numero)


def contadores(x):

    global contador
    global numeral
    global verificador

    contador = 0
    numeral = 1
    verificador = 0




while True:

    while True:

        try:
            numero_usuario = int(input('Digite um número inteiro: '))
        except ValueError:
            os.system('cls')
            print('Valor inválido. Por favor, digite um número inteiro.')
            continue
        
        multiplos(numero_usuario)
        os.system('cls')
        break

    
    print(f'lista_numeros_multiplicados = {lista_numeros_multiplicados}\n'
          f'lista_mais_recente = {lista_mais_recente}'
          f'lista_numeros_usuario = {lista_numeros_usuario}')


    while True:

            while True:
                    
                    print(
                    'O que você deseja fazer?\n\n'
                    '1 - Mostrar o número mais recente e seus mútiplos\n'      
                    '2 - Ver a lista inteira\n'      
                    '3 - Adicionar mais um número\n'
                    '4 - Ver o maior número das listas\n'
                    '5 - Ver a lista com a maior soma\n'
                    '6 - Encerrar o programa\n' 
                    )

                    opcao = input('Digite a opção desejada: ')

                    if opcao[0] in '12345':
                        break

                    os.system('cls')
                    print('Por favor, digite um opção válida.')


            match opcao:

                case '1':
                    print(f'O último número digitado foi {numero_mais_recente}\n'
                        f'E seus mútiplos são: ', end='')


                    verificador = len(lista_mais_recente) - 1


                    for n in lista_mais_recente:

                        if contador != verificador:
                            print(n, end='-')
                        else:
                            print(n)

                        contador += 1


                    contadores(1)


                case '2':

                    os.system('cls')

                    for item in lista_numeros_usuario:

                        print(f'{numeral}° número: {item}\n'
                            f'Múltiplos: ', end='')
                        numeral += 1

                        for lista in lista_numeros_multiplicados:

                            for number in lista:
                                verificador = len(lista) - 1

                                if contador != verificador:
                                    print(number, end='-')
                                else:
                                    print(number)

                    contadores(1)

                case '3':

                    break
