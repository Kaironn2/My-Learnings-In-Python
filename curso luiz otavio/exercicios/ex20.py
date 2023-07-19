import os
lista_de_inteiros = []

while True:
    numero_inteiro = int(input('Digite um número inteiro [999 para encerrar]: '))

    if numero_inteiro == 999:
        break
    lista_de_inteiros.append(numero_inteiro)
    os.system('cls')

numero_set = set()

def duplicado(lista):
    global numero_set
    retornar = 0
    verificar = 0

    for numero in lista_de_inteiros:
        if verificar == 0:
            if numero in numero_set:
                retornar = numero
                verificar += 1
        numero_set.add(numero)

    return retornar

primeiro_numero_a_duplicar = duplicado(1)

print(f'{numero_set}\nPrimeiro número duplicado: {primeiro_numero_a_duplicar}')
