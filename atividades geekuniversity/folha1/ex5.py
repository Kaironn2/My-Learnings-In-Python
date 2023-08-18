def user_sum():
    total = 0
    for repeat in range(1, 11):
        previous_total = total
        user_num = int(input('Digite um valor: '))
        total += user_num
        print(f'{user_num} + {previous_total} = {total}')


user_sum()
