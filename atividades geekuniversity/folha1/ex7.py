import os


def average():
    total = 0
    verify_break = 1
    while True:
        previous_total = total
        user_num = int(input('Digite um valor: '))
        if user_num <= 0:
            os.system('cls')
            print('Por favor, digite apenas números maiores que zero.')
            continue
        os.system('cls')
        total += user_num
        print(f'{user_num} + {previous_total} = {total}')

        if verify_break == 10:
            break

        verify_break += 1

    media = total / 10
    print(f'A média foi {media}')


average()
