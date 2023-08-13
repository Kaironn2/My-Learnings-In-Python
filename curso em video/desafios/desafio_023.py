import os

def number_analy(number):
    verify_isnumber = number.isdigit()

    if verify_isnumber:
        unit = number[-1]
        print(f'Unidade: {unit}')

        if len(number) > 1:
            ten = number[-2]
            print(f'Dezena: {ten}')

        if len(number) > 2:
            hundred = number[-3]
            print(f'Centena: {hundred}')

        if len(number) > 3:
            thousand = number[-4]
            print(f'Milhar: {thousand}')

        if len(number) > 4:
            ten_thousand = number[-5]
            print(f'Dezena de milhar: {ten_thousand}')

        if len(number) > 5:
            hundred_thousand = number[-6]
            print(f'Centena de milhar: {hundred_thousand}')
    else:
        print('Apenas números até 999999 são aceitos.')
    

number_analy('654321')
