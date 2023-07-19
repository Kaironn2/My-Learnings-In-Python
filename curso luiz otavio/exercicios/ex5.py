number = input('Digite um número inteiro: ')

if number.isdigit():

    number_int = int(number)
    resto_divisao = number_int % 2 == 0
    par_ou_impar = 'ímpar'

    if resto_divisao:
        par_ou_impar = 'par'

    print(f'O número escolhido foi {number_int} e ele é {par_ou_impar}')

else:
    print('Desculpe, mas você não digitou um número inteiro.')
