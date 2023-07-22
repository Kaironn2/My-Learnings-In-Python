import os

lista_numeros_multiplicados = []
lista_numeros_usuario = []
numero_mais_recente = 0
lista_mais_recente = []
numeral = 1
contador = 0
verificador = 0
soma = 0
encerrar = ''

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
        
        if numero_usuario in lista_numeros_usuario:
            os.system('cls')
            print(f'O número {numero_usuario} já foi adicionado, digite outro número.')
            continue

        multiplos(numero_usuario)
        os.system('cls')
        break



    while True:

            while True:
                    
                    print(
                    'O que você deseja fazer?\n\n'
                    '1 - Mostrar o número mais recente e seus mútiplos\n'      
                    '2 - Ver a lista inteira\n'      
                    '3 - Adicionar mais um número\n'
                    '4 - Ver o maior múltiplo das listas\n'
                    '5 - Ver a soma da lista com os maiores números\n'
                    '6 - Encerrar o programa\n' 
                    )

                    opcao = input('Digite a opção desejada: ')

                    if opcao[0] in '123456':
                        break

                    os.system('cls')
                    print('Por favor, digite um opção válida.')


            match opcao:

                case '1':
                    os.system('cls')
                    print(f'O último número digitado foi {numero_mais_recente}\n'
                        f'E seus mútiplos são: ', end='')


                    verificador = len(lista_mais_recente) - 1


                    for n in lista_mais_recente:

                        if contador != verificador:
                            print(n, end='-')
                        else:
                            print(f'{n}\n')

                        contador += 1


                    contadores(1)
                    


                case '2':

                    os.system('cls')

                    
                    for lista in lista_numeros_multiplicados:

                        contadores

                        print(f'{numeral}° numero: {lista_numeros_usuario[contador]}\n'
                              f'Múltiplos {lista}\n')

                        contador += 1 




                case '3':

                    os.system('cls')
                    break
                


                case '4':

                    os.system('cls')

                    for lista in lista_numeros_multiplicados:
                        
                        for numeros in lista:
                            maior_numero = 0

                        if numeros > maior_numero:
                            maior_numero = numeros
                        
                    print(f'O maior número multiplicado é: {maior_numero}')
                


                case '5':
                    
                    os.system('cls')

                    for num in lista_numeros_usuario:

                        if num == maior_numero:
                            verificador = contador
                        
                        contador += 1

                    contadores(1)

                    for numero in lista_numeros_multiplicados[verificador]:

                        soma += numero

                    print(f'Soma da lsita com maior valor: {soma}')

                

                case '6':
                    encerrar = True
                    break
    if encerrar:
        print('Programa encerrado!')
        break
            
