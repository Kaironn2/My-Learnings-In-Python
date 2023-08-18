def odd_sucessors(num, quant):
    if num % 2 == 0:
        current_odd = num + 1
    else:
        current_odd = user_num + 2
    print(f'{num}-{current_odd}', end='-')
    for numbers in range(1, quant):
        current_odd += 2
        print(current_odd, end='-')
    print('FIM')


user_num = int(
    input('Digite um número para ver seus sucessores ímpares: '))
user_quant = int(
    input('Agora digite quantos sucessores você deseja ver: '))

odd_sucessors(user_num, user_quant)
