def sum_pair_numbers(quant):
    total = 0
    current_pair = 2
    counter = 1
    for repeat in range(1, quant + 1):
        total += current_pair
        current_pair += 2
        print(total, counter)
        counter += 1
    print(f'A soma dos primeiros {quant} números é igual a {total}')


sum_pair_numbers(50)
