def get_min_max():
    num_list = []
    verify_break = 1
    while verify_break <= 10:
        user_num = int(input('Digite um valor inteiro: '))
        num_list.append(user_num)
        verify_break += 1
    min_value = min(num_list)
    max_value = max(num_list)
    print(f'O maior valor digitado foi {min_value} e o maior foi {max_value}')


get_min_max()
