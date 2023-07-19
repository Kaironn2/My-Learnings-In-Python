import os

def par_impar(num):
    if num % 2 == 0:
        return 'par'
    return 'ímpar'

while True:
    try:
        num_user = int(input('Digite um número para saber se é par ou ímpar: '))
    except ValueError:
        os.system('cls')
        print('Valor inválido, por favor, digite um número inteiro.')
        continue
    
    result = par_impar(num_user)

    print(f'O número {num_user} é {result}')

    option = input('\nVocê deseja verificar outro número? [s]im [n]ão: ').upper().startswith('N')

    if option:
        break
    else:
        numeros_digitados = []
        os.system('cls')
        continue

print('Programa finalizado.')
