import os

lista_de_inteiros = []



while True:
    try:
        numero_inteiro = int(input('Digite um número inteiro [999 para encerrar]: '))

    except ValueError:
        os.system('cls')
        print('Valor inválido. Por favor, digite apenas números inteiros.')

    if numero_inteiro == 999:
        break

    lista_de_inteiros.append(numero_inteiro)
    os.system('cls')



numero_set = set()

def duplicado(lista):
    global numero_set
    first_repeat = 0
    verificar = 0

    for numero in lista_de_inteiros:

        if verificar == 0:

            if numero in numero_set:
                first_repeat = numero
                verificar += 1
                return first_repeat

        numero_set.add(numero)

    return -1


primeiro_numero_a_duplicar = duplicado(1)


if primeiro_numero_a_duplicar == -1:
    print(f'{numero_set}\nNão há números duplicados')

else:
    print(f'{numero_set}\nPrimeiro número duplicado: {primeiro_numero_a_duplicar}')
