import os

numeros_digitados = []

def multiplicar(numeros_digitados):
    produto = 1
    for valor in numeros_digitados:
        produto *= valor
    return produto

while True:
    while not 000:
        numero_digitado = int(input('Digite um número (000 para parar): '))

        if numero_digitado == 000:
            break

        numeros_digitados.append(numero_digitado)
        
    resultado = multiplicar(numeros_digitados)

    print(resultado)

    option = input('Você deseja multiplicar outros números? [s]im [n]ão: ').upper().startswith('N')

    if option:
        break
    else:
        numeros_digitados = []
        os.system('cls')
        continue

print('Programa finalizado.')
